# ERPNext Implementation Plan — PetFactory Morocco

**Factory:** Famsun 5 TPH Pet Food Production Line, Benguerir, Morocco
**ERP System:** ERPNext (open source, self-hosted)
**Target Go-Live:** Q2 2027

---

## Why ERPNext

| Criterion | ERPNext | Odoo Community | Odoo Enterprise |
|---|---|---|---|
| MRP / Production Planning | Included free | Not available | Paid license |
| Batch Traceability | Built-in | Limited | Paid module |
| Quality Inspection | Included | Not available | Paid module |
| License Cost | $0 | $0 (but missing manufacturing) | $24-44/user/month |
| French + Arabic UI | Community translations | Same | Same |
| Self-hosted | Yes | Yes | Yes |
| Python-based (matches our stack) | Yes (Frappe/Python) | Yes (Python) | Yes |

ERPNext is 100% free for all manufacturing modules, Python-based (aligns with
our existing digital twin codebase), and supports the batch traceability
required by ONSSA.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    PetFactory Morocco                     │
│                                                          │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐ │
│  │  ERPNext      │   │ Digital Twin │   │  Dashboard   │ │
│  │  (Frappe)     │◄──┤ Simulator    │   │  (Streamlit) │ │
│  │              │   │  (Python)    ├──►│              │ │
│  └──────┬───────┘   └──────────────┘   └──────────────┘ │
│         │                                                │
│  ┌──────┴───────────────────────────────────────────┐   │
│  │              MariaDB / PostgreSQL                  │   │
│  └──────────────────────────────────────────────────┘   │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │  ONSSA Compliance Layer (Custom Doctypes)         │   │
│  │  - Batch genealogy    - HACCP checklists          │   │
│  │  - Ingredient tracing - Recall management         │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## Implementation Phases

### Phase 1: Core Setup (Weeks 1-4)

- [ ] Deploy ERPNext on Ubuntu 22.04 server (bench install)
- [ ] Configure Company: PetFactory Maroc SARL
- [ ] Set up Chart of Accounts (Moroccan PCGE)
- [ ] Configure currencies (MAD primary, EUR/USD for imports)
- [ ] Enable French + Arabic translations
- [ ] Set up Fiscal Year and tax rules (TVA 20%)
- [ ] Create Users and Roles (Production, QC, Warehouse, Finance, Admin)

### Phase 2: Inventory & Warehouse (Weeks 3-6)

- [ ] Define Warehouses (Raw Materials, WIP, Finished Goods, Quarantine)
- [ ] Set up Item Groups:
  - Raw Materials: Grains, Proteins, Meals, Fats/Oils, Vitamins/Minerals, Additives
  - Packaging: Bags (5kg, 10kg, 20kg), Labels, Pallets
  - Finished Goods: Dog Food SKUs, Cat Food SKUs
- [ ] Configure batch numbering (auto with date prefix: PF-YYMMDD-XXXX)
- [ ] Enable expiry date tracking on all batches
- [ ] Set reorder levels based on 5 TPH consumption rates
- [ ] Configure bin/silo mapping (14 surge bins + 200T steel silo)

### Phase 3: Manufacturing / MRP (Weeks 5-10)

- [ ] Create Bills of Material for each SKU (recipe formulations)
- [ ] Map the 8-stage production process as Operations:
  1. Raw Material Reception & Storage
  2. Grinding (Hammermill 200kW)
  3. Mixing
  4. Preconditioning & Extrusion
  5. Drying
  6. Cooling
  7. Coating / Enrobing
  8. Packaging
- [ ] Create Workstations matching physical equipment
- [ ] Define routing with standard cycle times
- [ ] Configure Work Order flow with batch tracking at each stage
- [ ] Set up MRP to auto-generate Work Orders + Purchase Orders
- [ ] Link production parameters to digital twin simulator outputs

### Phase 4: Quality Control (Weeks 8-12)

- [ ] Create Quality Inspection templates:
  - **Incoming Raw Materials:** Moisture %, protein %, aflatoxin test, visual inspection
  - **In-Process (Extrusion):** Moisture %, temperature, kibble density, gelatinization
  - **Post-Dryer:** Moisture ≤10%, water activity (Aw)
  - **Finished Goods:** AAFCO nutritional compliance, packaging integrity, weight check
- [ ] Configure inspection triggers (auto on Stock Entry)
- [ ] Build HACCP checklist as custom doctype
- [ ] Set up non-conformance workflow (Quarantine → Rework/Dispose)

### Phase 5: ONSSA Compliance Module (Weeks 10-14)

- [ ] Custom Doctype: **ONSSA Traceability Record**
  - Links batch → raw material lots → supplier certificates
  - Full forward/backward trace in one click
- [ ] Custom Doctype: **ONSSA Inspection Report**
  - Auto-populates from Quality Inspection data
  - Generates PDF in French for submission
- [ ] Custom Doctype: **HACCP Control Point**
  - CCP monitoring logs with corrective action tracking
  - Linked to production Work Orders
- [ ] Custom Report: **Recall Simulation**
  - Input: any batch number or ingredient lot
  - Output: all affected finished goods, customers, dates
- [ ] Custom Report: **Supplier Certificate Tracker**
  - Tracks validity of veterinary certificates, ONSSA approvals

### Phase 6: Purchasing & Sales (Weeks 12-16)

- [ ] Set up Suppliers (grain, protein meal, packaging vendors)
- [ ] Configure Purchase Order workflow with approval
- [ ] Set up landed cost calculation (import duties, freight to Benguerir)
- [ ] Create Customer groups (Distributors, Retailers, Export)
- [ ] Configure Sales Order → Delivery Note → Invoice flow
- [ ] Set up price lists (MAD domestic, EUR export)

