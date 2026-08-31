const pptxgen = require("pptxgenjs");
const pres = new pptxgen();

// ─── Layout & Metadata ───────────────────────────────────────────
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.author = "PetFactory Maroc";
pres.subject = "Avancement Infrastructure - Mise à jour Investisseurs";
pres.title = "PetFactory Maroc - Avancement Infrastructure";

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
  slide.addText("PetFactory Maroc  |  Mise à jour Investisseurs  |  Août 2026", {
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
// SLIDE 1 — Titre
// ═══════════════════════════════════════════════════════════════════
{
  const slide = darkSlide();

  slide.addShape(pres.ShapeType.rect, {
    x: 9.0, y: 0, w: 4.33, h: 3.2,
    fill: { color: C.amber }, transparency: 15,
  });

  slide.addShape(pres.ShapeType.rect, {
    x: 10.5, y: 3.2, w: 2.83, h: 4.3,
    fill: { color: C.teal }, transparency: 80,
  });

  slide.addText("PETFACTORY", {
    x: 0.8, y: 1.4, w: 8.0, h: 1.0,
    fontSize: 52, fontFace: "Calibri", bold: true, color: C.white,
    isTextBox: true, margin: 0,
  });
  slide.addText("MAROC", {
    x: 0.8, y: 2.2, w: 8.0, h: 0.9,
    fontSize: 44, fontFace: "Calibri", bold: false, color: C.amber,
    isTextBox: true, margin: 0,
  });

  slide.addText("Rapport d'avancement Infrastructure", {
    x: 0.8, y: 3.5, w: 8.0, h: 0.5,
    fontSize: 22, fontFace: "Arial", color: C.lightText,
    isTextBox: true, margin: 0,
  });
  slide.addText("Mise à jour Investisseurs  |  Août 2026", {
    x: 0.8, y: 4.1, w: 8.0, h: 0.4,
    fontSize: 14, fontFace: "Arial", color: "8899AA",
    isTextBox: true, margin: 0,
  });

  slide.addText([
    { text: "5 T/H ", options: { bold: true, color: C.amber, fontSize: 13 } },
    { text: "Ligne d'extrusion sèche   |   ", options: { color: "8899AA", fontSize: 11 } },
    { text: "FAMSUN ", options: { bold: true, color: C.amber, fontSize: 13 } },
    { text: "Clé en main   |   ", options: { color: "8899AA", fontSize: 11 } },
    { text: "Sidi Bouathmane, Maroc", options: { color: "8899AA", fontSize: 11 } },
  ], {
    x: 0.8, y: 5.8, w: 10.0, h: 0.4,
    fontFace: "Arial", isTextBox: true, margin: 0,
  });

  slide.addText("Petland Maroc  |  Propriété 100%  |  Confidentiel", {
    x: 0.8, y: 6.5, w: 10.0, h: 0.3,
    fontSize: 9, fontFace: "Arial", color: "667788",
    isTextBox: true, margin: 0,
  });
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 2 — Résumé Exécutif
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Résumé Exécutif", {
    x: 0.7, y: 0.4, w: 6.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  slide.addText(
    "PetFactory Maroc est une plateforme de fabrication d'aliments premium pour animaux, " +
    "détenue à 100% par Petland Maroc. Conçue clé en main par FAMSUN avec une ligne " +
    "d'extrusion sèche de 5 T/h, l'usine cible la production en marque blanche et co-marquée " +
    "pour les distributeurs, de l'entrée de gamme au super-premium. Stratégiquement située à " +
    "Sidi Bouathmane près du port de Casablanca, avec accès direct aux marchés UE, US, Golfe et Afrique.",
    {
      x: 0.7, y: 1.2, w: 7.5, h: 1.2,
      fontSize: 13, fontFace: "Arial", color: C.text, lineSpacingMultiple: 1.35,
      isTextBox: true, margin: 0,
    }
  );

  statCard(slide, 0.7,  2.7, 2.8, 1.3, "5 T/H",     "Capacité d'extrusion",     C.teal);
  statCard(slide, 3.8,  2.7, 2.8, 1.3, "14",         "Systèmes d'infrastructure", C.navy);
  statCard(slide, 6.9,  2.7, 2.8, 1.3, "24,2%",     "Avancement global",         C.amber);
  statCard(slide, 10.0, 2.7, 2.8, 1.3, "Nov 2026",  "Mise en service cible",     C.green);

  slide.addText("Points clés", {
    x: 0.7, y: 4.4, w: 5.0, h: 0.4,
    fontSize: 18, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const highlights = [
    ["Accord de libre-échange Maroc-USA",     "Accès en franchise douanière, transit 7-12 jours côte Est"],
    ["HACCP & ISO 22000 en cours",            "Enregistrement FDA prévu ; traçabilité complète des lots"],
    ["Transformateur électrique — BC signé",  "1 600 KVA — fabrication démarrée juillet 2026"],
    ["Proximité ports UE, Golfe et Afrique",  "Hub logistique Casablanca, accès multi-marchés"],
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
// SLIDE 3 — Position Stratégique & Opportunité de Marché
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Position Stratégique", {
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

  slide.addText("Avantage Géographique", {
    x: 1.1, y: 1.5, w: 5.0, h: 0.4,
    fontSize: 18, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const locItems = [
    { title: "Sidi Bouathmane, Maroc", desc: "Près du port en eau profonde de Casablanca, services conteneurs directs vers NY/NJ, Norfolk, Savannah, Montréal" },
    { title: "ALE Maroc-USA (depuis 2006)", desc: "Franchise douanière sur produits qualifiés. 7-12 jours vers la côte Est US vs. 30+ jours depuis l'Asie" },
    { title: "Proximité UE", desc: "Accès direct au marché européen. Objectif CA 300 M EUR d'ici 2030" },
    { title: "Stabilité du MAD", desc: "Indexé sur panier EUR/USD — fiable pour contrats d'approvisionnement pluriannuels" },
    { title: "Golfe & Afrique", desc: "Marchés en croissance pour animaux de compagnie, accessibles depuis le hub de Casablanca" },
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

  slide.addText("Marchés Cibles", {
    x: 7.3, y: 1.5, w: 5.0, h: 0.4,
    fontSize: 18, fontFace: "Calibri", bold: true, color: C.white,
    isTextBox: true, margin: 0,
  });

  const markets = [
    { region: "Amérique du Nord",  detail: "2-3 partenariats acheteurs clés\nAccès en franchise (ALE)", color: C.amber },
    { region: "Union Européenne",  detail: "Accès direct marché UE\nProximité géographique", color: C.teal },
    { region: "États du Golfe",    detail: "Demande premium croissante\nClasse moyenne en expansion", color: C.green },
    { region: "Afrique",           detail: "Marché émergent animaux de compagnie\nProximité régionale", color: "A78BFA" },
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
    { text: "Incoterms : ", options: { bold: true, fontSize: 10, color: C.navy } },
    { text: "FOB Casablanca (CIF/DDP disponible)   |   ", options: { fontSize: 10, color: C.lightText } },
    { text: "QMC : ", options: { bold: true, fontSize: 10, color: C.navy } },
    { text: "Conteneur complet (20/40 pieds par SKU)   |   ", options: { fontSize: 10, color: C.lightText } },
    { text: "Transit : ", options: { bold: true, fontSize: 10, color: C.navy } },
    { text: "10-14 jours port-à-port côte Est US", options: { fontSize: 10, color: C.lightText } },
  ], {
    x: 0.7, y: 6.75, w: 12.0, h: 0.3,
    fontFace: "Arial", isTextBox: true, margin: 0,
  });

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 4 — Ligne de Production
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Ligne de Production", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  slide.addText("FAMSUN Clé en main  |  Extrusion sèche 5 T/h", {
    x: 0.7, y: 0.95, w: 8.0, h: 0.35,
    fontSize: 14, fontFace: "Arial", color: C.lightText,
    isTextBox: true, margin: 0,
  });

  const stages = [
    { name: "Matières\nPremières",     spec: "10% humidité\n25°C entrée",        color: C.navy },
    { name: "Pré-\nconditionneur",     spec: "Vapeur 350 kg/h\nEau 400 kg/h",    color: C.darkTeal },
    { name: "Extrudeuse\nSJPS165",     spec: "Moteur 203 kW\nFourreau 145°C",    color: C.teal },
    { name: "Séchoir\nGZDH2200",       spec: "Entrée 140°C\nTapis 44 m²",        color: C.amber },
    { name: "Refroidisseur",           spec: "12 min\ntemps de séjour",           color: "5B9BD5" },
    { name: "Enrobeur",                spec: "12% matière grasse\n2% appétent",   color: "7C68AE" },
    { name: "Conditionnement",         spec: "Salle à 20°C\n45% HR",             color: C.green },
  ];

  const stageW = 1.5;
  const gapW = 0.2;
  const totalW = stages.length * stageW + (stages.length - 1) * gapW;
  const startX = (13.33 - totalW) / 2;
  const stageY = 1.7;

  stages.forEach((s, i) => {
    const sx = startX + i * (stageW + gapW);

    slide.addShape(pres.ShapeType.roundRect, {
      x: sx, y: stageY, w: stageW, h: 1.7,
      fill: { color: s.color },
      rectRadius: 0.1,
    });

    slide.addText(`${i + 1}`, {
      x: sx, y: stageY + 0.1, w: stageW, h: 0.3,
      fontSize: 11, fontFace: "Arial", bold: true, color: C.white,
      align: "center", transparency: 40, isTextBox: true, margin: 0,
    });

    slide.addText(s.name, {
      x: sx + 0.1, y: stageY + 0.35, w: stageW - 0.2, h: 0.6,
      fontSize: 12, fontFace: "Calibri", bold: true, color: C.white,
      align: "center", isTextBox: true, margin: 0,
    });

    slide.addText(s.spec, {
      x: sx + 0.1, y: stageY + 0.95, w: stageW - 0.2, h: 0.6,
      fontSize: 9, fontFace: "Arial", color: C.white,
      align: "center", transparency: 20, isTextBox: true, margin: 0,
    });

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

  slide.addText("Performances Garanties", {
    x: 1.1, y: 4.1, w: 5.2, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const perfItems = [
    ["Aliment chien (croquette 8,0 mm)", "≥ 5,0 T/h"],
    ["Aliment chat (croquette 4,0 mm)",  "≥ 4,5 T/h"],
    ["Densité apparente",                "350-450 g/L"],
    ["Humidité cible",                   "9,0%"],
    ["Activité de l'eau limite",         "≤ 0,60"],
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

  slide.addText("Gamme de Produits", {
    x: 7.5, y: 4.1, w: 5.0, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const products = [
    "Croquettes premium sèches (chien & chat)",
    "Formulations sur mesure (forme, densité, enrobage)",
    "Formats sans céréales & protéine unique",
    "Régimes de type vétérinaire",
    "Phase 2 : Ligne humide (pâté, morceaux en sauce, friandises)",
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
// SLIDE 5 — Aperçu des Systèmes d'Infrastructure
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Systèmes d'Infrastructure", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  slide.addText("14 systèmes suivis  |  128 tâches  |  24,2% d'avancement global", {
    x: 0.7, y: 0.95, w: 10.0, h: 0.35,
    fontSize: 14, fontFace: "Arial", color: C.lightText,
    isTextBox: true, margin: 0,
  });

  statCard(slide, 0.7,  1.5, 2.0, 1.0, "24",  "Tâches terminées",    C.green);
  statCard(slide, 2.9,  1.5, 2.0, 1.0, "14",  "En cours",            C.amber);
  statCard(slide, 5.1,  1.5, 2.0, 1.0, "90",  "Non démarrées",       C.lightText);
  statCard(slide, 7.3,  1.5, 2.0, 1.0, "1/7", "Jalons atteints",     C.teal);

  // Progress bar
  slide.addShape(pres.ShapeType.roundRect, {
    x: 9.8, y: 1.5, w: 2.9, h: 1.0,
    fill: { color: C.lightNavy },
    rectRadius: 0.1,
  });
  slide.addText("24,2%", {
    x: 9.8, y: 1.52, w: 2.9, h: 0.5,
    fontSize: 24, fontFace: "Calibri", bold: true, color: C.teal, align: "center",
    isTextBox: true, margin: 0,
  });
  slide.addShape(pres.ShapeType.roundRect, {
    x: 10.1, y: 2.15, w: 2.3, h: 0.18,
    fill: { color: "D0D8E0" },
    rectRadius: 0.09,
  });
  slide.addShape(pres.ShapeType.roundRect, {
    x: 10.1, y: 2.15, w: 2.3 * 0.242, h: 0.18,
    fill: { color: C.teal },
    rectRadius: 0.09,
  });

  const systems = [
    { name: "Électricité & Transformateur", spec: "1 600 KVA",       progress: 33, rag: "GREEN",  note: "BC signé. Fabrication démarre 1er juil." },
    { name: "Salle de contrôle & TGBT",    spec: "Séparation",       progress: 83, rag: "GREEN",  note: "Spécifications & plans approuvés" },
    { name: "Travaux béton extérieurs",     spec: "Béton",            progress: 83, rag: "GREEN",  note: "Finalisation fournisseur en cours" },
    { name: "Froid industriel",             spec: "Séparation sèche", progress: 67, rag: "GREEN",  note: "Revue des spécifications terminée" },
    { name: "Logiciels",                    spec: "ERP / MES",        progress: 67, rag: "GREEN",  note: "Approbation en cours" },
    { name: "Pont-bascule",                 spec: "60 T",             progress: 25, rag: "ORANGE", note: "Fournisseur choisi, BC en attente" },
    { name: "Système d'eau",               spec: "10 000 kg/h",      progress: 21, rag: "ORANGE", note: "Sélection pompe/réservoir démarrée" },
    { name: "Installation gaz",            spec: "15 m³",             progress: 21, rag: "ORANGE", note: "Fournisseur attendu le 21 juil." },
    { name: "Chaudière",                   spec: "6 000 kg/h vapeur", progress: 18, rag: "ORANGE", note: "Finalisation fournisseur le 11 juil." },
    { name: "Compresseur",                 spec: "37 kW x 2",        progress: 19, rag: "ORANGE", note: "Ingénierie faite, fournisseur en attente" },
    { name: "Ascenseur",                   spec: "2 x 2 T",          progress: 18, rag: "ORANGE", note: "Conception validée" },
    { name: "Cuve de stockage huile",      spec: "2 x 20 000 L",     progress:  4, rag: "RED",    note: "CRITIQUE : +8 sem. de retard" },
    { name: "Solaire",                     spec: "480 KVA cible",     progress:  0, rag: "GREY",   note: "Non encore lancé" },
  ];

  const tableY = 2.8;
  const rowH = 0.29;

  slide.addShape(pres.ShapeType.rect, {
    x: 0.7, y: tableY, w: 11.93, h: 0.35,
    fill: { color: C.navy },
  });
  const headers = [
    { text: "Système", x: 0.75, w: 2.6 },
    { text: "Spécification", x: 3.35, w: 1.8 },
    { text: "Avancement", x: 5.15, w: 2.8 },
    { text: "Statut", x: 7.95, w: 0.8 },
    { text: "Remarque", x: 8.75, w: 3.85 },
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

    slide.addText(s.name, {
      x: 0.75, y: ry, w: 2.6, h: rowH,
      fontSize: 9, fontFace: "Arial", bold: true, color: C.text,
      isTextBox: true, margin: 0, valign: "middle",
    });

    slide.addText(s.spec, {
      x: 3.35, y: ry, w: 1.8, h: rowH,
      fontSize: 9, fontFace: "Arial", color: C.lightText,
      isTextBox: true, margin: 0, valign: "middle",
    });

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

    const ragColor = s.rag === "RED" ? C.red : s.rag === "ORANGE" ? C.orange : s.rag === "GREEN" ? C.green : "AABBCC";
    iconCircle(slide, 8.2, ry + 0.09, 0.14, ragColor);

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
// SLIDE 6 — Systèmes Clés en Détail
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Systèmes Clés en Détail", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  // Card 1 — Chaudière
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.7, y: 1.3, w: 3.85, h: 4.2,
    fill: { color: C.white },
    shadow: { type: "outer", blur: 6, offset: 2, angle: 90, color: "CCCCCC", opacity: 0.35 },
    rectRadius: 0.12,
  });
  iconCircle(slide, 1.0, 1.5, 0.45, C.amber);
  slide.addText("Chaudière", {
    x: 1.6, y: 1.55, w: 2.8, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });
  const boilerSpecs = [
    "2 chaudières vapeur à tubes de fumée (N+1)",
    "Conception trois passes à fond humide",
    "Demande pic : 2 600 kg/h vapeur saturée",
    "Capacité unitaire : 1 600-2 000 kg/h",
    "Conception : 10 barg / Exploitation : 7-8 barg",
    "Bicombustible : GPL principal, GN prêt",
    "Rendement : ≥94% GN / ≥93% GPL",
    "Incl. alimentation eau, dégazeur, adoucisseur, OI",
    "Train vapeur culinaire (316L SS, ≤2μm)",
  ];
  boilerSpecs.forEach((spec, i) => {
    slide.addText(spec, {
      x: 1.0, y: 2.15 + i * 0.35, w: 3.3, h: 0.3,
      fontSize: 9, fontFace: "Arial", color: C.text,
      isTextBox: true, margin: 0,
    });
  });

  // Card 2 — Électricité
  slide.addShape(pres.ShapeType.roundRect, {
    x: 4.75, y: 1.3, w: 3.85, h: 4.2,
    fill: { color: C.white },
    shadow: { type: "outer", blur: 6, offset: 2, angle: 90, color: "CCCCCC", opacity: 0.35 },
    rectRadius: 0.12,
  });
  iconCircle(slide, 5.05, 1.5, 0.45, C.green);
  slide.addText("Électricité & Énergie", {
    x: 5.65, y: 1.55, w: 2.8, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });
  const elecSpecs = [
    "Transformateur 1 600 KVA (BC signé)",
    "Fabrication démarre : 1er juillet 2026",
    "Délai de livraison : 12 semaines",
    "Seul système avec bon de commande signé",
    "",
    "Cible solaire : 480 KVA (30% de la charge)",
    "Cadre : Loi marocaine 40-19",
    "Incentives : ECOTAQA / TATWIR",
    "Fournisseur solaire : non encore lancé",
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

  // Card 3 — Air comprimé & Eau
  slide.addShape(pres.ShapeType.roundRect, {
    x: 8.8, y: 1.3, w: 3.85, h: 4.2,
    fill: { color: C.white },
    shadow: { type: "outer", blur: 6, offset: 2, angle: 90, color: "CCCCCC", opacity: 0.35 },
    rectRadius: 0.12,
  });
  iconCircle(slide, 9.1, 1.5, 0.45, C.teal);
  slide.addText("Air & Eau", {
    x: 9.7, y: 1.55, w: 2.8, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });
  const airWaterSpecs = [
    "Air comprimé :",
    "  2 x 37 kW compresseurs",
    "  Demande totale : 363 m³/h",
    "  Ligne produit : 258 m³/h",
    "  Ingénierie terminée",
    "",
    "Système d'eau :",
    "  Capacité de conception : 10 000 kg/h",
    "  Débit réel : 2 760 kg/h",
    "  Sélection pompe/réservoir en cours",
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
  slide.addText("Synthèse Distribution Vapeur", {
    x: 1.1, y: 5.85, w: 3.5, h: 0.3,
    fontSize: 12, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });
  slide.addText(
    "Séchoir : 1,40 T/h (DN100)   |   Préconditionneur : 0,75 T/h (DN60)   |   Cuves graisse : 0,30 T/h (DN32)   |   " +
    "Total : 2,45 T/h   |   Retour condensats : 69,7% (cible 80%+ avec récupération flash)",
    {
      x: 1.1, y: 6.2, w: 11.2, h: 0.4,
      fontSize: 10, fontFace: "Arial", color: C.text,
      isTextBox: true, margin: 0,
    }
  );

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 7 — Calendrier du Projet
// ═══════════════════════════════════════════════════════════════════
{
  const slide = darkSlide();

  slide.addText("Calendrier du Projet", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.white,
    isTextBox: true, margin: 0,
  });

  slide.addText("Mise en service cible : 24 novembre 2026", {
    x: 0.7, y: 0.95, w: 8.0, h: 0.35,
    fontSize: 14, fontFace: "Arial", color: C.amber,
    isTextBox: true, margin: 0,
  });

  const lineY = 2.0;
  slide.addShape(pres.ShapeType.rect, {
    x: 1.2, y: lineY, w: 10.9, h: 0.04,
    fill: { color: C.teal },
  });

  const milestones = [
    { label: "Revue plans\nFAMSUN",            date: "31 mai",   status: "done",    x: 1.2 },
    { label: "Début fab.\nTransformateur",      date: "1er juil.",status: "next",    x: 2.8 },
    { label: "Finalisation\nFournisseurs x3",   date: "11 juil.", status: "next",    x: 4.2 },
    { label: "Fabrication\nÉquipements",        date: "18 août",  status: "future",  x: 5.8 },
    { label: "Expédition\nÉquipements",         date: "18 sept.", status: "future",  x: 7.3 },
    { label: "Livraisons\nSur site",            date: "28 oct.",  status: "future",  x: 8.8 },
    { label: "Installation\nTerminée",          date: "8 nov.",   status: "future",  x: 10.3 },
    { label: "Mise en\nService",                date: "24 nov.",  status: "target",  x: 11.8 },
  ];

  milestones.forEach((m) => {
    const dotColor = m.status === "done" ? C.green : m.status === "next" ? C.amber : m.status === "target" ? C.teal : "445566";
    const dotSize = m.status === "target" ? 0.28 : 0.22;
    const dotOffset = (dotSize - 0.04) / 2;

    iconCircle(slide, m.x - dotSize / 2 + 0.15, lineY - dotOffset, dotSize, dotColor);

    slide.addText(m.date, {
      x: m.x - 0.3, y: lineY - 0.55, w: 1.0, h: 0.3,
      fontSize: 10, fontFace: "Arial", bold: true,
      color: m.status === "done" ? C.green : m.status === "target" ? C.teal : "AABBCC",
      align: "center", isTextBox: true, margin: 0,
    });

    slide.addText(m.label, {
      x: m.x - 0.4, y: lineY + 0.35, w: 1.2, h: 0.55,
      fontSize: 9, fontFace: "Arial", color: "AABBCC", align: "center",
      isTextBox: true, margin: 0,
    });

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

  slide.addText("Chemin Critique", {
    x: 1.1, y: 3.7, w: 5.0, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.amber,
    isTextBox: true, margin: 0,
  });

  const critItems = [
    { phase: "MAINTENANT", item: "Travaux de génie civil pour chaudière, compresseur, pont-bascule, ascenseur, tranchées d'eau", deadline: "EN RETARD (était 18 juin)", color: C.red },
    { phase: "2 SEMAINES", item: "Finalisation fournisseurs : Chaudière + Compresseur + Ascenseur", deadline: "11 juil. 2026", color: C.amber },
    { phase: "3 SEMAINES", item: "Finalisation fournisseur installation gaz", deadline: "21 juil. 2026", color: C.amber },
    { phase: "6 SEMAINES", item: "Fabrication équipements terminée (chaudière, ascenseur)", deadline: "18 août 2026", color: "AABBCC" },
    { phase: "10 SEMAINES",item: "Expédition équipements majeurs terminée", deadline: "18 sept. 2026", color: "AABBCC" },
    { phase: "12 SEMAINES",item: "Livraison chaudière sur site (contrainte ferme du cahier des charges)", deadline: "19 oct. 2026", color: "AABBCC" },
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
// SLIDE 8 — Risques & Atténuation
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Risques & Atténuation", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const risks = [
    {
      title: "Retard Cuve de Stockage Huile",
      severity: "ÉLEVÉ",
      sevColor: C.red,
      description: "Revue spécification Annexe D bloquée depuis le 21 avril (+8 sem.). Seul système ROUGE. Fournisseur non sélectionné, BC non émis, fondation non démarrée, permis transport hors gabarit non initié.",
      mitigation: "Déblocage immédiat de la revue. Sélection fournisseur et demande de permis en parallèle. Escalade à la direction du projet.",
    },
    {
      title: "Travaux de Génie Civil Non Démarrés",
      severity: "ÉLEVÉ",
      sevColor: C.red,
      description: "5 lots de fondations étaient prévus le 18 juin et sont tous non démarrés (chaudière, compresseur, pont-bascule, cage ascenseur, tranchées d'eau).",
      mitigation: "Mobilisation accélérée des entrepreneurs. Prioriser les fondations chaudière et compresseur sur le chemin critique. Suivi hebdomadaire.",
    },
    {
      title: "Compression des Délais Fournisseurs",
      severity: "MOYEN",
      sevColor: C.orange,
      description: "Les fournisseurs chaudière, compresseur et ascenseur doivent être finalisés d'ici le 11 juillet. La fabrication doit démarrer le 18 juillet pour respecter la fenêtre d'expédition de septembre.",
      mitigation: "Suivi quotidien avec fournisseurs présélectionnés. Pré-négocier les conditions LOI. Préparer des fournisseurs de secours.",
    },
    {
      title: "Visibilité Silos FAMSUN",
      severity: "MOYEN",
      sevColor: C.orange,
      description: "Le périmètre silos dépend entièrement de l'équipe FAMSUN en Chine. Aucun suivi indépendant. Dernière mise à jour : avril 2026.",
      mitigation: "Demander une mise à jour formelle et un calendrier de livraison à FAMSUN. Points bimensuels. Définir les critères de réception.",
    },
    {
      title: "Solaire (0% d'avancement)",
      severity: "FAIBLE",
      sevColor: C.lightText,
      description: "Aucune tâche démarrée pour la cible solaire de 480 KVA. Pas encore sur le chemin critique mais représente des économies et un positionnement ESG.",
      mitigation: "Lancer l'appel d'offres fournisseurs au T4 2026. Tirer parti des incitations de la Loi 40-19. Mise en service possible post-démarrage.",
    },
  ];

  risks.forEach((r, i) => {
    const ry = 1.3 + i * 1.18;

    slide.addShape(pres.ShapeType.roundRect, {
      x: 0.7, y: ry, w: 11.95, h: 1.0,
      fill: { color: C.white },
      shadow: { type: "outer", blur: 4, offset: 1, angle: 90, color: "DDDDDD", opacity: 0.3 },
      rectRadius: 0.08,
    });

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

    slide.addText(r.title, {
      x: 1.85, y: ry + 0.08, w: 4.5, h: 0.3,
      fontSize: 13, fontFace: "Calibri", bold: true, color: C.navy,
      isTextBox: true, margin: 0,
    });

    slide.addText(r.description, {
      x: 1.85, y: ry + 0.4, w: 4.8, h: 0.5,
      fontSize: 8.5, fontFace: "Arial", color: C.lightText, lineSpacingMultiple: 1.2,
      isTextBox: true, margin: 0,
    });

    slide.addText("Atténuation :", {
      x: 7.0, y: ry + 0.08, w: 1.2, h: 0.3,
      fontSize: 9, fontFace: "Arial", bold: true, color: C.green,
      isTextBox: true, margin: 0,
    });

    slide.addText(r.mitigation, {
      x: 7.0, y: ry + 0.4, w: 5.4, h: 0.5,
      fontSize: 8.5, fontFace: "Arial", color: C.text, lineSpacingMultiple: 1.2,
      isTextBox: true, margin: 0,
    });
  });

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 9 — Conformité & Qualité
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Conformité & Assurance Qualité", {
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

  slide.addText("Certifications & Normes", {
    x: 1.1, y: 1.5, w: 5.0, h: 0.4,
    fontSize: 18, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const certs = [
    { cert: "HACCP", status: "En cours de mise en place", color: C.amber },
    { cert: "ISO 22000", status: "En cours de mise en place", color: C.amber },
    { cert: "Enregistrement FDA", status: "Prévu", color: C.lightText },
    { cert: "Étiquetage conforme AAFCO", status: "Intégré nativement", color: C.green },
    { cert: "Traçabilité complète des lots", status: "Intégrée ligne FAMSUN", color: C.green },
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

  slide.addText("Sécurité Incendie & Bâtiment", {
    x: 7.3, y: 1.5, w: 5.0, h: 0.4,
    fontSize: 18, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const fireItems = [
    "Dossier complet sécurité incendie NSI ERT déposé",
    "Plans PCI approuvés (RDC & 1er étage)",
    "Système de pressurisation incendie conçu",
    "Autorisation de modification du bâtiment obtenue",
    "Soufiane Incendie comme prestataire certifié",
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

  slide.addText("Garanties de Performance FAMSUN", {
    x: 1.1, y: 5.1, w: 5.0, h: 0.35,
    fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const guarantees = [
    { item: "Clause de pénalité", value: "2% du prix contrat par 2% d'écart sous la capacité" },
    { item: "Pénalité maximale", value: "10% par produit ; 20% du prix total du contrat" },
    { item: "Broyage aliment chien", value: "Broyeur à marteaux tamis 1,2 mm, D90 < 800 μm" },
    { item: "Broyage aliment chat", value: "Broyeur à marteaux tamis 1,0 mm, D90 < 500 μm" },
  ];

  guarantees.forEach((g, i) => {
    const gy = 5.6 + i * 0.27;
    slide.addText(g.item + " :", {
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
// SLIDE 10 — Jumeau Numérique & Technologie
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Jumeau Numérique & Technologie", {
    x: 0.7, y: 0.3, w: 12.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  slide.addText("Simulation de procédé construite avant mise en service — réduction des risques de production", {
    x: 0.7, y: 0.9, w: 12.0, h: 0.35,
    fontSize: 13, fontFace: "Arial", color: C.lightText,
    isTextBox: true, margin: 0,
  });

  const simFeatures = [
    { title: "Modèle Complet", desc: "7 opérations unitaires modélisées : matières premières jusqu'au conditionnement, avec paramètres réels FAMSUN" },
    { title: "Comparaison de Scénarios", desc: "Comparaison côte à côte : variations de débit, changements de recettes, ajustements saisonniers" },
    { title: "Optimisation Énergétique", desc: "Modélisation coûts vapeur, électricité et eau aux tarifs réels marocains (MAD/kWh, MAD/m³)" },
    { title: "Tableau de Bord en Direct", desc: "Tableau de bord temps réel avec simulation moteur pour formation opérateurs avant mise en service" },
    { title: "Prédiction Qualité", desc: "Suivi humidité, activité de l'eau, densité à chaque étape avec validation cibles et alertes" },
    { title: "Optimiseur de Recettes", desc: "Optimisation automatisée des paramètres procédé pour coût, qualité et objectifs de débit" },
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

  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.7, y: 6.55, w: 11.95, h: 0.35,
    fill: { color: C.lightTeal },
    rectRadius: 0.08,
  });
  slide.addText([
    { text: "Tarifs modélisés :   ", options: { bold: true, fontSize: 10, color: C.navy } },
    { text: "Vapeur : 0,18 MAD/kg   |   Électricité : 1,20 MAD/kWh   |   Eau : 8,50 MAD/m³", options: { fontSize: 10, color: C.text } },
  ], {
    x: 1.1, y: 6.55, w: 11.5, h: 0.35,
    fontFace: "Arial", isTextBox: true, margin: 0, valign: "middle",
  });

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 11 — Partenaires & Équipe
// ═══════════════════════════════════════════════════════════════════
{
  const slide = lightSlide();

  slide.addText("Partenaires & Équipe", {
    x: 0.7, y: 0.4, w: 8.0, h: 0.6,
    fontSize: 32, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });

  const partners = [
    {
      name: "FAMSUN",
      role: "Ligne de production clé en main",
      detail: "Extrudeuse bi-vis SJPS165, séchoir, préconditionneur, enrobeur, refroidisseur, conditionnement, silos. Supervision complète de l'installation et garanties de performance.",
      color: C.teal,
    },
    {
      name: "Petland Maroc",
      role: "Propriétaire 100% de l'usine",
      detail: "Sam Aribi, Chef de Projet. Propriété intégrale conservée. Indépendance opérationnelle et flexibilité stratégique totales.",
      color: C.navy,
    },
    {
      name: "Soufiane Incendie",
      role: "Prestataire Sécurité Incendie",
      detail: "Dossier complet NSI ERT, plans PCI (RDC & 1er étage), conception système de pressurisation, autorisations de modification du bâtiment.",
      color: C.green,
    },
  ];

  partners.forEach((p, i) => {
    const py = 1.2 + i * 1.4;

    slide.addShape(pres.ShapeType.roundRect, {
      x: 0.7, y: py, w: 11.95, h: 1.3,
      fill: { color: C.white },
      shadow: { type: "outer", blur: 5, offset: 2, angle: 90, color: "DDDDDD", opacity: 0.3 },
      rectRadius: 0.1,
    });

    iconCircle(slide, 1.0, py + 0.25, 0.7, p.color);
    slide.addText(p.name.charAt(0), {
      x: 1.0, y: py + 0.27, w: 0.7, h: 0.65,
      fontSize: 28, fontFace: "Calibri", bold: true, color: C.white,
      align: "center", isTextBox: true, margin: 0,
    });

    slide.addText(p.name, {
      x: 1.95, y: py + 0.15, w: 3.0, h: 0.35,
      fontSize: 16, fontFace: "Calibri", bold: true, color: C.navy,
      isTextBox: true, margin: 0,
    });

    slide.addText(p.role, {
      x: 1.95, y: py + 0.5, w: 3.0, h: 0.25,
      fontSize: 11, fontFace: "Arial", color: p.color,
      isTextBox: true, margin: 0,
    });

    slide.addText(p.detail, {
      x: 5.2, y: py + 0.15, w: 7.2, h: 1.0,
      fontSize: 10.5, fontFace: "Arial", color: C.lightText, lineSpacingMultiple: 1.3,
      isTextBox: true, margin: 0, valign: "middle",
    });
  });

  // Recruitment section
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.7, y: 5.7, w: 11.95, h: 0.75,
    fill: { color: C.lightNavy },
    rectRadius: 0.1,
  });
  slide.addText("Recrutement en Cours", {
    x: 1.1, y: 5.75, w: 3.0, h: 0.25,
    fontSize: 12, fontFace: "Calibri", bold: true, color: C.navy,
    isTextBox: true, margin: 0,
  });
  slide.addText(
    "Responsable Technique et Responsable Qualité — CV reçus, finalisation des entretiens prévue le 11 juillet 2026",
    {
      x: 1.1, y: 6.05, w: 11.2, h: 0.3,
      fontSize: 10, fontFace: "Arial", color: C.lightText,
      isTextBox: true, margin: 0,
    }
  );

  addSlideNumber(slide, false);
}

// ═══════════════════════════════════════════════════════════════════
// SLIDE 12 — Prochaines Étapes
// ═══════════════════════════════════════════════════════════════════
{
  const slide = darkSlide();

  slide.addShape(pres.ShapeType.rect, {
    x: 0, y: 0, w: 4.5, h: 1.5,
    fill: { color: C.amber }, transparency: 75,
  });

  slide.addText("Prochaines Étapes", {
    x: 0.8, y: 0.6, w: 8.0, h: 0.7,
    fontSize: 36, fontFace: "Calibri", bold: true, color: C.white,
    isTextBox: true, margin: 0,
  });

  const nextSteps = [
    { phase: "Immédiat (Juil. 2026)", items: [
      "Débloquer la revue spécification cuve huile (élément ROUGE)",
      "Mobiliser les entrepreneurs génie civil pour les 5 fondations en retard",
      "Finaliser les fournisseurs chaudière, compresseur et ascenseur d'ici le 11 juil.",
    ]},
    { phase: "Court terme (Août - Sept. 2026)", items: [
      "Fabrication des équipements et inspections qualité",
      "Finaliser la sélection du fournisseur gaz",
      "Lancer le suivi du calendrier de livraison des silos FAMSUN",
    ]},
    { phase: "Pré-mise en service (Oct. - Nov. 2026)", items: [
      "Tous les équipements livrés et installés sur site",
      "Tests systèmes et validation des performances FAMSUN",
      "Objectif : Usine mise en service le 24 novembre 2026",
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

  slide.addText("PetFactory Maroc  |  Petland Maroc  |  Sam Aribi, Chef de Projet", {
    x: 0.8, y: 6.5, w: 11.7, h: 0.3,
    fontSize: 12, fontFace: "Arial", color: C.amber,
    align: "center", isTextBox: true, margin: 0,
  });

  slide.addText("Confidentiel  |  Réservé aux discussions avec les investisseurs", {
    x: 0.8, y: 6.9, w: 11.7, h: 0.3,
    fontSize: 10, fontFace: "Arial", color: "667788",
    align: "center", isTextBox: true, margin: 0,
  });
}

// ═══════════════════════════════════════════════════════════════════
// Générer
// ═══════════════════════════════════════════════════════════════════
const outPath = "/home/user/petfactory-morocco/PetFactory_Infrastructure_Investor_Deck.pptx";
pres.writeFile({ fileName: outPath }).then(() => {
  console.log("Deck généré : " + outPath);
}).catch(err => {
  console.error("Erreur :", err);
});
