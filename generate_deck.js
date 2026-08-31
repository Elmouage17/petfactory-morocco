const pptxgen = require("pptxgenjs");
const pres = new pptxgen();

// ─── Layout & Metadata ───────────────────────────────────────────
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.author = "PetFactory Maroc";
pres.subject = "Infrastructure Progress - Investor Update";
pres.title = "PetFactory Morocco - Infrastructure Progress";

// ─── Palette ─────────────────────────────────────────────────────
const C = {
  navy:      "1B2A4A",
  teal:      "2E86AB",
  amber:     "E8963E",
  offWhite:  "F5F5F5",
  white:     "FFFFFF",
  text:      "2D2D2D",
  lightText: "6B7B8D",
  green:     "27AE60",
  orange:    "E67E22",
  red:       "C0392B",
  lightTeal: "D6EFF8",
  lightNavy: "E8EBF0",
  darkTeal:  "1A6B8A",
};

// ─── Helpers ─────────────────────────────────────────────────────
function addSlideNumber(slide, dark) {
  slide.addText("PetFactory Maroc  |  Investor Update  |  August 2026", {
    x: 0.5, y: 7.0, w: 12.33, h: 0.3,
    fontSize: 8, color: dark ? "8899AA" : C.lightText,
    fontFace: "Arial", align: "left", isTextBox: true, margin: 0,
  });
}

function darkSlide() {
  const slide = pres.addSlide();
  slide.background = { color: C.navy };
  return slide;
}

function lightSlide() {
  const slide = pres.addSlide();
  slide.background = { color: C.white };
  return slide;
}

function statCard(slide, x, y, w, h, number, label, color) {
  slide.addShape(pres.ShapeType.roundRect, {
    x, y, w, h,
    fill: { color: C.white },
    shadow: { type: "outer", blur: 6, offset: 2, angle: 90, color: "CCCCCC", opacity: 0.4 },
    rectRadius: 0.1,
  });
  slide.addText(number, {
    x, y: y + 0.15, w, h: 0.65,
    fontSize: 36, fontFace: "Calibri", bold: true, color: color || C.teal,
    align: "center", isTextBox: true, margin: 0,
  });
  slide.addText(label, {
    x, y: y + 0.75, w, h: 0.45,
    fontSize: 11, fontFace: "Arial", color: C.lightText,
    align: "center", isTextBox: true, margin: 0,
  });
}

