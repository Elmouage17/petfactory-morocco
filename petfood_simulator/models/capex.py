"""
CapEx budget tracking for PetFactory Maroc.

Tracks the total capital budget, vendor quotes, committed and forecasted
spending per system, and expected subsidies within a 12-month horizon.
All amounts are in MAD (Moroccan Dirham).
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date, timedelta
from enum import Enum
from typing import Dict, List, Optional


class QuoteStatus(Enum):
    RECEIVED = "received"
    UNDER_REVIEW = "under_review"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    EXPIRED = "expired"


class SpendingStatus(Enum):
    FORECASTED = "forecasted"
    COMMITTED = "committed"
    PAID = "paid"


class SubsidyStatus(Enum):
    APPLIED = "applied"
    APPROVED = "approved"
    RECEIVED = "received"
    REJECTED = "rejected"


# ── Vendor Quotes ───────────────────────────────────────────────────────────


@dataclass
class VendorQuote:
    vendor: str
    system: str
    description: str
    amount_mad: float
    currency_original: str = "MAD"
    amount_original: float = 0.0
    exchange_rate: float = 1.0
    quote_date: date = field(default_factory=date.today)
    valid_until: Optional[date] = None
    status: QuoteStatus = QuoteStatus.RECEIVED
    notes: str = ""

    @property
    def is_expired(self) -> bool:
        if self.valid_until is None:
            return False
        return date.today() > self.valid_until

    def to_dict(self) -> dict:
        return {
            "vendor": self.vendor,
            "system": self.system,
            "description": self.description,
            "amount_mad": self.amount_mad,
            "currency_original": self.currency_original,
            "amount_original": self.amount_original,
            "exchange_rate": self.exchange_rate,
            "quote_date": self.quote_date.isoformat(),
            "valid_until": self.valid_until.isoformat() if self.valid_until else None,
            "status": self.status.value,
            "notes": self.notes,
        }


# ── Budget Line Items (spending) ────────────────────────────────────────────


@dataclass
class BudgetLineItem:
    system: str
    description: str
    amount_mad: float
    status: SpendingStatus = SpendingStatus.FORECASTED
    expected_date: Optional[date] = None
    paid_date: Optional[date] = None
    vendor: str = ""
    po_number: str = ""
    notes: str = ""

    def to_dict(self) -> dict:
        return {
            "system": self.system,
            "description": self.description,
            "amount_mad": self.amount_mad,
            "status": self.status.value,
            "expected_date": self.expected_date.isoformat() if self.expected_date else None,
            "paid_date": self.paid_date.isoformat() if self.paid_date else None,
            "vendor": self.vendor,
            "po_number": self.po_number,
            "notes": self.notes,
        }


# ── Subsidies ────────────────────────────────────────────────────────────────


@dataclass
class Subsidy:
    name: str
    provider: str
    amount_mad: float
    status: SubsidyStatus = SubsidyStatus.APPLIED
    application_date: Optional[date] = None
    expected_receipt_date: Optional[date] = None
    received_date: Optional[date] = None
    conditions: str = ""
    notes: str = ""

    @property
    def is_within_12_months(self) -> bool:
        if self.expected_receipt_date is None:
            return False
        horizon = date.today() + timedelta(days=365)
        return self.expected_receipt_date <= horizon

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "provider": self.provider,
            "amount_mad": self.amount_mad,
            "status": self.status.value,
            "application_date": self.application_date.isoformat() if self.application_date else None,
            "expected_receipt_date": self.expected_receipt_date.isoformat() if self.expected_receipt_date else None,
            "received_date": self.received_date.isoformat() if self.received_date else None,
            "conditions": self.conditions,
            "notes": self.notes,
        }


# ── Main CapEx Budget Model ─────────────────────────────────────────────────


SYSTEMS = [
    "Boiler System",
    "Air Compressor System",
    "Water System",
    "Weighbridge",
    "Big Storage Oil Tank",
    "Elevator",
    "Electrical Installation & Transformer",
    "Aménagement Extérieur",
    "Solaire Électricité",
    "Installation GAZ",
    "Séparation et Froid Industriel",
    "Séparation Salle de Commande & MCC",
    "Recrutement",
    "Logiciel",
]


@dataclass
class CapexBudget:
    total_budget_mad: float = 0.0
    contingency_pct: float = 10.0
    quotes: List[VendorQuote] = field(default_factory=list)
    line_items: List[BudgetLineItem] = field(default_factory=list)
    subsidies: List[Subsidy] = field(default_factory=list)

    # ── Quote management ─────────────────────────────────────────────────

    def add_quote(self, quote: VendorQuote) -> None:
        self.quotes.append(quote)

    def quotes_for_system(self, system: str) -> List[VendorQuote]:
        return [q for q in self.quotes if q.system == system]

    def accepted_quotes(self) -> List[VendorQuote]:
        return [q for q in self.quotes if q.status == QuoteStatus.ACCEPTED]

    def best_quote_for_system(self, system: str) -> Optional[VendorQuote]:
        active = [
            q for q in self.quotes_for_system(system)
            if q.status in (QuoteStatus.RECEIVED, QuoteStatus.UNDER_REVIEW)
            and not q.is_expired
        ]
        if not active:
            return None
        return min(active, key=lambda q: q.amount_mad)

    # ── Spending management ──────────────────────────────────────────────

    def add_line_item(self, item: BudgetLineItem) -> None:
        self.line_items.append(item)

    def items_for_system(self, system: str) -> List[BudgetLineItem]:
        return [li for li in self.line_items if li.system == system]

    # ── Subsidy management ───────────────────────────────────────────────

    def add_subsidy(self, subsidy: Subsidy) -> None:
        self.subsidies.append(subsidy)

    def subsidies_within_horizon(self) -> List[Subsidy]:
        return [
            s for s in self.subsidies
            if s.is_within_12_months
            and s.status in (SubsidyStatus.APPLIED, SubsidyStatus.APPROVED)
        ]

    # ── Aggregated metrics ───────────────────────────────────────────────

    @property
    def contingency_mad(self) -> float:
        return self.total_budget_mad * (self.contingency_pct / 100.0)

    @property
    def usable_budget_mad(self) -> float:
        return self.total_budget_mad - self.contingency_mad

    @property
    def total_paid(self) -> float:
        return sum(
            li.amount_mad for li in self.line_items
            if li.status == SpendingStatus.PAID
        )

    @property
    def total_committed(self) -> float:
        return sum(
            li.amount_mad for li in self.line_items
            if li.status == SpendingStatus.COMMITTED
        )

    @property
    def total_forecasted(self) -> float:
        return sum(
            li.amount_mad for li in self.line_items
            if li.status == SpendingStatus.FORECASTED
        )

    @property
    def total_spent_and_committed(self) -> float:
        return self.total_paid + self.total_committed

    @property
    def total_future_spending(self) -> float:
        return self.total_committed + self.total_forecasted

    @property
    def total_subsidies_expected(self) -> float:
        return sum(s.amount_mad for s in self.subsidies_within_horizon())

    @property
    def total_subsidies_received(self) -> float:
        return sum(
            s.amount_mad for s in self.subsidies
            if s.status == SubsidyStatus.RECEIVED
        )

    @property
    def remaining_budget(self) -> float:
        return (
            self.usable_budget_mad
            - self.total_spent_and_committed
            + self.total_subsidies_received
        )

    @property
    def remaining_budget_with_expected_subsidies(self) -> float:
        return self.remaining_budget + self.total_subsidies_expected

    @property
    def budget_utilization_pct(self) -> float:
        if self.usable_budget_mad == 0:
            return 0.0
        return (self.total_spent_and_committed / self.usable_budget_mad) * 100.0

    # ── Per-system breakdown ─────────────────────────────────────────────

    def system_summary(self, system: str) -> Dict[str, float]:
        items = self.items_for_system(system)
        return {
            "paid": sum(li.amount_mad for li in items if li.status == SpendingStatus.PAID),
            "committed": sum(li.amount_mad for li in items if li.status == SpendingStatus.COMMITTED),
            "forecasted": sum(li.amount_mad for li in items if li.status == SpendingStatus.FORECASTED),
            "total": sum(li.amount_mad for li in items),
            "quotes_received": len(self.quotes_for_system(system)),
        }

    def all_systems_summary(self) -> Dict[str, Dict[str, float]]:
        systems = {li.system for li in self.line_items}
        systems.update(q.system for q in self.quotes)
        return {s: self.system_summary(s) for s in sorted(systems)}

    # ── Monthly cashflow forecast ────────────────────────────────────────

    def monthly_forecast(self, months_ahead: int = 12) -> List[Dict]:
        today = date.today()
        forecast = []
        for m in range(months_ahead):
            month_start = date(
                today.year + (today.month + m - 1) // 12,
                (today.month + m - 1) % 12 + 1,
                1,
            )
            if m + 1 < months_ahead:
                month_end = date(
                    today.year + (today.month + m) // 12,
                    (today.month + m) % 12 + 1,
                    1,
                ) - timedelta(days=1)
            else:
                month_end = date(
                    today.year + (today.month + m) // 12,
                    (today.month + m) % 12 + 1,
                    1,
                ) - timedelta(days=1)

            outflows = sum(
                li.amount_mad for li in self.line_items
                if li.expected_date and month_start <= li.expected_date <= month_end
                and li.status in (SpendingStatus.COMMITTED, SpendingStatus.FORECASTED)
            )
            inflows = sum(
                s.amount_mad for s in self.subsidies
                if s.expected_receipt_date
                and month_start <= s.expected_receipt_date <= month_end
                and s.status in (SubsidyStatus.APPLIED, SubsidyStatus.APPROVED)
            )
            forecast.append({
                "month": month_start.strftime("%Y-%m"),
                "outflows_mad": round(outflows, 2),
                "subsidy_inflows_mad": round(inflows, 2),
                "net_mad": round(inflows - outflows, 2),
            })
        return forecast

    # ── Full dashboard snapshot ──────────────────────────────────────────

    def snapshot(self) -> Dict:
        return {
            "total_budget_mad": self.total_budget_mad,
            "contingency_pct": self.contingency_pct,
            "contingency_mad": round(self.contingency_mad, 2),
            "usable_budget_mad": round(self.usable_budget_mad, 2),
            "total_paid": round(self.total_paid, 2),
            "total_committed": round(self.total_committed, 2),
            "total_forecasted": round(self.total_forecasted, 2),
            "total_spent_and_committed": round(self.total_spent_and_committed, 2),
            "remaining_budget": round(self.remaining_budget, 2),
            "subsidies_received": round(self.total_subsidies_received, 2),
            "subsidies_expected_12m": round(self.total_subsidies_expected, 2),
            "remaining_with_subsidies": round(self.remaining_budget_with_expected_subsidies, 2),
            "budget_utilization_pct": round(self.budget_utilization_pct, 2),
            "systems": self.all_systems_summary(),
            "monthly_forecast": self.monthly_forecast(),
        }

    # ── Persistence ──────────────────────────────────────────────────────

    def save(self, path: str) -> None:
        data = {
            "total_budget_mad": self.total_budget_mad,
            "contingency_pct": self.contingency_pct,
            "quotes": [q.to_dict() for q in self.quotes],
            "line_items": [li.to_dict() for li in self.line_items],
            "subsidies": [s.to_dict() for s in self.subsidies],
        }
        with open(path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @classmethod
    def load(cls, path: str) -> "CapexBudget":
        with open(path) as f:
            data = json.load(f)

        budget = cls(
            total_budget_mad=data["total_budget_mad"],
            contingency_pct=data.get("contingency_pct", 10.0),
        )

        for q in data.get("quotes", []):
            budget.quotes.append(VendorQuote(
                vendor=q["vendor"],
                system=q["system"],
                description=q["description"],
                amount_mad=q["amount_mad"],
                currency_original=q.get("currency_original", "MAD"),
                amount_original=q.get("amount_original", 0.0),
                exchange_rate=q.get("exchange_rate", 1.0),
                quote_date=date.fromisoformat(q["quote_date"]),
                valid_until=date.fromisoformat(q["valid_until"]) if q.get("valid_until") else None,
                status=QuoteStatus(q["status"]),
                notes=q.get("notes", ""),
            ))

        for li in data.get("line_items", []):
            budget.line_items.append(BudgetLineItem(
                system=li["system"],
                description=li["description"],
                amount_mad=li["amount_mad"],
                status=SpendingStatus(li["status"]),
                expected_date=date.fromisoformat(li["expected_date"]) if li.get("expected_date") else None,
                paid_date=date.fromisoformat(li["paid_date"]) if li.get("paid_date") else None,
                vendor=li.get("vendor", ""),
                po_number=li.get("po_number", ""),
                notes=li.get("notes", ""),
            ))

        for s in data.get("subsidies", []):
            budget.subsidies.append(Subsidy(
                name=s["name"],
                provider=s["provider"],
                amount_mad=s["amount_mad"],
                status=SubsidyStatus(s["status"]),
                application_date=date.fromisoformat(s["application_date"]) if s.get("application_date") else None,
                expected_receipt_date=date.fromisoformat(s["expected_receipt_date"]) if s.get("expected_receipt_date") else None,
                received_date=date.fromisoformat(s["received_date"]) if s.get("received_date") else None,
                conditions=s.get("conditions", ""),
                notes=s.get("notes", ""),
            ))

        return budget
