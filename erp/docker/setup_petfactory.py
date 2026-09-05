"""
Post-install setup for PetFactory Morocco ERPNext.
Run this after docker compose up to configure the company, warehouses,
item groups, and workstations for the 5 TPH pet food line.

Usage:
    pip install requests
    python setup_petfactory.py

Requires ERPNext running at http://localhost:8080
"""

import requests
import sys
import time

BASE_URL = "http://localhost:8080"
AUTH = ("Administrator", "admin")


def api(method, doctype, data=None, name=None):
    url = f"{BASE_URL}/api/resource/{doctype}"
    if name:
        url += f"/{name}"
    if method == "GET":
        r = requests.get(url, auth=AUTH)
    elif method == "POST":
        r = requests.post(url, json=data, auth=AUTH)
    elif method == "PUT":
        r = requests.put(url, json=data, auth=AUTH)
    else:
        raise ValueError(f"Unknown method: {method}")

    if r.status_code >= 400:
        print(f"  WARN: {method} {doctype}/{name or ''} -> {r.status_code}: {r.text[:200]}")
        return None
    return r.json().get("data", {})


def wait_for_erpnext():
    print("Waiting for ERPNext to be ready...")
    for i in range(60):
        try:
            r = requests.get(f"{BASE_URL}/api/method/frappe.ping", auth=AUTH, timeout=5)
            if r.status_code == 200:
                print("ERPNext is ready.\n")
                return True
        except requests.ConnectionError:
            pass
        time.sleep(5)
    print("ERROR: ERPNext did not start in 5 minutes.")
    sys.exit(1)


def setup_company():
    print("[1/7] Setting up company...")
    api("POST", "Company", {
        "company_name": "PetFactory Maroc SARL",
        "abbr": "PFM",
        "default_currency": "MAD",
        "country": "Morocco",
        "chart_of_accounts": "Standard",
        "domain": "Manufacturing",
    })
    print("  Company: PetFactory Maroc SARL (MAD)")


def setup_warehouses():
    print("[2/7] Setting up warehouses...")
    warehouses = [
        ("Raw Materials Store - PFM", "Raw materials: grains, proteins, additives"),
        ("Silo Storage - PFM", "200T steel silo + 14 surge bins"),
        ("Work In Progress - PFM", "Production line WIP"),
        ("Finished Goods - PFM", "Packaged pet food ready for dispatch"),
        ("Quarantine - PFM", "QC hold / non-conforming product"),
        ("Packaging Materials - PFM", "Bags, labels, pallets"),
    ]
    for name, desc in warehouses:
        api("POST", "Warehouse", {
            "warehouse_name": name.replace(" - PFM", ""),
            "company": "PetFactory Maroc SARL",
            "warehouse_type": "Store",
        })
        print(f"  Warehouse: {name}")


def setup_item_groups():
    print("[3/7] Setting up item groups...")
    groups = {
        "Raw Materials": [
            "Grains & Cereals",
            "Protein Meals",
            "Fats & Oils",
            "Vitamins & Minerals",
            "Additives & Flavors",
        ],
        "Packaging": [
            "Bags",
            "Labels",
            "Pallets",
        ],
        "Finished Goods": [
            "Dog Food",
            "Cat Food",
        ],
    }
    for parent, children in groups.items():
        api("POST", "Item Group", {
            "item_group_name": parent,
            "parent_item_group": "All Item Groups",
        })
        for child in children:
            api("POST", "Item Group", {
                "item_group_name": child,
                "parent_item_group": parent,
            })
            print(f"  Group: {parent} > {child}")