function iconCircle(slide, x, y, size, bgColor) {
  slide.addShape(pres.ShapeType.ellipse, {
    x, y, w: size, h: size,
    fill: { color: bgColor },
  });
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 1 — Title
// ═══════════════════════════════════════════════════════════════════
{
  const slide = darkSlide();

  // Large amber accent block top-right
  slide.addShape(pres.ShapeType.rect, {
    x: 9.0, y: 0, w: 4.33, h: 3.2,
    fill: { color: C.amber }, transparency: 15,
  });

  // Subtle teal block bottom-right
  slide.addShape(pres.ShapeType.rect, {
    x: 10.5, y: 3.2, w: 2.83, h: 4.3,
    fill: { color: C.teal }, transparency: 80,
  });

  slide.addText("PETFACTORY", {
    x: 0.8, y: 1.4, w: 8.0, h: 1.0,
    fontSize: 52, fontFace: "Calibri", bold: true, color: C.white,
    isTextBox: true, margin: 0,
  });
  slide.addText("MOROCCO", {
    x: 0.8, y: 2.2, w: 8.0, h: 0.9,
    fontSize: 44, fontFace: "Calibri", bold: false, color: C.amber,
    isTextBox: true, margin: 0,
  });

  slide.addText("Infrastructure Progress Report", {
    x: 0.8, y: 3.5, w: 8.0, h: 0.5,
    fontSize: 22, fontFace: "Arial", color: C.lightText,
    isTextBox: true, margin: 0,
  });
  slide.addText("Investor Update  |  August 2026", {
    x: 0.8, y: 4.1, w: 8.0, h: 0.4,
    fontSize: 14, fontFace: "Arial", color: "8899AA",
    isTextBox: true, margin: 0,
  });

  // Key facts at bottom
  slide.addText([
    { text: "5 T/H ", options: { bold: true, color: C.amber, fontSize: 13 } },
    { text: "Dry Extrusion Line   |   ", options: { color: "8899AA", fontSize: 11 } },
    { text: "FAMSUN ", options: { bold: true, color: C.amber, fontSize: 13 } },
    { text: "Turnkey   |   ", options: { color: "8899AA", fontSize: 11 } },
    { text: "Sidi Bouathmane, Morocco", options: { color: "8899AA", fontSize: 11 } },
  ], {
    x: 0.8, y: 5.8, w: 10.0, h: 0.4,
    fontFace: "Arial", isTextBox: true, margin: 0,
  });

  slide.addText("Petland Maroc  |  100% Ownership  |  Confidential", {
    x: 0.8, y: 6.5, w: 10.0, h: 0.3,
    fontSize: 9, fontFace: "Arial", color: "667788",
    isTextBox: true, margin: 0,
  });
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 2 — Executive Summary
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Executive Summary", {
    x: 0.7, y: 0.4, w: 6.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  // Description paragraph
  slide.addText(
    "PetFactory Morocco is a greenfield premium pet food manufacturing platform, " +
    "100% owned by Petland Maroc. Engineered turnkey by FAMSUN with a 5 T/h dry " +
    "extrusion line, the facility targets private-label and co-branded production " +
    "for retailers across economy to super-premium tiers. Strategically located at " +
    "Sidi Bouathmane near Casablanca port, with direct access to EU, US, Gulf and African markets.",
    {
      x: 0.7, y: 1.2, w: 7.5, h: 1.2,
      fontSize: 13, fontFace: "Arial", color: C.text, lineSpacingMultiple: 1.35,
      isTextBox: true, margin: 0,
    }
  );

  // Stat cards row
  statCard(slide, 0.7,  2.7, 2.8, 1.3, "5 T/H",     "Extrusion Capacity",     C.teal);
  statCard(slide, 3.8,  2.7, 2.8, 1.3, "14",         "Infrastructure Systems",  C.navy);
  statCard(slide, 6.9,  2.7, 2.8, 1.3, "24.2%",     "Overall Progress",        C.amber);
  statCard(slide, 10.0, 2.7, 2.8, 1.3, "Nov 2026",  "Target Commissioning",    C.green);

  // Key highlights section
  slide.addText("Key Highlights", {
    x: 0.7, y: 4.4, w: 5.0, h: 0.4,
    fontSize: 18, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const highlights = [
    ["JV with Normandie Pet Food (France)", "EU market access, backed by Bpifrance & Credit Agricole"],
    ["US-Morocco Free Trade Agreement",     "Duty-free access, 7-12 day East Coast transit"],
    ["HACCP & ISO 22000 in implementation", "FDA registration planned; full batch traceability"],
    ["Electrical transformer PO signed",    "1,600 KVA — manufacturing starts July 2026"],
  ];

  highlights.forEach((h, i) => {
    const yBase = 5.0 + i * 0.55;
    iconCircle(slide, 0.7, yBase + 0.05, 0.25, C.teal);
    slide.addText(h[0], {
      x: 1.1, y: yBase, w: 4.5, h: 0.3,
      fontSize: 12, fontFace: "Arial", bold: true, color: C.text,
      isTextBox: true, margin: 0,
    });
    slide.addText(h[1], {
      x: 5.7, y: yBase, w: 7.0, h: 0.3,
      fontSize: 11, fontFace: "Arial", color: C.lightText,
      isTextBox: true, margin: 0,
    });
  });

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 3 — Strategic Position & Market Opportunity
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Strategic Position", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  // Left column — Location advantages
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.7, y: 1.3, w: 5.8, h: 5.3,
    fill: { color: C.lightNavy },
    rectRadius: 0.15,
  });

  slide.addText("Location Advantage", {
    x: 1.1, y: 1.5, w: 5.0, h: 0.4,
    fontSize: 18, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const locItems = [
    { title: "Sidi Bouathmane, Morocco", desc: "Near Casablanca deep-water port, direct container services to NY/NJ, Norfolk, Savannah, Montreal" },
    { title: "US-Morocco FTA (since 2006)", desc: "Duty-free on qualifying goods. 7-12 days to US East Coast vs. 30+ days from Asia" },
    { title: "EU Proximity", desc: "JV with Normandie Pet Food targets EUR 300M revenue by 2030. Direct access to EU market" },
    { title: "MAD Currency Stability", desc: "Pegged to EUR/USD basket — reliable for multi-year supply contracts" },
    { title: "Gulf & Africa", desc: "Growing pet ownership markets accessible from Casablanca hub" },
  ];

  locItems.forEach((item, i) => {
    const yBase = 2.15 + i * 0.85;
    iconCircle(slide, 1.1, yBase + 0.05, 0.22, C.amber);
    slide.addText(item.title, {
      x: 1.5, y: yBase, w: 4.8, h: 0.3,
      fontSize: 12, fontFace: "Arial", bold: true, color: C.text,
      isTextBox: true, margin: 0,
    });
    slide.addText(item.desc, {
      x: 1.5, y: yBase + 0.3, w: 4.8, h: 0.4,
      fontSize: 10, fontFace: "Arial", color: C.lightText, lineSpacingMultiple: 1.2,
      isTextBox: true, margin: 0,
    });
  });

  // Right column — Market targets
  slide.addShape(pres.ShapeType.roundRect, {
    x: 6.9, y: 1.3, w: 5.8, h: 5.3,
    fill: { color: C.navy },
    rectRadius: 0.15,
  });

  slide.addText("Target Markets", {
    x: 7.3, y: 1.5, w: 5.0, h: 0.4,
    fontSize: 18, fontFace: "Calibri", bold: true, color: C.white,
    isTextBox: true, margin: 0,
  });

  const markets = [
    { region: "North America",  detail: "2-3 anchor buyer partnerships\nDuty-free FTA access", color: C.amber },
    { region: "European Union", detail: "Normandie Pet Food JV\nBpifrance / Credit Agricole backed", color: C.teal },
    { region: "Gulf States",    detail: "Premium pet food demand\nGrowing middle class", color: C.green },
    { region: "Africa",         detail: "Emerging pet ownership\nRegional proximity", color: "A78BFA" },
  ];

  markets.forEach((m, i) => {
    const yBase = 2.15 + i * 1.05;
    slide.addShape(pres.ShapeType.roundRect, {
      x: 7.3, y: yBase, w: 5.0, h: 0.85,
      fill: { color: "253660" },
      rectRadius: 0.08,
    });
    iconCircle(slide, 7.5, yBase + 0.2, 0.4, m.color);
    slide.addText(m.region, {
      x: 8.1, y: yBase + 0.08, w: 4.0, h: 0.3,
      fontSize: 13, fontFace: "Arial", bold: true, color: C.white,
      isTextBox: true, margin: 0,
    });
    slide.addText(m.detail, {
      x: 8.1, y: yBase + 0.38, w: 4.0, h: 0.4,
      fontSize: 10, fontFace: "Arial", color: "AAB8CC", lineSpacingMultiple: 1.15,
      isTextBox: true, margin: 0,
    });
  });

  // Logistics callout
  slide.addText([
    { text: "Incoterms: ", options: { bold: true, fontSize: 10, color: C.navy } },
    { text: "FOB Casablanca (CIF/DDP available)   |   ", options: { fontSize: 10, color: C.lightText } },
    { text: "MOQ: ", options: { bold: true, fontSize: 10, color: C.navy } },
    { text: "Full container (20-ft / 40-ft per SKU)   |   ", options: { fontSize: 10, color: C.lightText } },
    { text: "Transit: ", options: { bold: true, fontSize: 10, color: C.navy } },
    { text: "10-14 days port-to-port US East Coast", options: { fontSize: 10, color: C.lightText } },
  ], {
    x: 0.7, y: 6.75, w: 12.0, h: 0.3,
    fontFace: "Arial", isTextBox: true, margin: 0,
  });

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 4 — Production Line
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Production Line", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  slide.addText("FAMSUN Turnkey  |  5 T/h Dry Extrusion", {
    x: 0.7, y: 0.95, w: 8.0, h: 0.35,
    fontSize: 14, fontFace: "Arial", color: C.lightText,
    isTextBox: true, margin: 0,
  });

  // Process flow — 7 stages as connected cards
  const stages = [
    { name: "Raw\nMaterials",     spec: "10% moisture\n25°C input",        color: C.navy },
    { name: "Pre-\nconditioner",  spec: "Steam 350 kg/h\nWater 400 kg/h",     color: C.darkTeal },
    { name: "Extruder\nSJPS165",  spec: "203 kW motor\n145°C barrel",     color: C.teal },
    { name: "Dryer\nGZDH2200",    spec: "140°C inlet\n44 m² belt",   color: C.amber },
    { name: "Cooler",             spec: "12 min\nresidence time",              color: "5B9BD5" },
    { name: "Coater",             spec: "12% fat\n2% palatant",                color: "7C68AE" },
    { name: "Packaging",          spec: "20°C room\n45% RH",             color: C.green },
  ];

  const stageW = 1.5;
  const gapW = 0.2;
  const totalW = stages.length * stageW + (stages.length - 1) * gapW;
  const startX = (13.33 - totalW) / 2;
  const stageY = 1.7;

  stages.forEach((s, i) => {
    const sx = startX + i * (stageW + gapW);

    // Card
    slide.addShape(pres.ShapeType.roundRect, {
      x: sx, y: stageY, w: stageW, h: 1.7,
      fill: { color: s.color },
      rectRadius: 0.1,
    });

    // Stage number
    slide.addText(`${i + 1}`, {
      x: sx, y: stageY + 0.1, w: stageW, h: 0.3,
      fontSize: 11, fontFace: "Arial", bold: true, color: C.white,
      align: "center", transparency: 40, isTextBox: true, margin: 0,
    });

    // Stage name
    slide.addText(s.name, {
      x: sx + 0.1, y: stageY + 0.35, w: stageW - 0.2, h: 0.6,
      fontSize: 12, fontFace: "Calibri", bold: true, color: C.white,
      align: "center", isTextBox: true, margin: 0,
    });

    // Spec
    slide.addText(s.spec, {
      x: sx + 0.1, y: stageY + 0.95, w: stageW - 0.2, h: 0.6,
      fontSize: 9, fontFace: "Arial", color: C.white,
      align: "center", transparency: 20, isTextBox: true, margin: 0,
    });

    // Arrow between stages
    if (i < stages.length - 1) {
      slide.addShape(pres.ShapeType.triangle, {
        x: sx + stageW + 0.02, y: stageY + 0.7, w: 0.16, h: 0.2,
        fill: { color: C.lightText }, rotate: 90,
      });
    }
  });

  // Performance specs section
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.7, y: 3.9, w: 6.0, h: 3.0,
    fill: { color: C.lightNavy },
    rectRadius: 0.12,
  });

  slide.addText("Guaranteed Performance", {
    x: 1.1, y: 4.1, w: 5.2, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const perfItems = [
    ["Dog food (8.0 mm kibble)", "≥ 5.0 T/h"],
    ["Cat food (4.0 mm kibble)", "≥ 4.5 T/h"],
    ["Bulk density",             "350-450 g/L"],
    ["Moisture target",          "9.0%"],
    ["Water activity limit",     "≤ 0.60"],
  ];

  perfItems.forEach((p, i) => {
    const py = 4.6 + i * 0.42;
    slide.addText(p[0], {
      x: 1.1, y: py, w: 3.5, h: 0.3,
      fontSize: 11, fontFace: "Arial", color: C.text,
      isTextBox: true, margin: 0,
    });
    slide.addText(p[1], {
      x: 4.6, y: py, w: 1.8, h: 0.3,
      fontSize: 12, fontFace: "Arial", bold: true, color: C.teal, align: "right",
      isTextBox: true, margin: 0,
    });
  });

  // Product range section
  slide.addShape(pres.ShapeType.roundRect, {
    x: 7.1, y: 3.9, w: 5.6, h: 3.0,
    fill: { color: C.lightNavy },
    rectRadius: 0.12,
  });

  slide.addText("Product Range", {
    x: 7.5, y: 4.1, w: 5.0, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const products = [
    "Premium dry kibble (dog & cat)",
    "Custom formulations (shape, density, coating)",
    "Grain-free & single-protein formats",
    "Prescription-style diets",
    "Phase 2: Wet line (pate, chunks-in-gravy, treats)",
  ];

  products.forEach((p, i) => {
    const py = 4.6 + i * 0.42;
    iconCircle(slide, 7.5, py + 0.05, 0.18, i === 4 ? C.amber : C.teal);
    slide.addText(p, {
      x: 7.85, y: py, w: 4.6, h: 0.3,
      fontSize: 11, fontFace: "Arial", color: i === 4 ? C.amber : C.text,
      italic: i === 4,
      isTextBox: true, margin: 0,
    });
  });

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 5 — Infrastructure Systems Overview
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Infrastructure Systems", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  slide.addText("14 Systems Tracked  |  128 Tasks  |  24.2% Overall Progress", {
    x: 0.7, y: 0.95, w: 10.0, h: 0.35,
    fontSize: 14, fontFace: "Arial", color: C.lightText,
    isTextBox: true, margin: 0,
  });

  // Summary stat cards
  statCard(slide, 0.7,  1.5, 2.0, 1.0, "24",  "Tasks Complete",    C.green);
  statCard(slide, 2.9,  1.5, 2.0, 1.0, "14",  "In Progress",       C.amber);
  statCard(slide, 5.1,  1.5, 2.0, 1.0, "90",  "Not Started",       C.lightText);
  statCard(slide, 7.3,  1.5, 2.0, 1.0, "1/7", "Milestones Passed", C.teal);

  // Progress bar
  slide.addShape(pres.ShapeType.roundRect, {
    x: 9.8, y: 1.5, w: 2.9, h: 1.0,
    fill: { color: C.lightNavy },
    rectRadius: 0.1,
  });
  slide.addText("24.2%", {
    x: 9.8, y: 1.52, w: 2.9, h: 0.5,
    fontSize: 24, fontFace: "Calibri", bold: true, color: C.teal, align: "center",
    isTextBox: true, margin: 0,
  });
  // Bar bg
  slide.addShape(pres.ShapeType.roundRect, {
    x: 10.1, y: 2.15, w: 2.3, h: 0.18,
    fill: { color: "D0D8E0" },
    rectRadius: 0.09,
  });
  // Bar fill
  slide.addShape(pres.ShapeType.roundRect, {
    x: 10.1, y: 2.15, w: 2.3 * 0.242, h: 0.18,
    fill: { color: C.teal },
    rectRadius: 0.09,
  });

  // Systems table
  const systems = [
    { name: "Electrical & Transformer", spec: "1,600 KVA",       progress: 33, rag: "GREEN",  note: "PO signed. Mfg starts Jul 1" },
    { name: "Control Room & MCC",       spec: "Separation",       progress: 83, rag: "GREEN",  note: "Specs & drawings approved" },
    { name: "Exterior Concrete Works",  spec: "Béton",       progress: 83, rag: "GREEN",  note: "Vendor finalization in progress" },
    { name: "Industrial Cold",          spec: "Dry separation",   progress: 67, rag: "GREEN",  note: "Spec review complete" },
    { name: "Software",                 spec: "ERP / MES",        progress: 67, rag: "GREEN",  note: "Approval in progress" },
    { name: "Weighbridge",             spec: "60 T",              progress: 25, rag: "ORANGE", note: "Supplier selected, PO pending" },
    { name: "Water System",            spec: "10,000 kg/h",       progress: 21, rag: "ORANGE", note: "Pump/tank selection started" },
    { name: "Gas Installation",        spec: "15 m³",        progress: 21, rag: "ORANGE", note: "Vendor due Jul 21" },
    { name: "Boiler System",           spec: "6,000 kg/h steam",  progress: 18, rag: "ORANGE", note: "Vendor finalization Jul 11" },
    { name: "Compressor",              spec: "37 kW x 2",         progress: 19, rag: "ORANGE", note: "Engineering done, vendor pending" },
    { name: "Elevator",                spec: "2 x 2 T",           progress: 18, rag: "ORANGE", note: "Design validated" },
    { name: "Oil Storage Tank",        spec: "2 x 20,000 L",      progress:  4, rag: "RED",    note: "CRITICAL: +8 weeks delayed" },
    { name: "Solar Electricity",       spec: "480 KVA target",    progress:  0, rag: "GREY",   note: "Not yet initiated" },
  ];

  const tableY = 2.8;
  const rowH = 0.29;

  // Header row
  slide.addShape(pres.ShapeType.rect, {
    x: 0.7, y: tableY, w: 11.93, h: 0.35,
    fill: { color: C.navy },
  });
  const headers = [
    { text: "System", x: 0.75, w: 2.6 },
    { text: "Specification", x: 3.35, w: 1.8 },
    { text: "Progress", x: 5.15, w: 2.8 },
    { text: "Status", x: 7.95, w: 0.8 },
    { text: "Note", x: 8.75, w: 3.85 },
  ];
  headers.forEach(h => {
    slide.addText(h.text, {
      x: h.x, y: tableY, w: h.w, h: 0.35,
      fontSize: 9, fontFace: "Arial", bold: true, color: C.white,
      isTextBox: true, margin: 0, valign: "middle",
    });
  });

  systems.forEach((s, i) => {
    const ry = tableY + 0.37 + i * rowH;
    const bgColor = i % 2 === 0 ? C.offWhite : C.white;

    slide.addShape(pres.ShapeType.rect, {
      x: 0.7, y: ry, w: 11.93, h: rowH,
      fill: { color: bgColor },
    });

    // System name
    slide.addText(s.name, {
      x: 0.75, y: ry, w: 2.6, h: rowH,
      fontSize: 9, fontFace: "Arial", bold: true, color: C.text,
      isTextBox: true, margin: 0, valign: "middle",
    });

    // Spec
    slide.addText(s.spec, {
      x: 3.35, y: ry, w: 1.8, h: rowH,
      fontSize: 9, fontFace: "Arial", color: C.lightText,
      isTextBox: true, margin: 0, valign: "middle",
    });

    // Progress bar
    const barX = 5.15;
    const barW = 2.0;
    slide.addShape(pres.ShapeType.roundRect, {
      x: barX, y: ry + 0.09, w: barW, h: 0.14,
      fill: { color: "D8DEE4" },
      rectRadius: 0.07,
    });
    if (s.progress > 0) {
      const fillColor = s.rag === "RED" ? C.red : s.rag === "ORANGE" ? C.orange : C.green;
      slide.addShape(pres.ShapeType.roundRect, {
        x: barX, y: ry + 0.09, w: Math.max(barW * (s.progress / 100), 0.08), h: 0.14,
        fill: { color: fillColor },
        rectRadius: 0.07,
      });
    }
    slide.addText(`${s.progress}%`, {
      x: 7.2, y: ry, w: 0.6, h: rowH,
      fontSize: 8, fontFace: "Arial", bold: true,
      color: s.rag === "RED" ? C.red : C.text,
      isTextBox: true, margin: 0, valign: "middle",
    });

    // RAG dot
    const ragColor = s.rag === "RED" ? C.red : s.rag === "ORANGE" ? C.orange : s.rag === "GREEN" ? C.green : "AABBCC";
    iconCircle(slide, 8.2, ry + 0.09, 0.14, ragColor);

    // Note
    slide.addText(s.note, {
      x: 8.75, y: ry, w: 3.85, h: rowH,
      fontSize: 8, fontFace: "Arial",
      color: s.rag === "RED" ? C.red : C.lightText,
      bold: s.rag === "RED",
      isTextBox: true, margin: 0, valign: "middle",
    });
  });

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 6 — Key Systems Deep Dive
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Key Systems Deep Dive", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  // Card 1 — Boiler
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.7, y: 1.3, w: 3.85, h: 4.2,
    fill: { color: C.white },
    shadow: { type: "outer", blur: 6, offset: 2, angle: 90, color: "CCCCCC", opacity: 0.35 },
    rectRadius: 0.12,
  });
  iconCircle(slide, 1.0, 1.5, 0.45, C.amber);
  slide.addText("Boiler System", {
    x: 1.6, y: 1.55, w: 2.8, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });
  const boilerSpecs = [
    "2 fire-tube steam boilers (N+1 logic)",
    "Three-pass wet-back design",
    "Peak demand: 2,600 kg/h saturated steam",
    "Unit size: 1,600-2,000 kg/h each",
    "Design: 10 barg / Operating: 7-8 barg",
    "Dual-fuel: LPG primary, NG ready",
    "Efficiency: ≥94% NG / ≥93% LPG",
    "Incl. feedwater, deaerator, softener, RO",
    "Culinary steam train (316L SS, ≤2μm)",
  ];
  boilerSpecs.forEach((spec, i) => {
    slide.addText(spec, {
      x: 1.0, y: 2.15 + i * 0.35, w: 3.3, h: 0.3,
      fontSize: 9, fontFace: "Arial", color: C.text,
      isTextBox: true, margin: 0,
    });
  });

  // Card 2 — Electrical
  slide.addShape(pres.ShapeType.roundRect, {
    x: 4.75, y: 1.3, w: 3.85, h: 4.2,
    fill: { color: C.white },
    shadow: { type: "outer", blur: 6, offset: 2, angle: 90, color: "CCCCCC", opacity: 0.35 },
    rectRadius: 0.12,
  });
  iconCircle(slide, 5.05, 1.5, 0.45, C.green);
  slide.addText("Electrical & Power", {
    x: 5.65, y: 1.55, w: 2.8, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });
  const elecSpecs = [
    "1,600 KVA transformer (PO signed)",
    "Manufacturing starts: July 1, 2026",
    "12-week lead time to delivery",
    "Only system with signed purchase order",
    "",
    "Solar target: 480 KVA (30% of load)",
    "Framework: Moroccan Law 40-19",
    "Incentives: ECOTAQA / TATWIR",
    "Solar vendor: not yet initiated",
  ];
  elecSpecs.forEach((spec, i) => {
    if (spec === "") return;
    slide.addText(spec, {
      x: 5.05, y: 2.15 + i * 0.35, w: 3.3, h: 0.3,
      fontSize: 9, fontFace: "Arial", color: i >= 5 ? C.amber : C.text,
      italic: i >= 5,
      isTextBox: true, margin: 0,
    });
  });

  // Card 3 — Compressed Air & Water
  slide.addShape(pres.ShapeType.roundRect, {
    x: 8.8, y: 1.3, w: 3.85, h: 4.2,
    fill: { color: C.white },
    shadow: { type: "outer", blur: 6, offset: 2, angle: 90, color: "CCCCCC", opacity: 0.35 },
    rectRadius: 0.12,
  });
  iconCircle(slide, 9.1, 1.5, 0.45, C.teal);
  slide.addText("Air & Water", {
    x: 9.7, y: 1.55, w: 2.8, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });
  const airWaterSpecs = [
    "Compressed Air:",
    "  2 x 37 kW compressors",
    "  Total demand: 363 m³/h",
    "  Product line: 258 m³/h",
    "  Engineering complete",
    "",
    "Water System:",
    "  Design capacity: 10,000 kg/h",
    "  Actual flow: 2,760 kg/h",
    "  Pump/tank selection in progress",
  ];
  airWaterSpecs.forEach((spec, i) => {
    if (spec === "") return;
    const isHeader = spec.endsWith(":");
    slide.addText(spec, {
      x: 9.1, y: 2.15 + i * 0.35, w: 3.3, h: 0.3,
      fontSize: 9, fontFace: "Arial", color: C.text,
      bold: isHeader,
      isTextBox: true, margin: 0,
    });
  });

  // Steam distribution callout
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.7, y: 5.75, w: 11.95, h: 1.0,
    fill: { color: C.lightTeal },
    rectRadius: 0.1,
  });
  slide.addText("Steam Distribution Summary", {
    x: 1.1, y: 5.85, w: 3.0, h: 0.3,
    fontSize: 12, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });
  slide.addText(
    "Dryer: 1.40 T/h (DN100)   |   Preconditioner: 0.75 T/h (DN60)   |   Fat Tanks: 0.30 T/h (DN32)   |   " +
    "Total: 2.45 T/h   |   Condensate return: 69.7% (target 80%+ with flash recovery)",
    {
      x: 1.1, y: 6.2, w: 11.2, h: 0.4,
      fontSize: 10, fontFace: "Arial", color: C.text,
      isTextBox: true, margin: 0,
    }
  );

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 7 — Project Timeline
// ═══════════════════════════════════════════════════════════════════
{
  const slide = darkSlide();

  slide.addText("Project Timeline", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.white,
    isTextBox: true, margin: 0,
  });

  slide.addText("Target Commissioning: November 24, 2026", {
    x: 0.7, y: 0.95, w: 8.0, h: 0.35,
    fontSize: 14, fontFace: "Arial", color: C.amber,
    isTextBox: true, margin: 0,
  });

  // Timeline line
  const lineY = 2.0;
  slide.addShape(pres.ShapeType.rect, {
    x: 1.2, y: lineY, w: 10.9, h: 0.04,
    fill: { color: C.teal },
  });

  const milestones = [
    { label: "FAMSUN\nDrawing Review",       date: "May 31",  status: "done",    x: 1.2 },
    { label: "Transformer\nMfg Starts",      date: "Jul 1",   status: "next",    x: 2.8 },
    { label: "Vendor\nFinalization x3",      date: "Jul 11",  status: "next",    x: 4.2 },
    { label: "Equipment\nManufacturing",     date: "Aug 18",  status: "future",  x: 5.8 },
    { label: "Equipment\nShipping",          date: "Sep 18",  status: "future",  x: 7.3 },
    { label: "Site\nDeliveries",             date: "Oct 28",  status: "future",  x: 8.8 },
    { label: "Installation\nComplete",       date: "Nov 8",   status: "future",  x: 10.3 },
    { label: "Commissioned\n& Ready",        date: "Nov 24",  status: "target",  x: 11.8 },
  ];

  milestones.forEach((m) => {
    const dotColor = m.status === "done" ? C.green : m.status === "next" ? C.amber : m.status === "target" ? C.teal : "445566";
    const dotSize = m.status === "target" ? 0.28 : 0.22;
    const dotOffset = (dotSize - 0.04) / 2;

    // Dot on the line
    iconCircle(slide, m.x - dotSize / 2 + 0.15, lineY - dotOffset, dotSize, dotColor);

    // Date above
    slide.addText(m.date, {
      x: m.x - 0.3, y: lineY - 0.55, w: 1.0, h: 0.3,
      fontSize: 10, fontFace: "Arial", bold: true,
      color: m.status === "done" ? C.green : m.status === "target" ? C.teal : "AABBCC",
      align: "center", isTextBox: true, margin: 0,
    });

    // Label below
    slide.addText(m.label, {
      x: m.x - 0.4, y: lineY + 0.35, w: 1.2, h: 0.55,
      fontSize: 9, fontFace: "Arial", color: "AABBCC", align: "center",
      isTextBox: true, margin: 0,
    });

    // Checkmark for done
    if (m.status === "done") {
      slide.addText("✓", {
        x: m.x - 0.1, y: lineY - 0.05, w: 0.5, h: 0.25,
        fontSize: 12, fontFace: "Arial", bold: true, color: C.white,
        align: "center", isTextBox: true, margin: 0,
      });
    }
  });

  // Critical path callout
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.7, y: 3.5, w: 11.95, h: 3.2,
    fill: { color: "1E2F50" },
    rectRadius: 0.12,
  });

  slide.addText("Critical Path Items", {
    x: 1.1, y: 3.7, w: 5.0, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.amber,
    isTextBox: true, margin: 0,
  });

  const critItems = [
    { phase: "NOW",       item: "Civil works start for boiler, compressor, weighbridge, elevator, water trenching", deadline: "OVERDUE (was Jun 18)", color: C.red },
    { phase: "2 WEEKS",   item: "Vendor finalization: Boiler + Compressor + Elevator", deadline: "Jul 11, 2026", color: C.amber },
    { phase: "3 WEEKS",   item: "Gas installation vendor finalization", deadline: "Jul 21, 2026", color: C.amber },
    { phase: "6 WEEKS",   item: "Equipment manufacturing complete (boiler, elevator)", deadline: "Aug 18, 2026", color: "AABBCC" },
    { phase: "10 WEEKS",  item: "Major equipment shipping complete", deadline: "Sep 18, 2026", color: "AABBCC" },
    { phase: "12 WEEKS",  item: "Boiler delivery on site (hard constraint from RFP)", deadline: "Oct 19, 2026", color: "AABBCC" },
  ];

  critItems.forEach((c, i) => {
    const cy = 4.25 + i * 0.42;

    slide.addShape(pres.ShapeType.roundRect, {
      x: 1.1, y: cy + 0.02, w: 0.9, h: 0.28,
      fill: { color: c.color },
      rectRadius: 0.05,
    });
    slide.addText(c.phase, {
      x: 1.1, y: cy, w: 0.9, h: 0.32,
      fontSize: 8, fontFace: "Arial", bold: true, color: C.white,
      align: "center", isTextBox: true, margin: 0, valign: "middle",
    });

    slide.addText(c.item, {
      x: 2.2, y: cy, w: 6.0, h: 0.32,
      fontSize: 10, fontFace: "Arial", color: C.white,
      isTextBox: true, margin: 0, valign: "middle",
    });

    slide.addText(c.deadline, {
      x: 8.5, y: cy, w: 3.8, h: 0.32,
      fontSize: 10, fontFace: "Arial", bold: true,
      color: c.color === C.red ? C.red : c.color,
      align: "right",
      isTextBox: true, margin: 0, valign: "middle",
    });
  });

  addSlideNumber(slide, true);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 8 — Risks & Mitigation
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Risks & Mitigation", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const risks = [
    {
      title: "Oil Storage Tank Delay",
      severity: "HIGH",
      sevColor: C.red,
      description: "Annex D spec review blocked since April 21 (+8 weeks). Only RED system. Vendor not selected, PO not issued, foundation not started, oversized transport permit not initiated.",
      mitigation: "Immediate unblocking of spec review. Parallel-track vendor selection and permit application. Escalate to project leadership.",
    },
    {
      title: "Civil Works Not Started",
      severity: "HIGH",
      sevColor: C.red,
      description: "5 foundation packages were due June 18 and are all unstarted (boiler, compressor, weighbridge, elevator shaft, water trenching).",
      mitigation: "Fast-track contractor mobilization. Prioritize boiler and compressor foundations on critical path. Weekly progress tracking.",
    },
    {
      title: "Vendor Deadline Compression",
      severity: "MEDIUM",
      sevColor: C.orange,
      description: "Boiler, compressor, and elevator vendors must be finalized by July 11. Manufacturing must start July 18 to meet September shipping window.",
      mitigation: "Daily follow-up with shortlisted vendors. Pre-negotiate LOI terms. Prepare backup vendor options.",
    },
    {
      title: "FAMSUN Silo Visibility",
      severity: "MEDIUM",
      sevColor: C.orange,
      description: "Silo scope entirely dependent on FAMSUN Chinese team. No independent tracking. Last update: April 2026.",
      mitigation: "Request formal status update and delivery schedule from FAMSUN. Establish bi-weekly check-ins. Define acceptance criteria.",
    },
    {
      title: "Solar Generation (0% Progress)",
      severity: "LOW",
      sevColor: C.lightText,
      description: "No tasks started for 480 KVA solar target. Not yet on critical path but represents cost savings and ESG positioning.",
      mitigation: "Initiate vendor RFP in Q4 2026. Leverage Moroccan Law 40-19 incentives. Can be commissioned post-startup.",
    },
  ];

  risks.forEach((r, i) => {
    const ry = 1.3 + i * 1.18;

    // Card
    slide.addShape(pres.ShapeType.roundRect, {
      x: 0.7, y: ry, w: 11.95, h: 1.0,
      fill: { color: C.white },
      shadow: { type: "outer", blur: 4, offset: 1, angle: 90, color: "DDDDDD", opacity: 0.3 },
      rectRadius: 0.08,
    });

    // Severity badge
    slide.addShape(pres.ShapeType.roundRect, {
      x: 0.9, y: ry + 0.15, w: 0.75, h: 0.25,
      fill: { color: r.sevColor },
      rectRadius: 0.05,
    });
    slide.addText(r.severity, {
      x: 0.9, y: ry + 0.13, w: 0.75, h: 0.28,
      fontSize: 8, fontFace: "Arial", bold: true, color: C.white,
      align: "center", isTextBox: true, margin: 0, valign: "middle",
    });

    // Title
    slide.addText(r.title, {
      x: 1.85, y: ry + 0.08, w: 4.5, h: 0.3,
      fontSize: 13, fontFace: "Calibri", bold: true, color: C.navy,
      isTextBox: true, margin: 0,
    });

    // Description
    slide.addText(r.description, {
      x: 1.85, y: ry + 0.4, w: 4.8, h: 0.5,
      fontSize: 8.5, fontFace: "Arial", color: C.lightText, lineSpacingMultiple: 1.2,
      isTextBox: true, margin: 0,
    });

    // Mitigation label
    slide.addText("Mitigation:", {
      x: 7.0, y: ry + 0.08, w: 1.0, h: 0.3,
      fontSize: 9, fontFace: "Arial", bold: true, color: C.green,
      isTextBox: true, margin: 0,
    });

    // Mitigation text
    slide.addText(r.mitigation, {
      x: 7.0, y: ry + 0.4, w: 5.4, h: 0.5,
      fontSize: 8.5, fontFace: "Arial", color: C.text, lineSpacingMultiple: 1.2,
      isTextBox: true, margin: 0,
    });
  });

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 9 — Compliance & Quality
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Compliance & Quality Assurance", {
    x: 0.7, y: 0.4, w: 10.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  // Left — Certifications
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.7, y: 1.3, w: 5.8, h: 3.3,
    fill: { color: C.lightNavy },
    rectRadius: 0.12,
  });

  slide.addText("Certifications & Standards", {
    x: 1.1, y: 1.5, w: 5.0, h: 0.4,
    fontSize: 18, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const certs = [
    { cert: "HACCP", status: "In Implementation", color: C.amber },
    { cert: "ISO 22000", status: "In Implementation", color: C.amber },
    { cert: "FDA Establishment Registration", status: "Planned", color: C.lightText },
    { cert: "AAFCO-aligned Labeling", status: "Support Built In", color: C.green },
    { cert: "Full Batch Traceability", status: "Built into FAMSUN Line", color: C.green },
  ];

  certs.forEach((c, i) => {
    const cy = 2.1 + i * 0.48;
    iconCircle(slide, 1.1, cy + 0.06, 0.2, c.color);
    slide.addText(c.cert, {
      x: 1.5, y: cy, w: 2.8, h: 0.3,
      fontSize: 11, fontFace: "Arial", bold: true, color: C.text,
      isTextBox: true, margin: 0,
    });
    slide.addText(c.status, {
      x: 4.3, y: cy, w: 2.0, h: 0.3,
      fontSize: 10, fontFace: "Arial", color: c.color, align: "right",
      isTextBox: true, margin: 0,
    });
  });

  // Right — Fire Safety & Engineering
  slide.addShape(pres.ShapeType.roundRect, {
    x: 6.9, y: 1.3, w: 5.8, h: 3.3,
    fill: { color: C.lightNavy },
    rectRadius: 0.12,
  });

  slide.addText("Fire Safety & Building", {
    x: 7.3, y: 1.5, w: 5.0, h: 0.4,
    fontSize: 18, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const fireItems = [
    "Full NSI ERT fire safety dossier filed",
    "PCI plans approved (ground & 1st floor)",
    "Fire pressurization system designed",
    "Building modification authorization obtained",
    "Soufiane Incendie as certified provider",
  ];

  fireItems.forEach((f, i) => {
    const fy = 2.1 + i * 0.48;
    iconCircle(slide, 7.3, fy + 0.06, 0.2, C.green);
    slide.addText(f, {
      x: 7.7, y: fy, w: 4.7, h: 0.3,
      fontSize: 11, fontFace: "Arial", color: C.text,
      isTextBox: true, margin: 0,
    });
  });

  // Performance guarantees
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.7, y: 4.9, w: 11.95, h: 1.8,
    fill: { color: C.white },
    shadow: { type: "outer", blur: 5, offset: 2, angle: 90, color: "CCCCCC", opacity: 0.3 },
    rectRadius: 0.12,
  });

  slide.addText("FAMSUN Performance Guarantees", {
    x: 1.1, y: 5.1, w: 5.0, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const guarantees = [
    { item: "Penalty Clause", value: "2% of contract price per 2% deviation below capacity" },
    { item: "Maximum Penalty", value: "10% per product; 20% total of contract price" },
    { item: "Dog Food Milling", value: "Hammer mill 1.2mm sieve, D90 < 800 μm" },
    { item: "Cat Food Milling", value: "Hammer mill 1.0mm sieve, D90 < 500 μm" },
  ];

  guarantees.forEach((g, i) => {
    const gy = 5.6 + i * 0.27;
    slide.addText(g.item + ":", {
      x: 1.1, y: gy, w: 2.5, h: 0.25,
      fontSize: 10, fontFace: "Arial", bold: true, color: C.text,
      isTextBox: true, margin: 0,
    });
    slide.addText(g.value, {
      x: 3.6, y: gy, w: 9.0, h: 0.25,
      fontSize: 10, fontFace: "Arial", color: C.lightText,
      isTextBox: true, margin: 0,
    });
  });

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 10 — Digital Twin & Technology
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Digital Twin & Technology", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  slide.addText("Process simulation built before commissioning — de-risking production parameters", {
    x: 0.7, y: 0.95, w: 10.0, h: 0.35,
    fontSize: 13, fontFace: "Arial", color: C.lightText,
    isTextBox: true, margin: 0,
  });

  // Simulator features grid — 2x3
  const simFeatures = [
    { title: "Full Process Model", desc: "7 unit operations modeled: raw materials through packaging, with real FAMSUN equipment parameters" },
    { title: "Scenario Comparison", desc: "Compare production scenarios side-by-side: throughput variations, recipe changes, seasonal adjustments" },
    { title: "Energy Optimization", desc: "Steam, electricity, and water cost modeling at real Moroccan utility rates (MAD/kWh, MAD/m³)" },
    { title: "Live Dashboard", desc: "Real-time monitoring dashboard with live engine simulation for operator training pre-commissioning" },
    { title: "Quality Prediction", desc: "Moisture, water activity, density tracking at each stage with target validation and alerts" },
    { title: "Recipe Optimizer", desc: "Automated optimization of process parameters for cost, quality, and throughput targets" },
  ];

  simFeatures.forEach((f, i) => {
    const col = i % 3;
    const row = Math.floor(i / 3);
    const cx = 0.7 + col * 4.1;
    const cy = 1.6 + row * 2.55;

    slide.addShape(pres.ShapeType.roundRect, {
      x: cx, y: cy, w: 3.85, h: 2.2,
      fill: { color: C.white },
      shadow: { type: "outer", blur: 5, offset: 2, angle: 90, color: "CCCCCC", opacity: 0.3 },
      rectRadius: 0.1,
    });

    iconCircle(slide, cx + 0.25, cy + 0.25, 0.35, C.teal);
    slide.addText(`0${i + 1}`, {
      x: cx + 0.25, y: cy + 0.26, w: 0.35, h: 0.32,
      fontSize: 11, fontFace: "Arial", bold: true, color: C.white,
      align: "center", isTextBox: true, margin: 0,
    });

    slide.addText(f.title, {
      x: cx + 0.75, y: cy + 0.25, w: 2.8, h: 0.35,
      fontSize: 13, fontFace: "Calibri", bold: true, color: C.navy,
      isTextBox: true, margin: 0,
    });

    slide.addText(f.desc, {
      x: cx + 0.25, y: cy + 0.8, w: 3.4, h: 1.2,
      fontSize: 10, fontFace: "Arial", color: C.lightText, lineSpacingMultiple: 1.3,
      isTextBox: true, margin: 0,
    });
  });

  // Utility costs callout
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.7, y: 6.55, w: 11.95, h: 0.35,
    fill: { color: C.lightTeal },
    rectRadius: 0.08,
  });
  slide.addText([
    { text: "Utility Rates Modeled:   ", options: { bold: true, fontSize: 10, color: C.navy } },
    { text: "Steam: 0.18 MAD/kg   |   Electricity: 1.20 MAD/kWh   |   Water: 8.50 MAD/m³", options: { fontSize: 10, color: C.text } },
  ], {
    x: 1.1, y: 6.55, w: 11.5, h: 0.35,
    fontFace: "Arial", isTextBox: true, margin: 0, valign: "middle",
  });

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 11 — Partners & Team
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Partners & Team", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const partners = [
    {
      name: "FAMSUN",
      role: "Turnkey Production Line",
      detail: "SJPS165 twin-screw extruder, dryer, preconditioner, coater, cooler, packaging, silos. Full installation supervision and performance guarantees.",
      color: C.teal,
    },
    {
      name: "Normandie Pet Food",
      role: "EU Market JV Partner",
      detail: "French partner targeting EUR 300M revenue by 2030. Capitalized through Bpifrance and Credit Agricole. No equity lock-up, no capacity exclusivity.",
      color: C.amber,
    },
    {
      name: "Petland Maroc",
      role: "100% Factory Owner",
      detail: "Sam Aribi, Chef de Projet. Full ownership retained. Contractual JV structure preserves operational independence and strategic flexibility.",
      color: C.navy,
    },
    {
      name: "Soufiane Incendie",
      role: "Fire Safety Provider",
      detail: "Full NSI ERT dossier, PCI floor plans (ground & 1st floor), pressurization system design, building modification authorizations.",
      color: C.green,
    },
  ];

  partners.forEach((p, i) => {
    const py = 1.2 + i * 1.2;

    slide.addShape(pres.ShapeType.roundRect, {
      x: 0.7, y: py, w: 11.95, h: 1.15,
      fill: { color: C.white },
      shadow: { type: "outer", blur: 5, offset: 2, angle: 90, color: "DDDDDD", opacity: 0.3 },
      rectRadius: 0.1,
    });

    // Partner initial in circle
    iconCircle(slide, 1.0, py + 0.2, 0.7, p.color);
    slide.addText(p.name.charAt(0), {
      x: 1.0, y: py + 0.22, w: 0.7, h: 0.65,
      fontSize: 28, fontFace: "Calibri", bold: true, color: C.white,
      align: "center", isTextBox: true, margin: 0,
    });

    slide.addText(p.name, {
      x: 1.95, y: py + 0.12, w: 3.0, h: 0.35,
      fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
      isTextBox: true, margin: 0,
    });

    slide.addText(p.role, {
      x: 1.95, y: py + 0.45, w: 3.0, h: 0.25,
      fontSize: 11, fontFace: "Arial", color: p.color,
      isTextBox: true, margin: 0,
    });

    slide.addText(p.detail, {
      x: 5.2, y: py + 0.15, w: 7.2, h: 0.85,
      fontSize: 10.5, fontFace: "Arial", color: C.lightText, lineSpacingMultiple: 1.3,
      isTextBox: true, margin: 0, valign: "middle",
    });
  });

  // Recruitment section
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.7, y: 6.0, w: 11.95, h: 0.65,
    fill: { color: C.lightNavy },
    rectRadius: 0.1,
  });
  slide.addText("Recruitment in Progress", {
    x: 1.1, y: 6.05, w: 3.0, h: 0.25,
    fontSize: 12, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });
  slide.addText(
    "Technical Manager (Responsable Technique) and Quality Manager (Responsable Qualité) — CVs received, interview finalization by July 11, 2026",
    {
      x: 1.1, y: 6.3, w: 11.2, h: 0.3,
      fontSize: 10, fontFace: "Arial", color: C.lightText,
      isTextBox: true, margin: 0,
    }
  );

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 12 — Closing / Next Steps
// ═══════════════════════════════════════════════════════════════════
{
  const slide = darkSlide();

  // Amber accent
  slide.addShape(pres.ShapeType.rect, {
    x: 0, y: 0, w: 4.5, h: 1.5,
    fill: { color: C.amber }, transparency: 75,
  });

  slide.addText("Next Steps", {
    x: 0.8, y: 0.6, w: 8.0, h: 0.7,
    fontSize: 36, fontFace: "Calibri", bold: true, color: C.white,
    isTextBox: true, margin: 0,
  });

  const nextSteps = [
    { phase: "Immediate (Jul 2026)", items: [
      "Unblock oil storage tank spec review (RED item)",
      "Mobilize civil works contractors for 5 overdue foundations",
      "Finalize boiler, compressor, and elevator vendors by Jul 11",
    ]},
    { phase: "Near-term (Aug - Sep 2026)", items: [
      "Equipment manufacturing and quality inspections",
      "Complete gas installation vendor selection",
      "Initiate FAMSUN silo delivery schedule tracking",
    ]},
    { phase: "Pre-commissioning (Oct - Nov 2026)", items: [
      "All equipment delivered and installed on site",
      "Systems testing and FAMSUN performance validation",
      "Target: Facility commissioned November 24, 2026",
    ]},
  ];

  nextSteps.forEach((ns, i) => {
    const ny = 1.7 + i * 1.7;

    slide.addShape(pres.ShapeType.roundRect, {
      x: 0.8, y: ny, w: 11.7, h: 1.5,
      fill: { color: "1E2F50" },
      rectRadius: 0.1,
    });

    slide.addText(ns.phase, {
      x: 1.2, y: ny + 0.1, w: 4.0, h: 0.35,
      fontSize: 14, fontFace: "Calibri", bold: true, color: C.amber,
      isTextBox: true, margin: 0,
    });

    ns.items.forEach((item, j) => {
      iconCircle(slide, 1.2, ny + 0.6 + j * 0.3, 0.15, C.teal);
      slide.addText(item, {
        x: 1.5, y: ny + 0.5 + j * 0.3, w: 10.5, h: 0.3,
        fontSize: 11, fontFace: "Arial", color: "CCDDEE",
        isTextBox: true, margin: 0,
      });
    });
  });

  // Contact
  slide.addText("PetFactory Maroc  |  Petland Maroc  |  Sam Aribi, Chef de Projet", {
    x: 0.8, y: 6.5, w: 11.7, h: 0.3,
    fontSize: 12, fontFace: "Arial", color: C.amber,
    align: "center", isTextBox: true, margin: 0,
  });

  slide.addText("Confidential  |  For Investor Discussion Only", {
    x: 0.8, y: 6.9, w: 11.7, h: 0.3,
    fontSize: 10, fontFace: "Arial", color: "667788",
    align: "center", isTextBox: true, margin: 0,
  });
}

// ═══════════════════════════════════════════════════════════════════
// Generate
// ═══════════════════════════════════════════════════════════════════
const outPath = "/home/user/petfactory-morocco/PetFactory_Infrastructure_Investor_Deck.pptx";
pres.writeFile({ fileName: outPath }).then(() => {
  console.log("Deck generated: " + outPath);
}).catch(err => {
  console.error("Error:", err);
});
