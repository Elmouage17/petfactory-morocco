"""
ERPNext ↔ PetFactory Digital Twin Connector
Bridges production simulation data with ERPNext records.

Usage:
    connector = ERPNextConnector("https://erp.petfactory.ma", API_KEY, API_SECRET)
    connector.push_stage_log("PF-2027.03.15-0001", "Extrusion", {...})
    recipe = connector.pull_recipe("Premium Dog Adult")
"""

import os
import requests
from datetime import datetime, timedelta
from typing import Optional


class ERPNextConnector:

    def __init__(
        self,
        url: str = "",
        api_key: str = "",
        api_secret: str = "",
    ):
        self.url = url or os.getenv("ERPNEXT_URL", "http://localhost:8000")
        self.api_key = api_key or os.getenv("ERPNEXT_API_KEY", "")
        self.api_secret = api_secret or os.getenv("ERPNEXT_API_SECRET", "")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"token {self.api_key}:{self.api_secret}",
            "Content-Type": "application/json",
        })

    def _get(self, doctype: str, name: str = "", filters: dict = None, fields: list = None):
        if name:
            resp = self.session.get(f"{self.url}/api/resource/{doctype}/{name}")
        else:
            params = {}
            if filters:
                params["filters"] = str(filters)
            if fields:
                params["fields"] = str(fields)
            resp = self.session.get(f"{self.url}/api/resource/{doctype}", params=params)
        resp.raise_for_status()
        return resp.json().get("data", {})

    def _post(self, doctype: str, data: dict):
        resp = self.session.post(
            f"{self.url}/api/resource/{doctype}",
            json={"data": data},
        )
        resp.raise_for_status()
        return resp.json().get("data", {})

    def _put(self, doctype: str, name: str, data: dict):
        resp = self.session.put(
            f"{self.url}/api/resource/{doctype}/{name}",
            json={"data": data},
        )
        resp.raise_for_status()
        return resp.json().get("data", {})

    # ── Recipe Management ──────────────────────────────────────────────────

    def pull_recipe(self, recipe_name: str) -> dict:
        """Pull recipe formulation from ERPNext for use in simulator."""
        recipe = self._get("Recipe Formulation", recipe_name)
        return {
            "name": recipe.get("recipe_name"),
            "species": recipe.get("species"),
            "target_weight_kg": recipe.get("target_batch_weight_kg"),
            "extruder_temp_c": recipe.get("extruder_temp_c"),
            "extruder_moisture_pct": recipe.get("extruder_moisture_pct"),
            "dryer_target_moisture_pct": recipe.get("dryer_target_moisture_pct"),
            "kibble_density_target": recipe.get("kibble_density_target"),
            "coating_fat_pct": recipe.get("coating_fat_pct"),
            "ingredients": [
                {
                    "item": ing.get("item"),
                    "percentage": ing.get("percentage"),
                    "weight_kg": ing.get("weight_kg"),
                }
                for ing in recipe.get("ingredients", [])
            ],
        }

    def pull_bom(self, item_code: str) -> dict:
        """Pull Bill of Materials from ERPNext."""
        bom = self._get("BOM", filters={"item": item_code, "is_active": 1})
        if isinstance(bom, list) and bom:
            return self._get("BOM", bom[0]["name"])
        return {}

    # ── Production Data Push ───────────────────────────────────────────────

    def push_stage_log(
        self,
        batch_id: str,
        stage: str,
        temperature_c: Optional[float] = None,
        moisture_pct: Optional[float] = None,
        notes: str = "",
    ):
        """Push a production stage measurement from the simulator to ERPNext."""
        row = {
            "stage": stage,
            "start_time": datetime.now().isoformat(),
            "passed_qc": 1,
        }
        if temperature_c is not None:
            row["temperature_c"] = round(temperature_c, 1)
        if moisture_pct is not None:
            row["moisture_pct"] = round(moisture_pct, 2)
        if notes:
            row["operator_notes"] = notes

        return self._put("Production Batch Record", batch_id, {
            "stage_logs": [row],
        })

    def create_batch_record(
        self,
        work_order: str,
        recipe: str,
        shift: str = "Morning (06:00-14:00)",
    ) -> dict:
        """Create a new Production Batch Record for a production run."""
        return self._post("Production Batch Record", {
            "work_order": work_order,
            "recipe": recipe,
            "production_date": datetime.now().strftime("%Y-%m-%d"),
            "shift": shift,
            "qc_result": "Pending",
            "onssa_traceable": 1,
        })

    def update_batch_output(
        self,
        batch_id: str,
        yield_kg: float,
        waste_kg: float,
        qc_result: str = "Pass",
    ):
        """Update batch output after production is complete."""
        target = self._get("Production Batch Record", batch_id)
        target_weight = target.get("recipe", {}).get("target_batch_weight_kg", 5000)
        yield_pct = (yield_kg / target_weight * 100) if target_weight else 0

        return self._put("Production Batch Record", batch_id, {
            "yield_kg": round(yield_kg, 1),
            "waste_kg": round(waste_kg, 1),
            "yield_pct": round(yield_pct, 2),
            "qc_result": qc_result,
        })

    # ── HACCP Logging ──────────────────────────────────────────────────────

    def log_haccp_measurement(
        self,
        ccp_id: str,
        measured_value: float,
        unit: str,
        batch_record: str = "",
        within_limits: bool = True,
        corrective_action: str = "",
    ) -> dict:
        """Log a HACCP critical control point measurement."""
        data = {
            "ccp_id": ccp_id,
            "measured_value": measured_value,
            "unit": unit,
            "monitoring_time": datetime.now().isoformat(),
            "within_limits": 1 if within_limits else 0,
        }
        if batch_record:
            data["batch_record"] = batch_record
        if corrective_action:
            data["corrective_action"] = corrective_action
        return self._post("HACCP Control Point Log", data)

    # ── Traceability Queries ───────────────────────────────────────────────

    def trace_forward(self, ingredient_batch: str) -> list:
        """Find all finished goods that used a specific ingredient batch."""
        records = self._get(
            "Production Batch Record",
            filters={"ingredient_lots.batch_no": ingredient_batch},
            fields=["name", "finished_batch_no", "production_date", "recipe"],
        )
        return records if isinstance(records, list) else []

    def trace_backward(self, finished_batch: str) -> dict:
        """Find all ingredients used in a finished goods batch."""
        record = self._get(
            "Production Batch Record",
            filters={"finished_batch_no": finished_batch},
        )
        if isinstance(record, list) and record:
            full = self._get("Production Batch Record", record[0]["name"])
            return {
                "batch": full.get("name"),
                "recipe": full.get("recipe"),
                "date": full.get("production_date"),
                "ingredients": full.get("ingredient_lots", []),
                "stage_logs": full.get("stage_logs", []),
                "qc_result": full.get("qc_result"),
            }
        return {}

    # ── Quality Inspection ─────────────────────────────────────────────────

    def create_quality_inspection(
        self,
        batch_no: str,
        item_code: str,
        inspection_type: str = "In Process",
        readings: list = None,
    ) -> dict:
        """Create a Quality Inspection record."""
        data = {
            "inspection_type": inspection_type,
            "reference_type": "Stock Entry",
            "item_code": item_code,
            "batch_no": batch_no,
            "inspected_by": "Administrator",
        }
        if readings:
            data["readings"] = readings
        return self._post("Quality Inspection", data)