def setup_workstations():
    print("[4/7] Setting up workstations (Famsun 5 TPH line)...")
    workstations = [
        ("WS-RECV", "Reception & Storage", "Drum Precleaner 40 t/h, Permanent Magnet, 200T Silo", 0),
        ("WS-GRIND", "Grinding", "Hammermill 200 kW, 3000 RPM, 6-7 t/h", 200),
        ("WS-MIX", "Mixing", "Twin-shaft paddle mixer, 2000 kg batch", 30),
        ("WS-EXTR", "Preconditioning & Extrusion", "Famsun twin-screw extruder, 5 TPH", 350),
        ("WS-DRY", "Drying", "3-pass belt dryer, target ≤10% moisture", 150),
        ("WS-COOL", "Cooling", "Counter-flow cooler", 15),
        ("WS-COAT", "Coating", "Vacuum coater / drum enrober", 20),
        ("WS-PACK", "Packaging", "Auto bagging 5/10/20 kg, metal detector", 10),
    ]
    for ws_id, name, desc, kw in workstations:
        api("POST", "Workstation", {
            "workstation_name": f"{ws_id}: {name}",
            "description": desc,
            "production_capacity": 5,
            "electricity_cost": round(kw * 0.001 * 1.2, 2),
        })
        print(f"  Workstation: {ws_id} - {name} ({kw} kW)")


def setup_sample_items():
    print("[5/7] Creating sample items...")
    raw_materials = [
        ("RM-CORN", "Corn (Maize)", "Grains & Cereals", "Kg"),
        ("RM-WHEAT", "Wheat", "Grains & Cereals", "Kg"),
        ("RM-RICE", "Rice Broken", "Grains & Cereals", "Kg"),
        ("RM-CHKN", "Chicken Meal", "Protein Meals", "Kg"),
        ("RM-FISH", "Fish Meal", "Protein Meals", "Kg"),
        ("RM-SOYA", "Soybean Meal", "Protein Meals", "Kg"),
        ("RM-CHKF", "Chicken Fat", "Fats & Oils", "Kg"),
        ("RM-VITM", "Vitamin Premix", "Vitamins & Minerals", "Kg"),
        ("RM-MINM", "Mineral Premix", "Vitamins & Minerals", "Kg"),
        ("RM-SALT", "Salt (NaCl)", "Additives & Flavors", "Kg"),
    ]
    finished_goods = [
        ("FG-DOG-ADL-10", "Premium Dog Adult 10kg", "Dog Food", "Unit"),
        ("FG-DOG-ADL-20", "Premium Dog Adult 20kg", "Dog Food", "Unit"),
        ("FG-DOG-PUP-5", "Premium Dog Puppy 5kg", "Dog Food", "Unit"),
        ("FG-CAT-ADL-5", "Premium Cat Adult 5kg", "Cat Food", "Unit"),
        ("FG-CAT-KIT-2", "Premium Cat Kitten 2kg", "Cat Food", "Unit"),
    ]
    for code, name, group, uom in raw_materials + finished_goods:
        api("POST", "Item", {
            "item_code": code,
            "item_name": name,
            "item_group": group,
            "stock_uom": uom,
            "has_batch_no": 1,
            "has_expiry_date": 1,
            "create_new_batch": 1,
        })
        print(f"  Item: {code} - {name}")


def setup_sample_bom():
    print("[6/7] Creating sample BOM (Premium Dog Adult)...")
    api("POST", "BOM", {
        "item": "FG-DOG-ADL-10",
        "quantity": 1000,
        "uom": "Kg",
        "company": "PetFactory Maroc SARL",
        "items": [
            {"item_code": "RM-CORN", "qty": 300, "uom": "Kg"},
            {"item_code": "RM-WHEAT", "qty": 150, "uom": "Kg"},
            {"item_code": "RM-CHKN", "qty": 250, "uom": "Kg"},
            {"item_code": "RM-SOYA", "qty": 100, "uom": "Kg"},
            {"item_code": "RM-CHKF", "qty": 80, "uom": "Kg"},
            {"item_code": "RM-RICE", "qty": 50, "uom": "Kg"},
            {"item_code": "RM-VITM", "qty": 25, "uom": "Kg"},
            {"item_code": "RM-MINM", "qty": 25, "uom": "Kg"},
            {"item_code": "RM-SALT", "qty": 5, "uom": "Kg"},
        ],
        "with_operations": 1,
        "operations": [
            {"operation": "Reception", "workstation": "WS-RECV: Reception & Storage", "time_in_mins": 30},
            {"operation": "Grinding", "workstation": "WS-GRIND: Grinding", "time_in_mins": 60},
            {"operation": "Mixing", "workstation": "WS-MIX: Mixing", "time_in_mins": 20},
            {"operation": "Extrusion", "workstation": "WS-EXTR: Preconditioning & Extrusion", "time_in_mins": 60},
            {"operation": "Drying", "workstation": "WS-DRY: Drying", "time_in_mins": 45},
            {"operation": "Cooling", "workstation": "WS-COOL: Cooling", "time_in_mins": 30},
            {"operation": "Coating", "workstation": "WS-COAT: Coating", "time_in_mins": 15},
            {"operation": "Packaging", "workstation": "WS-PACK: Packaging", "time_in_mins": 30},
        ],
    })
    print("  BOM: Premium Dog Adult (1000 kg batch)")