### Phase 7: Integration & Go-Live (Weeks 14-18)

- [ ] API integration: Digital Twin → ERPNext
  - Push production parameters (temperatures, moisture, throughput) to Work Orders
  - Pull BOM/recipe data into simulator
- [ ] Barcode setup for warehouse operations
- [ ] User training (French-language materials)
- [ ] Parallel run: manual + ERPNext for 2-4 weeks
- [ ] Data migration from spreadsheets (PetFactoryMaroc_ProjectTracker.xlsx)
- [ ] Go-live

---

## Custom Doctypes for Pet Food Manufacturing

### 1. Recipe Formulation

```
Recipe Formulation
├── recipe_name         (Data)
├── sku_link            (Link → Item)
├── target_weight_kg    (Float)
├── ingredients         (Table → Recipe Ingredient)
│   ├── item            (Link → Item)
│   ├── percentage      (Percent)
│   ├── weight_kg       (Float, auto-calculated)
│   ├── min_pct         (Percent)
│   └── max_pct         (Percent)
├── nutritional_targets (Table → Nutritional Target)
│   ├── nutrient        (crude_protein, crude_fat, crude_fiber, moisture, ash)
│   ├── target_pct      (Percent)
│   ├── min_pct         (Percent)
│   └── max_pct         (Percent)
├── aafco_profile       (Select: Growth, Maintenance, All Life Stages)
├── species             (Select: Dog, Cat)
└── status              (Select: Draft, Active, Superseded)
```

### 2. Production Batch Record

```
Production Batch Record
├── batch_id            (auto: PF-YYMMDD-XXXX)
├── work_order          (Link → Work Order)
├── recipe              (Link → Recipe Formulation)
├── production_date     (Date)
├── shift               (Select: Morning, Afternoon, Night)
├── line_operator       (Link → Employee)
├── stage_logs          (Table → Stage Log)
│   ├── stage           (Select: 1-Reception through 8-Packaging)
│   ├── start_time      (Datetime)
│   ├── end_time        (Datetime)
│   ├── temperature_c   (Float)
│   ├── moisture_pct    (Float)
│   ├── operator_notes  (Small Text)
│   └── passed_qc       (Check)
├── ingredient_lots     (Table → Ingredient Lot Used)
│   ├── item            (Link → Item)
│   ├── batch_no        (Link → Batch)
│   ├── qty_used_kg     (Float)
│   └── supplier        (Link → Supplier)
├── yield_kg            (Float)
├── waste_kg            (Float)
├── qc_result           (Select: Pass, Fail, Conditional)
└── onssa_traceable     (Check, default: 1)
```

### 3. HACCP Control Point Log

```
HACCP Control Point Log
├── ccp_id              (Data: CCP-01 through CCP-XX)
├── ccp_name            (Data: e.g., "Extrusion Temperature")
├── work_order          (Link → Work Order)
├── batch               (Link → Production Batch Record)
├── critical_limit      (Data: e.g., "≥85°C for ≥15 sec")
├── measured_value      (Float)
├── unit                (Data: °C, %, seconds)
├── monitoring_time     (Datetime)
├── within_limits       (Check)
├── corrective_action   (Small Text, mandatory if not within limits)
├── verified_by         (Link → Employee)
└── verification_time   (Datetime)
```

---

## Server Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Ubuntu 22.04 LTS | Ubuntu 22.04 LTS |
| CPU | 4 cores | 8 cores |
| RAM | 8 GB | 16 GB |
| Storage | 100 GB SSD | 256 GB SSD |
| Database | MariaDB 10.6 | MariaDB 10.11 |
| Python | 3.10+ | 3.11 |
| Reverse Proxy | Nginx | Nginx |

Estimated hosting cost (Moroccan VPS or on-premise): **$30-80/month**

---

## Digital Twin Integration

The existing petfood_simulator can feed real-time production data into ERPNext
via the Frappe REST API:

```python
import requests

ERPNEXT_URL = "https://erp.petfactory.ma"
API_KEY = "your-api-key"
API_SECRET = "your-api-secret"

def push_production_data(batch_id: str, stage: str, data: dict):
    """Push simulator output to ERPNext Production Batch Record."""
    response = requests.post(
        f"{ERPNEXT_URL}/api/resource/Production Batch Record/{batch_id}",
        headers={
            "Authorization": f"token {API_KEY}:{API_SECRET}",
            "Content-Type": "application/json",
        },
        json={
            "stage_logs": [{
                "stage": stage,
                "temperature_c": data.get("temperature"),
                "moisture_pct": data.get("moisture"),
                "start_time": data.get("timestamp"),
            }]
        },
    )
    return response.json()
```

---

## Cost Summary

| Item | One-time | Monthly |
|---|---|---|
| ERPNext license | $0 | $0 |
| Server hosting | — | $50 |
| Implementation consultant (optional) | $5,000-15,000 | — |
| Barcode hardware (scanners + printer) | $1,500 | — |
| User training | $2,000 | — |
| **Total** | **$8,500-18,500** | **$50** |

Compare to Odoo Enterprise: $0 one-time + $240-880/month (10-20 users)
over 3 years = **$8,640-31,680 in licensing alone**.

---

## Next Steps

1. Provision a test server and install ERPNext
2. Configure base company data and chart of accounts
3. Enter BOMs for top 3 SKUs
4. Build the ONSSA traceability custom doctype
5. Test end-to-end: Purchase → Production → QC → Delivery