def setup_quality_templates():
    print("[7/7] Creating quality inspection templates...")
    templates = [
        {
            "name": "Raw Material Incoming",
            "item_group": "Raw Materials",
            "readings": [
                {"specification": "Moisture Content", "min_value": 0, "max_value": 14, "formula": "%"},
                {"specification": "Protein Content", "min_value": 0, "max_value": 100, "formula": "%"},
                {"specification": "Aflatoxin (B1)", "min_value": 0, "max_value": 20, "formula": "ppb"},
                {"specification": "Visual Inspection", "min_value": 0, "max_value": 1, "formula": "Pass/Fail"},
                {"specification": "Foreign Matter", "min_value": 0, "max_value": 0.5, "formula": "%"},
            ]
        },
        {
            "name": "Post-Extrusion Check",
            "readings": [
                {"specification": "Moisture Content", "min_value": 20, "max_value": 28, "formula": "%"},
                {"specification": "Barrel Temperature", "min_value": 80, "max_value": 150, "formula": "°C"},
                {"specification": "Kibble Density", "min_value": 300, "max_value": 500, "formula": "g/L"},
                {"specification": "Gelatinization", "min_value": 80, "max_value": 100, "formula": "%"},
            ]
        },
        {
            "name": "Finished Goods Release",
            "readings": [
                {"specification": "Moisture Content", "min_value": 0, "max_value": 10, "formula": "%"},
                {"specification": "Water Activity (Aw)", "min_value": 0, "max_value": 0.65, "formula": "Aw"},
                {"specification": "Crude Protein", "min_value": 22, "max_value": 100, "formula": "%"},
                {"specification": "Crude Fat", "min_value": 8, "max_value": 100, "formula": "%"},
                {"specification": "Package Weight", "min_value": 9.9, "max_value": 10.2, "formula": "kg"},
                {"specification": "Seal Integrity", "min_value": 0, "max_value": 1, "formula": "Pass/Fail"},
                {"specification": "Metal Detection", "min_value": 0, "max_value": 1, "formula": "Pass/Fail"},
            ]
        },
    ]
    for tmpl in templates:
        api("POST", "Quality Inspection Template", {
            "quality_inspection_template_name": tmpl["name"],
            "item_group": tmpl.get("item_group", ""),
            "readings": tmpl["readings"],
        })
        print(f"  Template: {tmpl['name']} ({len(tmpl['readings'])} checks)")


if __name__ == "__main__":
    wait_for_erpnext()
    setup_company()
    setup_warehouses()
    setup_item_groups()
    setup_workstations()
    setup_sample_items()
    setup_sample_bom()
    setup_quality_templates()
    print("\nSetup complete! Open http://localhost:8080")
    print("Login: Administrator / admin")
    print("\nNext steps:")
    print("  1. Change admin password")
    print("  2. Set language to French in Settings > User")
    print("  3. Import remaining recipes and items")
    print("  4. Configure ONSSA custom doctypes (see erp/custom_doctypes/)")
