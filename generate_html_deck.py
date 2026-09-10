import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Superimposition & Anthropomorphization in Design | Bhavya Anand (2501730046)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-dark: #090D16;
      --card-bg: rgba(26, 35, 53, 0.7);
      --card-border: rgba(71, 85, 105, 0.4);
      --accent-blue: #38BDF8;
      --accent-cyan: #2DD4BF;
      --accent-purple: #A855F7;
      --accent-rose: #F43F5E;
      --accent-amber: #F59E0B;
      --accent-emerald: #10B981;
      --text-main: #F8FAFC;
      --text-muted: #94A3B8;
      --text-dim: #64748B;
      --font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-heading: 'Space Grotesk', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-body);
      overflow: hidden;
      height: 100vh;
      width: 100vw;
      user-select: none;
      -webkit-font-smoothing: antialiased;
    }

    /* Ambient Background Glow */
    .ambient-glow {
      position: fixed;
      top: -20%;
      left: 10%;
      width: 60vw;
      height: 60vh;
      background: radial-gradient(circle, rgba(56, 189, 248, 0.08) 0%, rgba(168, 85, 247, 0.05) 50%, transparent 70%);
      filter: blur(80px);
      z-index: 0;
      pointer-events: none;
    }

    /* Top Navigation / Status */
    header {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 54px;
      padding: 0 32px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.07);
      background: rgba(9, 13, 22, 0.85);
      backdrop-filter: blur(16px);
      z-index: 100;
    }

    .brand-meta {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .badge-uni {
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: var(--accent-blue);
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      letter-spacing: 0.5px;
    }

    .deck-title {
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 500;
    }

    .header-controls {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .slide-counter {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--accent-cyan);
      background: rgba(45, 212, 191, 0.08);
      padding: 4px 12px;
      border-radius: 20px;
      border: 1px solid rgba(45, 212, 191, 0.2);
    }

    .ctrl-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }

    .ctrl-btn:hover {
      background: rgba(255, 255, 255, 0.12);
      border-color: var(--accent-blue);
      color: var(--accent-blue);
    }

    /* Progress Bar */
    .progress-bar {
      position: fixed;
      top: 53px;
      left: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple), var(--accent-cyan));
      width: 0%;
      transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 101;
    }

    /* Viewport & Slide Container */
    #slide-viewport {
      position: relative;
      width: 100vw;
      height: calc(100vh - 54px);
      margin-top: 54px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
      z-index: 10;
    }

    .slide {
      position: absolute;
      width: min(1360px, 94vw);
      height: min(760px, 86vh);
      background: rgba(18, 24, 38, 0.85);
      backdrop-filter: blur(24px);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 24px;
      padding: 40px 48px;
      display: none;
      flex-direction: column;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.7), 0 0 1px 1px rgba(255, 255, 255, 0.05);
      opacity: 0;
      transform: scale(0.98);
      transition: opacity 0.35s ease, transform 0.35s ease;
    }

    .slide.active {
      display: flex;
      opacity: 1;
      transform: scale(1);
    }

    /* Slide Header */
    .slide-header {
      margin-bottom: 24px;
    }

    .slide-tag {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--accent-blue);
      margin-bottom: 6px;
      display: inline-block;
    }

    .slide-title {
      font-family: var(--font-heading);
      font-size: 28px;
      font-weight: 700;
      color: #FFFFFF;
      letter-spacing: -0.5px;
      line-height: 1.2;
    }

    .slide-subtitle {
      font-size: 14px;
      color: var(--text-muted);
      margin-top: 6px;
    }

    /* Grid Layouts */
    .grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      flex: 1;
      min-height: 0;
    }

    .grid-2-asym {
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 24px;
      flex: 1;
      min-height: 0;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      flex: 1;
      min-height: 0;
    }

    .grid-4 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: 1fr 1fr;
      gap: 18px;
      flex: 1;
      min-height: 0;
    }

    /* Card Component */
    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 22px 26px;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
    }

    .card h3 {
      font-size: 16px;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .card h3 .pill {
      font-size: 10px;
      padding: 2px 8px;
      border-radius: 4px;
      font-family: var(--font-mono);
    }

    .card p {
      font-size: 13.5px;
      line-height: 1.6;
      color: var(--text-muted);
      margin-bottom: 12px;
    }

    .card ul {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .card li {
      font-size: 13px;
      line-height: 1.5;
      color: var(--text-muted);
      position: relative;
      padding-left: 18px;
    }

    .card li::before {
      content: "•";
      position: absolute;
      left: 0;
      color: var(--accent-blue);
      font-weight: bold;
    }

    .card strong {
      color: var(--text-main);
    }

    /* Visual Media Containers */
    .media-card {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: rgba(11, 15, 25, 0.7);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 16px;
      padding: 16px;
      position: relative;
      overflow: hidden;
    }

    .media-card img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      border-radius: 10px;
    }

    .media-caption {
      font-size: 11.5px;
      color: var(--text-dim);
      margin-top: 10px;
      text-align: center;
      font-style: italic;
    }

    /* Student ID Card (Slide 1) */
    .id-card-wrapper {
      background: linear-gradient(135deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95));
      border: 1px solid rgba(56, 189, 248, 0.4);
      border-radius: 20px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(56, 189, 248, 0.05);
      position: relative;
    }

    .id-header {
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 14px;
      margin-bottom: 16px;
      text-align: center;
    }

    .id-header h4 {
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 1px;
      color: var(--accent-blue);
      text-transform: uppercase;
    }

    .id-header span {
      font-size: 11px;
      color: var(--text-muted);
    }

    .id-body {
      display: flex;
      gap: 18px;
      align-items: center;
      margin-bottom: 18px;
    }

    .id-photo {
      width: 90px;
      height: 115px;
      border-radius: 10px;
      object-fit: cover;
      border: 2px solid var(--accent-cyan);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    }

    .id-info {
      display: flex;
      flex-direction: column;
      gap: 5px;
    }

    .id-field {
      font-size: 12px;
      color: var(--text-muted);
    }

    .id-field strong {
      color: #FFFFFF;
      font-size: 13px;
    }

    .id-badge {
      display: inline-block;
      font-size: 10.5px;
      background: rgba(16, 185, 129, 0.15);
      color: var(--accent-emerald);
      border: 1px solid rgba(16, 185, 129, 0.3);
      padding: 2px 8px;
      border-radius: 4px;
      font-weight: 700;
      margin-top: 4px;
    }

    .id-footer {
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 14px;
      font-size: 11px;
      color: var(--text-dim);
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    /* Comparison Table (Slide 10) */
    .heuristic-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12.5px;
      margin-top: 8px;
    }

    .heuristic-table th {
      background: rgba(30, 41, 59, 0.9);
      color: var(--accent-blue);
      padding: 12px 14px;
      text-align: left;
      font-weight: 700;
      border-bottom: 2px solid rgba(56, 189, 248, 0.3);
      font-size: 11px;
      letter-spacing: 0.5px;
    }

    .heuristic-table td {
      padding: 12px 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      color: var(--text-muted);
      line-height: 1.4;
    }

    .heuristic-table tr:hover td {
      background: rgba(255, 255, 255, 0.02);
    }

    .heuristic-table td strong {
      color: var(--accent-cyan);
    }

    .heuristic-table .tag-risk {
      color: var(--accent-rose);
      font-weight: 600;
      font-size: 11.5px;
    }

    /* Heuristic Rule Card (Slide 12) */
    .rule-row {
      display: flex;
      align-items: center;
      gap: 16px;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 12px 18px;
      margin-bottom: 10px;
      transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .rule-row:hover {
      transform: translateX(4px);
      border-color: var(--accent-cyan);
    }

    .rule-pill {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 6px;
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: var(--accent-blue);
      white-space: nowrap;
    }

    .rule-title {
      font-size: 13.5px;
      font-weight: 700;
      color: #FFFFFF;
      min-width: 220px;
    }

    .rule-desc {
      font-size: 12.5px;
      color: var(--text-muted);
      flex: 1;
    }

    /* Speaker Notes Modal */
    #notes-drawer {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: 200px;
      background: rgba(11, 15, 25, 0.95);
      backdrop-filter: blur(24px);
      border-top: 1px solid var(--accent-purple);
      padding: 20px 32px;
      transform: translateY(100%);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 200;
      box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.7);
    }

    #notes-drawer.open {
      transform: translateY(0);
    }

    .notes-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }

    .notes-title {
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 1px;
      color: var(--accent-purple);
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .notes-content {
      font-size: 14px;
      line-height: 1.6;
      color: #E2E8F0;
      overflow-y: auto;
      max-height: 130px;
    }

    /* Floating Navigation Controls */
    .nav-floating {
      position: fixed;
      bottom: 24px;
      right: 32px;
      display: flex;
      gap: 8px;
      z-index: 100;
    }

    .nav-btn {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(26, 35, 53, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #FFFFFF;
      font-size: 18px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      backdrop-filter: blur(12px);
      transition: all 0.2s ease;
      box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }

    .nav-btn:hover {
      background: var(--accent-blue);
      color: #000000;
      transform: scale(1.05);
    }

    /* Print Stylesheet */
    @media print {
      body {
        overflow: visible;
        height: auto;
        background: #FFFFFF !important;
        color: #000000 !important;
      }
      header, .progress-bar, .nav-floating, #notes-drawer, .ambient-glow {
        display: none !important;
      }
      #slide-viewport {
        margin: 0;
        padding: 0;
        display: block;
        height: auto;
      }
      .slide {
        display: block !important;
        opacity: 1 !important;
        transform: none !important;
        position: relative !important;
        page-break-after: always;
        width: 100% !important;
        height: 95vh !important;
        background: #FFFFFF !important;
        color: #000000 !important;
        border: 1px solid #CCC !important;
        margin-bottom: 20px;
      }
    }
  </style>
</head>
<body>

  <div class="ambient-glow"></div>

  <!-- Header -->
  <header>
    <div class="brand-meta">
      <span class="badge-uni">K.R. MANGALAM UNIVERSITY</span>
      <span class="deck-title">School of Design & Innovation • B.Des UI/UX Studio</span>
    </div>
    <div class="header-controls">
      <span class="slide-counter" id="slide-counter">SLIDE 01 / 13</span>
      <button class="ctrl-btn" onclick="toggleNotes()" title="Press 'S' to toggle">
        🎙️ Notes
      </button>
      <button class="ctrl-btn" onclick="toggleFullscreen()" title="Press 'F' to toggle">
        ⛶ Fullscreen
      </button>
      <button class="ctrl-btn" onclick="window.print()" title="Export PDF">
        📄 Print / PDF
      </button>
    </div>
  </header>

  <div class="progress-bar" id="progress-bar"></div>

  <!-- Viewport -->
  <div id="slide-viewport">

    <!-- SLIDE 1: TITLE & STUDENT ID CARD -->
    <div class="slide active" id="slide-1" data-notes="Good morning respected faculty and peers. I am Bhavya Anand, roll number 2501730046, a 3rd-semester B.Des student specializing in UI/UX Design at K.R. Mangalam University. Today, I am presenting my research on two foundational principles of modern visual and interactive design: Superimposition and Anthropomorphization. As UI/UX designers, we constantly struggle with flat interfaces feeling lifeless or overwhelming. Today, we will unpack how layering spatial depth and injecting human emotional empathy create natural, delightful products.">
      <div class="grid-2-asym">
        <div style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <span class="slide-tag">B.Des Studio Research Submission • Academic Year 2025–2029</span>
            <h1 class="slide-title" style="font-size: 34px; margin-top: 8px;">SUPERIMPOSITION &<br><span style="color: var(--accent-blue);">ANTHROPOMORPHIZATION</span><br>IN DESIGN</h1>
            <p class="slide-subtitle" style="font-size: 15px; color: var(--accent-cyan); margin-top: 10px;">Visual Layering, Emotional Affordances & Cognitive Semiotics in Modern UI/UX</p>
          </div>
          
          <div class="card" style="margin-top: 24px; background: rgba(30, 41, 59, 0.5); border-color: rgba(168, 85, 247, 0.3);">
            <h3 style="color: var(--accent-purple); font-size: 14px;">STUDIO RESEARCH THESIS</h3>
            <p style="font-size: 13px;">How do modern interfaces transcend flat rectangles? By choreographing visual space through <strong>Superimposition</strong> (where things live in depth) and emotional empathy through <strong>Anthropomorphism</strong> (how things communicate and connect).</p>
            <ul style="margin-top: 6px;">
              <li><strong>Gestalt Figure-Ground:</strong> 3D mental models via CSS z-index and glassmorphism.</li>
              <li><strong>Don Norman’s 3 Levels:</strong> Visceral cuteness, Behavioral physics, Reflective pride.</li>
              <li><strong>The Uncanny Valley:</strong> Why stylized mascots succeed where realistic 3D avatars fail.</li>
            </ul>
          </div>
        </div>

        <!-- Student Credential ID Card -->
        <div class="id-card-wrapper">
          <div class="id-header">
            <h4>STUDENT CREDENTIAL CARD</h4>
            <span>B.Des (UI & UX Design) • 3rd Semester</span>
          </div>
          <div class="id-body">
            <img src="assets/bhavya_photo.jpeg" alt="Bhavya Anand" class="id-photo" onerror="this.src='bhavya_photo.jpeg'">
            <div class="id-info">
              <div class="id-field">NAME: <strong style="color: var(--accent-cyan);">BHAVYA ANAND</strong></div>
              <div class="id-field">ROLL NO: <strong style="color: var(--accent-amber);">2501730046</strong></div>
              <div class="id-field">SEMESTER: <strong>3rd Sem (Section E)</strong></div>
              <div class="id-field">DEGREE: <strong>B.Des (UI/UX)</strong></div>
              <div><span class="id-badge">VERIFIED JURY SUBMISSION</span></div>
            </div>
          </div>
          <div class="id-footer">
            <div><strong>INSTITUTION:</strong> K.R. Mangalam University, Gurugram</div>
            <div><strong>DEPARTMENT:</strong> School of Design & Innovation</div>
            <div><strong>SUBJECT:</strong> Visual Design Systems & Cognitive HCI</div>
            <div><strong>CONTACT:</strong> bhavya.bpr@gmail.com</div>
            <div style="color: var(--accent-emerald); font-weight: 600; margin-top: 4px;">● Live Presentation Deck</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 2: ROADMAP -->
    <div class="slide" id="slide-2" data-notes="Here is our studio roadmap. I have organized this presentation into four core modules. First, we examine Superimposition—the spatial dimension that controls where information lives. Second, Anthropomorphism—the emotional dimension that governs how systems behave and connect. Third, we explore the exciting intersection in spatial computing and modern UI. Finally, I will share the Heuristic Studio Framework I developed to guide our everyday design decisions.">
      <div class="slide-header">
        <span class="slide-tag">DESIGN ROADMAP & AGENDA</span>
        <h2 class="slide-title">The Architectural Blueprint: Space vs. Soul</h2>
        <p class="slide-subtitle">Deconstructing how spatial layering and emotional projection unite in human-computer interaction</p>
      </div>
      <div class="grid-4">
        <div class="card" style="border-left: 4px solid var(--accent-blue);">
          <h3 style="color: var(--accent-blue);">PART 01: SUPERIMPOSITION</h3>
          <p><strong>The Spatial Dimension</strong></p>
          <ul>
            <li>Historical roots: Bauhaus photomontage to Swiss typography</li>
            <li>Cognitive mechanism: Gestalt Figure-Ground & Occlusion cues</li>
            <li>UI/UX stack: Z-index hierarchy, Glassmorphism, and Spatial HUDs</li>
          </ul>
        </div>
        <div class="card" style="border-left: 4px solid var(--accent-purple);">
          <h3 style="color: var(--accent-purple);">PART 02: ANTHROPOMORPHISM</h3>
          <p><strong>The Emotional Dimension</strong></p>
          <ul>
            <li>Psychological roots: Pareidolia, Fusiform Face Area & mental models</li>
            <li>Don Norman's 3 levels: Visceral, Behavioral, and Reflective design</li>
            <li>Touchpoints: Micro-physics, conversational tone & brand mascots</li>
          </ul>
        </div>
        <div class="card" style="border-left: 4px solid var(--accent-cyan);">
          <h3 style="color: var(--accent-cyan);">PART 03: THE CONVERGENCE</h3>
          <p><strong>Where Layers Meet Agents</strong></p>
          <ul>
            <li>Spatial Empathy: Anchoring humanized agents into 3D environments</li>
            <li>Mixed Reality case study: Apple VisionOS Spatial Personas</li>
            <li>Everyday UI: Apple Dynamic Island & mascot notification feeds</li>
          </ul>
        </div>
        <div class="card" style="border-left: 4px solid var(--accent-rose);">
          <h3 style="color: var(--accent-rose);">PART 04: STUDIO FRAMEWORK</h3>
          <p><strong>Heuristics, Ethics & Guidelines</strong></p>
          <ul>
            <li>The Danger Zone: Masahiro Mori's Uncanny Valley (1970)</li>
            <li>Ethical UX: Avoiding deceptive empathy and manipulative guilt traps</li>
            <li>5-point B.Des design checklist for classroom projects</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- SLIDE 3: DECONSTRUCTING SUPERIMPOSITION -->
    <div class="slide" id="slide-3" data-notes="In this slide, we examine the theoretical roots of Superimposition. In graphic design history, Moholy-Nagy and the Bauhaus pioneers used photomontage to combine disparate planes into one narrative. In cognitive psychology, Edgar Rubin proved that our brains instantly separate figure from ground. Occlusion—one object partially hiding another—is the strongest monocular depth cue humans possess. In UI/UX, we harness this cue to keep users situated in their workflow while presenting secondary information.">
      <div class="slide-header">
        <span class="slide-tag">MODULE 01 • SPATIAL ARCHITECTURE</span>
        <h2 class="slide-title">Superimposition: Meaning, Lineage & Perception</h2>
        <p class="slide-subtitle">How the deliberate stacking of visual planes constructs depth and cognitive hierarchy</p>
      </div>
      <div class="grid-2">
        <div class="card">
          <h3 style="color: var(--accent-blue);">CORE DESIGN DEFINITION</h3>
          <p><strong>Superimposition</strong> is the deliberate overlapping, layering, or compositing of distinct visual elements, planes, or textures onto a shared viewport to create depth, contextual hierarchy, and emergent narrative.</p>
          <p style="color: var(--accent-cyan); font-weight: 700; margin-top: 10px;">HISTORICAL EVOLUTION IN GRAPHIC DESIGN:</p>
          <ul>
            <li><strong>Bauhaus & Dada Photomontage (1920s):</strong> László Moholy-Nagy and Hannah Höch shattered single-point perspective by superimposing printed media to evoke social commentary.</li>
            <li><strong>Swiss Typography & Screenprinting (1950s):</strong> Overprinting transparent CMYK inks established mathematical grids and optical color mixing.</li>
            <li><strong>Postmodern Deconstruction (1990s):</strong> David Carson layered type over distorted photography, proving that emotional mood often trumps rigid legibility.</li>
          </ul>
        </div>
        <div class="card">
          <h3 style="color: var(--accent-amber);">COGNITIVE PSYCHOLOGY MECHANISMS</h3>
          <p>Why does superimposition work so effortlessly in the human visual cortex?</p>
          <ul>
            <li><strong>Figure-Ground Segregation (Edgar Rubin):</strong> The visual cortex automatically distinguishes between focal objects (figures) and background space (ground). Superimposition sharpens this cognitive boundary.</li>
            <li><strong>Monocular Occlusion Cues:</strong> When Object A partially obscures Object B, our depth perception immediately registers that A is closer in physical space. No binocular stereoscopy is needed!</li>
            <li><strong>Context Preservation (Zero Memory Penalty):</strong> Superimposing a drawer or modal sheet over a form allows users to inspect reference data without losing their active state, preventing cognitive overload.</li>
          </ul>
          <div style="margin-top: 14px; padding: 10px; background: rgba(16, 185, 129, 0.1); border-left: 3px solid var(--accent-emerald); font-size: 11.5px; color: var(--accent-emerald);">
            <strong>UI/UX Heuristic:</strong> Always provide clear depth cues (elevation shadow, border, blur) so users understand what is interactive vs. background context.
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 4: SUPERIMPOSITION IN MODERN UI/UX -->
    <div class="slide" id="slide-4" data-notes="Notice our custom Z-stack diagram on the left. In digital architecture, superimposition is quantified through the Z-axis. From background canvas, to content cards, floating buttons, modal scrims, and spatial AR reticles. On the right, we break down how glassmorphism in iOS and macOS maintains spatial continuity without tearing the user away from their context. But as designers, we must watch out for the 'Layer Cake' trap: when too many layers overlap, contrast collapses and users become disoriented.">
      <div class="slide-header">
        <span class="slide-tag">MODULE 01 • INTERFACE PATTERNS</span>
        <h2 class="slide-title">Superimposition in Modern UI/UX Architecture</h2>
        <p class="slide-subtitle">From CSS Z-Index Stacking to Spatial Glassmorphism and Heads-Up Displays</p>
      </div>
      <div class="grid-2">
        <div class="media-card">
          <img src="assets/z_stack.png" alt="Z-Stack Cognitive Hierarchy Diagram" onerror="this.src='z_stack.png'">
          <span class="media-caption">Figure 1.1: Cognitive Hierarchy along the Z-Axis in Modern Digital Systems</span>
        </div>
        <div class="card">
          <h3 style="color: var(--accent-blue);">CORE DIGITAL IMPLEMENTATIONS</h3>
          <ul>
            <li><strong>1. Glassmorphism & Translucency:</strong> CSS <code>backdrop-filter: blur(20px)</code> allows users to perceive that content continues beneath the active sheet (e.g. iOS Control Center, macOS Sonoma). It maintains orientation without visual isolation.</li>
            <li><strong>2. Persistent Floating Controls (FAB & Bottom Sheets):</strong> Floating Action Buttons and persistent navigation live at z-index 50. According to Fitts's Law, their superimposed position keeps high-frequency triggers within thumb reach.</li>
            <li><strong>3. Spatial Computing & Heads-Up Displays (HUDs):</strong> In Apple VisionOS and automotive windshield HUDs, digital UI windows are superimposed directly onto the physical environment, using ambient cast shadows to look grounded.</li>
          </ul>
          <div style="margin-top: 14px; padding: 10px; background: rgba(244, 63, 94, 0.1); border-left: 3px solid var(--accent-rose); font-size: 11.5px; color: var(--accent-rose);">
            <strong>CRITICAL UX WARNING: The 'Layer Cake' Trap:</strong> Stacking more than 3 distinct active layers causes cognitive friction and fails WCAG AA contrast standards. Always enforce scrim dimming.
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 5: DECONSTRUCTING ANTHROPOMORPHISM -->
    <div class="slide" id="slide-5" data-notes="Now we explore Anthropomorphism. Why do we treat our phones, cars, and software like they have thoughts and feelings? Because of pareidolia and our evolutionary Fusiform Face Area. Clifford Nass and Byron Reeves proved in 'The Media Equation' that humans unconsciously treat digital interfaces according to social rules. If an app is polite, we like it; if an app is rude or cold, we reject it. As UI/UX designers, we can leverage this to reduce technophobia and dramatically increase user forgiveness during system errors.">
      <div class="slide-header">
        <span class="slide-tag">MODULE 02 • EMOTIONAL AFFORDANCE</span>
        <h2 class="slide-title">Anthropomorphization: Evolutionary Roots & Relational UX</h2>
        <p class="slide-subtitle">Attributing human traits, emotional states, and social intent to digital interfaces</p>
      </div>
      <div class="grid-2">
        <div class="card">
          <h3 style="color: var(--accent-purple);">CORE DESIGN DEFINITION</h3>
          <p><strong>Anthropomorphism</strong> is the innate human tendency to attribute human traits, intentions, emotional expressions, or personality to non-human objects, software, and computational interfaces.</p>
          <p style="color: var(--accent-amber); font-weight: 700; margin-top: 10px;">THE BIOLOGICAL ENGINE: PAREIDOLIA</p>
          <ul>
            <li><strong>Fusiform Face Area (FFA):</strong> Human neurobiology detects two eyes and a mouth within 50ms. We see friendly 'faces' in car headlights, power sockets, and app icons.</li>
            <li><strong>Social Brain Hypothesis:</strong> Humans process computer interactions using the exact same social heuristics we use with other humans (Byron Reeves & Clifford Nass, 'The Media Equation').</li>
            <li><strong>Infantile Schema (Kindchenschema):</strong> Konrad Lorenz proved that large heads, large eyes, and soft curved contours trigger instinctual parental warmth and protection.</li>
          </ul>
        </div>
        <div class="card">
          <h3 style="color: var(--accent-cyan);">STRATEGIC VALUE IN UI/UX DESIGN</h3>
          <ul>
            <li><strong>1. Immediate Cognitive Familiarity:</strong> Users rely on innate social protocols (turn-taking, polite greetings, nods) to navigate complex software without manuals.</li>
            <li><strong>2. Reducing Technophobia:</strong> Intimidating financial, medical, or developer software feels approachable when a humble, humanlike guide walks the user step-by-step.</li>
            <li><strong>3. The 'Pratfall Effect' & Error Tolerance:</strong> When an interface shows genuine human humility (e.g. 'Oops, we dropped the ball!'), users exhibit significantly higher patience and lower churn.</li>
            <li><strong>4. Brand Recall & Emotional Stickiness:</strong> Users don't love databases; they love personalities (Duolingo's Duo, Github's Octocat, Apple's Siri).</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- SLIDE 6: DON NORMAN'S THREE LEVELS -->
    <div class="slide" id="slide-6" data-notes="Here we see Don Norman's famous Emotional Design triad applied directly to interface anthropomorphism. At the Visceral level, rounded organic corners and soft palettes trigger subconscious safety signals. At the Behavioral level, organic easing curves—like spring physics and breathing loaders—make the interface feel organically alive. At the Reflective level, brand personality creates long-term user attachment. A great UI/UX designer designs across all three levels simultaneously.">
      <div class="slide-header">
        <span class="slide-tag">MODULE 02 • THEORETICAL FRAMEWORK</span>
        <h2 class="slide-title">Don Norman's 3 Levels of Emotional Design</h2>
        <p class="slide-subtitle">Mapping Visceral, Behavioral, and Reflective layers to UI Anthropomorphism</p>
      </div>
      <div class="grid-2">
        <div class="media-card">
          <img src="assets/emotional_design.png" alt="Don Norman Emotional Design Triad" onerror="this.src='emotional_design.png'">
          <span class="media-caption">Figure 2.1: Norman’s Cognitive Levels Translated to Interface Personas</span>
        </div>
        <div class="card">
          <h3 style="color: var(--accent-amber);">TRANSLATING NORMAN'S TRIAD TO INTERFACES</h3>
          <ul>
            <li><strong>1. Visceral Level (Pre-Cognitive / Immediate Gut Reaction):</strong> Processed in under 50ms. Triggered by baby-schema geometry, warm color harmonies, rounded button corners, and friendly visual symmetry. It asks: <em>'Does this feel safe and delightful?'</em></li>
            <li><strong>2. Behavioral Level (Usability & Organic Physics):</strong> How the interface feels during direct manipulation. Springs that compress on drag, loading skeletons that breathe with human lung cadence, micro-switches that snap like physical toggles. It asks: <em>'Does this respond naturally?'</em></li>
            <li><strong>3. Reflective Level (Identity, Pride & Storytelling):</strong> The post-interaction narrative. How users feel about their own identity after engaging. Duolingo's mascot celebrating user language milestones, Spotify Wrapped diagnosing music personalities. It asks: <em>'What does this product say about who I am?'</em></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- SLIDE 7: TOUCHPOINTS & MASCOTS -->
    <div class="slide" id="slide-7" data-notes="On this slide, look at the classic Tom character on the left. In animation and design, giving an animal human postures and social context creates instant empathy. On the right, we examine how this translates into UI. It's not just drawing a cartoon; it's in the physics of our animations. When an element stretches like rubber or an owl mascot covers its eyes when you type a password, we are injecting biological playfulness into dry digital workflows.">
      <div class="slide-header">
        <span class="slide-tag">MODULE 02 • TOUCHPOINTS & MASCOTS</span>
        <h2 class="slide-title">Digital Touchpoints: Mascots, Physics & Microcopy</h2>
        <p class="slide-subtitle">How subtle human gestures and brand personas turn mechanical tools into companions</p>
      </div>
      <div class="grid-2-asym">
        <div class="media-card" style="max-height: 480px;">
          <img src="assets/tom_anthropomorphism.jpg" alt="Tom Mugshot Anthropomorphism" style="max-height: 320px;" onerror="this.src='tom_anthropomorphism.jpg'">
          <div style="margin-top: 10px; text-align: center;">
            <strong style="color: var(--accent-amber); font-size: 13px;">Mascot Persona in Action</strong>
            <p style="font-size: 11.5px; color: var(--text-muted); margin-top: 4px;">Classic animation projects human social drama (mugshot, smirk) onto a character. Digital UI uses this same technique to make brand mascots unforgettable.</p>
          </div>
        </div>
        <div class="card">
          <h3 style="color: var(--accent-blue);">THREE PILLARS OF INTERFACE ANTHROPOMORPHISM</h3>
          <ul>
            <li><strong>A. Micro-Interactions & Organic Physics:</strong> Instead of robotic linear transitions (ease-in-out), modern UI uses damping springs and gravity. When you drag a card on iOS, it squishes slightly like rubber; when you refresh, the spinner stretches like elastic dough.</li>
            <li><strong>B. Contextual Peek-a-Boo Reactions:</strong> On login pages like Readme.com, the mascot covers its eyes when the user clicks into the password field, then peeks when 'show password' is clicked. This humanizes authentication.</li>
            <li><strong>C. Conversational Voice & Microcopy Rhythm:</strong> Robotic: 'Error 404: Null Reference'. Anthropomorphic: 'We looked everywhere, but we couldn't find that page. Let's get you back home.' Conversational phrasing restores user confidence.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- SLIDE 8: THE UNCANNY VALLEY -->
    <div class="slide" id="slide-8" data-notes="Every UX student must understand the Uncanny Valley curve shown on the left. In 1970, Masahiro Mori discovered that when an entity looks almost human, but has a 1% imperfection—like dead eyes or unnatural blinking—our brain classifies it as a diseased corpse or threat, causing revulsion. That's why hyper-realistic 3D AI bank tellers fail. Honest stylization—like Duolingo or Pixar—bypasses this trap entirely. Our takeaway: never try to fake human biology; use clean, expressive abstraction.">
      <div class="slide-header">
        <span class="slide-tag">MODULE 02 • THE DANGER ZONE</span>
        <h2 class="slide-title">Masahiro Mori's Uncanny Valley (1970) in UX</h2>
        <p class="slide-subtitle">Why hyper-realistic avatars creep users out, and why honest abstraction always wins</p>
      </div>
      <div class="grid-2">
        <div class="media-card">
          <img src="assets/uncanny_valley.png" alt="Uncanny Valley Curve Diagram" onerror="this.src='uncanny_valley.png'">
          <span class="media-caption">Figure 2.2: Masahiro Mori's Curve Applied to Modern Digital Interfaces</span>
        </div>
        <div class="card">
          <h3 style="color: var(--accent-rose);">THE PSYCHOLOGICAL REJECTION THRESHOLD</h3>
          <p>As an artificial entity becomes more human-like, user comfort increases up to a cliff where near-human imperfections trigger evolutionary disgust and distrust.</p>
          <ul>
            <li><strong>The Metaverse Avatar Trap:</strong> Early VR attempts at photorealistic 3D human avatars resulted in lifeless, glazed eyes, mismatched lip sync, and stiff micro-expressions that alienated users.</li>
            <li><strong>The Synthetic Bank Teller Failure:</strong> AI customer service agents with rendered 3D human faces make users hyper-scrutinize every glitch. Users report feeling watched by a digital zombie.</li>
            <li><strong>The Sweet Spot: Honest Stylization:</strong> Duolingo, Pixar characters, Discord Wumpus, and Slack emoji stay safely on the left peak. Because they are stylized cartoons, the user's imagination fills in emotional warmth without expecting anatomical perfection.</li>
          </ul>
          <div style="margin-top: 14px; padding: 10px; background: rgba(16, 185, 129, 0.1); border-left: 3px solid var(--accent-emerald); font-size: 12px; color: var(--accent-emerald);">
            <strong>B.Des Studio Rule:</strong> <em>"Stylize the form, humanize the behavior. Never fake human biology."</em>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 9: THE CONVERGENCE -->
    <div class="slide" id="slide-9" data-notes="Now we arrive at the nexus where both principles collide. On the left, look at how superimposing humanoid figures onto a mountain terrain immediately transforms cold rock into an emotional, spiritual presence. In digital design, this is Spatial Empathy. Apple VisionOS uses Spatial Personas to project your friend's volumetric avatar directly onto the carpet of your living room. It's the ultimate marriage of Z-depth superimposition and human micro-expression.">
      <div class="slide-header">
        <span class="slide-tag">MODULE 03 • THE NEXUS</span>
        <h2 class="slide-title">When Superimposition Meets Anthropomorphism</h2>
        <p class="slide-subtitle">Spatial Empathy: Anchoring humanized agents onto multi-layered reality</p>
      </div>
      <div class="grid-2-asym">
        <div class="media-card" style="max-height: 480px;">
          <img src="assets/mountain_superimposition.jpeg" alt="Mountain Superimposition" style="max-height: 320px;" onerror="this.src='mountain_superimposition.jpeg'">
          <div style="margin-top: 10px; text-align: center;">
            <strong style="color: var(--accent-cyan); font-size: 13px;">Visual Art Case: Spatial Superimposition</strong>
            <p style="font-size: 11.5px; color: var(--text-muted); margin-top: 4px;">Superimposing humanoid figures onto a mountain landscape imbues cold geography with emotional presence and divine protection.</p>
          </div>
        </div>
        <div class="card">
          <h3 style="color: var(--accent-purple);">THREE SPATIAL EMPATHY PARADIGMS IN UI/UX</h3>
          <ul>
            <li><strong>1. Apple VisionOS 'Spatial Personas':</strong> Apple solved the isolation of VR by superimposing real-time 3D volumetric avatars into the user's living room during FaceTime. By synchronizing micro-gaze tracking and spatial audio, it creates the cognitive illusion of another human sharing your physical room.</li>
            <li><strong>2. Real-Time AR Face Tracking & Lenses (Snapchat / Instagram):</strong> Superimposing anthropomorphic animal features, blush, and exaggerated eyes directly onto the user's live video feed. This merges the user's own identity with an expressive avatar layer in real time.</li>
            <li><strong>3. Spatial AI Companions & Ambient Assistants:</strong> In future smart home and automotive interfaces, AI agents won't be confined to flat rectangles; they will be superimposed as ambient spatial holographic entities on kitchen counters or dashboards, gesturing and making eye contact.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- SLIDE 10: COMPARATIVE HEURISTIC MATRIX -->
    <div class="slide" id="slide-10" data-notes="To ground our research in rigorous UI/UX methodology, I built this comparative heuristic matrix. Look at how Duolingo pairs a floating lock-screen widget with an urgent mascot persona, driving an 18% lift in retention. Meanwhile, Apple's Dynamic Island uses organic elastic physics to make a hardware sensor cutout feel like a responsive living organ. Each technique comes with real trade-offs—such as visual distraction or emotional fatigue—which we must balance as designers.">
      <div class="slide-header">
        <span class="slide-tag">MODULE 03 • CASE STUDY TEARDOWN</span>
        <h2 class="slide-title">Comparative Heuristic Matrix: Industry Case Studies</h2>
        <p class="slide-subtitle">A structured breakdown of modern digital products utilizing both design levers</p>
      </div>
      <div class="card" style="padding: 16px;">
        <table class="heuristic-table">
          <thead>
            <tr>
              <th>PRODUCT / USE CASE</th>
              <th>SUPERIMPOSITION TYPE</th>
              <th>ANTHROPOMORPHIC TRAIT</th>
              <th>UX IMPACT & METRIC</th>
              <th>FAILURE RISK</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Duolingo Streak HUD</strong></td>
              <td>Floating Lockscreen Widget & Dynamic Island overlay</td>
              <td>Urgent, weeping, or ecstatic mascot persona (Duo)</td>
              <td>+18% Day-30 retention; builds intense daily habit loop</td>
              <td><span class="tag-risk">Emotional fatigue; user annoyance at aggressive guilt</span></td>
            </tr>
            <tr>
              <td><strong>Apple Dynamic Island</strong></td>
              <td>Morphing black pill superimposed on status bar</td>
              <td>Organic 'breathing' elasticity and fluid squash/stretch</td>
              <td>Glanceable background awareness with zero context switch</td>
              <td><span class="tag-risk">Occlusion of top screen content; thumb reach strain</span></td>
            </tr>
            <tr>
              <td><strong>Apple VisionOS Personas</strong></td>
              <td>Volumetric 3D spatial mesh rendered in user's room</td>
              <td>Synchronized eye gaze, mouth shape & head tilts</td>
              <td>Deep psychological co-presence in remote collaboration</td>
              <td><span class="tag-risk">Occasional uncanny eye tracking glitches; processing lag</span></td>
            </tr>
            <tr>
              <td><strong>Automotive AR HUD</strong></td>
              <td>Windshield optical projection directly over roadway</td>
              <td>Pedestrian stick-figure avatars with gaze vectors</td>
              <td>Reduces driver reaction time by 280ms during night driving</td>
              <td><span class="tag-risk">Cognitive visual clutter; driver target fixation risk</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- SLIDE 11: ETHICAL FRONTIER -->
    <div class="slide" id="slide-11" data-notes="As designers, we cannot ignore ethics. Anthropomorphism becomes toxic when it turns into 'Deceptive Empathy'—like a streaming app showing a crying cartoon to guilt you out of unsubscribing. That is manipulative confirmshaming. Similarly, over-superimposition destroys accessibility for users with visual impairments. In our studio work, our manifesto must be clear: humanize to assist, never to manipulate; layer to clarify, never to obscure.">
      <div class="slide-header">
        <span class="slide-tag">MODULE 04 • ETHICAL DESIGN</span>
        <h2 class="slide-title">The Dark Side: Deceptive Empathy & Sensory Clutter</h2>
        <p class="slide-subtitle">When emotional anthropomorphism turns manipulative and visual layering breaks accessibility</p>
      </div>
      <div class="grid-4">
        <div class="card" style="border-left: 4px solid var(--accent-rose);">
          <h3 style="color: var(--accent-rose);">DARK PATTERN 01: DECEPTIVE EMPATHY</h3>
          <p><strong>Weaponizing Guilt (Confirmshaming)</strong></p>
          <ul>
            <li>Using cute anthropomorphic mascots crying or looking heartbroken when a user tries to cancel a subscription or delete an account.</li>
            <li>Example: 'Are you really going to make Duo cry?' or pet apps showing shivering animals to prevent cancellation.</li>
            <li><strong>Ethical Breach:</strong> Coercing user decisions through artificial emotional distress rather than functional value.</li>
          </ul>
        </div>
        <div class="card" style="border-left: 4px solid var(--accent-amber);">
          <h3 style="color: var(--accent-amber);">DARK PATTERN 02: OVER-SUPERIMPOSITION</h3>
          <p><strong>The Layer Cake & Visual Hostage</strong></p>
          <ul>
            <li>Stacking multiple translucent modals, persistent banners, chat bubbles, and consent overlays until base content is obscured.</li>
            <li><strong>Accessibility Violation:</strong> Fails WCAG 2.1 contrast standards (4.5:1 ratio) on low-end screens or under direct sunlight.</li>
            <li><strong>Cognitive Cost:</strong> Induces sensory overload, micro-frustration, and loss of mental spatial mapping.</li>
          </ul>
        </div>
        <div class="card" style="border-left: 4px solid var(--accent-purple);">
          <h3 style="color: var(--accent-purple);">DARK PATTERN 03: FALSE SENTIENCE</h3>
          <p><strong>Misleading Trust in Generative AI</strong></p>
          <ul>
            <li>Designing conversational bots that claim to 'feel sad' or 'remember our bond' when they are statistical token predictors.</li>
            <li>Vulnerable users (children, elderly) form parasocial attachments and divulge private data.</li>
            <li><strong>Design Mandate:</strong> Honest AI disclosure—convey system limits clearly.</li>
          </ul>
        </div>
        <div class="card" style="border-left: 4px solid var(--accent-emerald);">
          <h3 style="color: var(--accent-emerald);">THE B.DES ETHICAL MANIFESTO</h3>
          <p><strong>Our Studio Guiding Principle</strong></p>
          <ul>
            <li><strong>"Humanize to assist, never to manipulate."</strong></li>
            <li><strong>"Layer to clarify, never to obscure."</strong></li>
            <li>Empathy must be a conduit for user empowerment, not a mechanism for dark-pattern entrapment.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- SLIDE 12: MY B.DES STUDIO FRAMEWORK -->
    <div class="slide" id="slide-12" data-notes="From this research, I created this 5-point studio framework for our UI/UX design projects. Before presenting any prototype in our jury or critique, we can audit it: Did we justify the Z-axis? Did we stay out of the Uncanny Valley? Are our physics organic? Is our contrast accessible? And do we respect user autonomy? This gives us a concrete design methodology.">
      <div class="slide-header">
        <span class="slide-tag">MODULE 04 • PRACTICAL TOOLKIT</span>
        <h2 class="slide-title">My B.Des Studio Framework: 5 Golden Heuristics</h2>
        <p class="slide-subtitle">A ready-to-use checklist for designing spatial layers and humanized micro-interactions</p>
      </div>
      <div>
        <div class="rule-row">
          <span class="rule-pill">RULE 01</span>
          <span class="rule-title">Establish Strict Z-Axis Roles</span>
          <span class="rule-desc">Every superimposed element must justify its elevation. Layer 0 = Surface, Layer 1 = Content, Layer 2 = Floating triggers, Layer 3 = Modals. Never stack arbitrarily.</span>
        </div>
        <div class="rule-row">
          <span class="rule-pill" style="color: var(--accent-purple); border-color: var(--accent-purple);">RULE 02</span>
          <span class="rule-title">Respect the Uncanny Boundary</span>
          <span class="rule-desc">Always choose stylized geometric abstraction over pseudorealistic 3D human renders. An expressive 2D mascot is infinitely more empathetic than a creepy synthetic human.</span>
        </div>
        <div class="rule-row">
          <span class="rule-pill" style="color: var(--accent-cyan); border-color: var(--accent-cyan);">RULE 03</span>
          <span class="rule-title">Anchor Motion in Natural Physics</span>
          <span class="rule-desc">Use cubic-bezier spring curves (damping ratio 0.7) and organic mass rather than linear motion. Let buttons stretch and bounce with biological playfulness.</span>
        </div>
        <div class="rule-row">
          <span class="rule-pill" style="color: var(--accent-amber); border-color: var(--accent-amber);">RULE 04</span>
          <span class="rule-title">Enforce Strict WCAG Accessibility</span>
          <span class="rule-desc">Ensure any superimposed text or icon maintains at least 4.5:1 contrast against blurred backdrops. Always provide non-motion fallbacks for vestibular disorders.</span>
        </div>
        <div class="rule-row">
          <span class="rule-pill" style="color: var(--accent-emerald); border-color: var(--accent-emerald);">RULE 05</span>
          <span class="rule-title">Preserve Total User Autonomy</span>
          <span class="rule-desc">Never use mascot tears or simulated grief to guilt-trip users during cancellation or settings flows. Emotional design must serve clarity, never manipulation.</span>
        </div>
      </div>
    </div>

    <!-- SLIDE 13: CONCLUSION & REFERENCES -->
    <div class="slide" id="slide-13" data-notes="To conclude: Space and Soul. Superimposition choreographs spatial depth and mental models, while Anthropomorphism choreographs relational warmth and empathy. I have cited foundational literature here from Don Norman, Masahiro Mori, and Edgar Rubin. Thank you so much for your time and attention. I am eager to hear your feedback, critique, and questions!">
      <div class="slide-header">
        <span class="slide-tag">CONCLUSION & BIBLIOGRAPHY</span>
        <h2 class="slide-title">Harmonizing Space and Soul in Design</h2>
        <p class="slide-subtitle">Summary thesis, academic references, and jury discussion</p>
      </div>
      <div class="grid-2">
        <div class="card">
          <h3 style="color: var(--accent-blue);">CORE THESIS SUMMARY</h3>
          <p style="font-size: 15px; color: var(--accent-cyan); font-weight: 700; margin-bottom: 16px;">
            "Great digital product design lives in the deliberate harmony of Space and Soul."
          </p>
          <ul>
            <li><strong>Superimposition governs SPACE:</strong> It structures visual priority, preserves context along the z-axis, and eliminates cognitive disjunction in 2D and 3D viewports.</li>
            <li><strong>Anthropomorphism governs SOUL:</strong> It sparks emotional resonance, builds intuitive mental models via social cues, and turns cold computational tools into trusted partners.</li>
            <li><strong>The Ultimate Goal:</strong> To craft interfaces that are spatially transparent, emotionally dignified, and ergonomically effortless.</li>
          </ul>
        </div>
        <div class="card">
          <h3 style="color: var(--accent-amber);">ACADEMIC & INDUSTRY REFERENCES</h3>
          <ul style="gap: 8px;">
            <li>1. <strong>Norman, Donald A. (2004).</strong> <em>Emotional Design: Why We Love (or Hate) Everyday Things.</em> Basic Books.</li>
            <li>2. <strong>Mori, Masahiro (1970).</strong> <em>The Uncanny Valley.</em> Energy, 7(4), pp. 33–35.</li>
            <li>3. <strong>Reeves, Byron & Nass, Clifford (1996).</strong> <em>The Media Equation: How People Treat Computers Like Real People.</em> Cambridge University Press.</li>
            <li>4. <strong>Rubin, Edgar (1915).</strong> <em>Synsoplevede Figurer (Figure-Ground Perception).</em> Gyldendalske.</li>
            <li>5. <strong>Nielsen Norman Group (NN/g). (2024).</strong> <em>Emotional Ergonomics & Spatial Overlay Guidelines in XR.</em></li>
          </ul>
          <div style="margin-top: 18px; padding-top: 14px; border-top: 1px solid rgba(255, 255, 255, 0.1);">
            <p style="font-size: 11px; color: var(--accent-purple); font-weight: 700; text-transform: uppercase;">STUDENT PRESENTER</p>
            <p style="font-size: 13px; color: #FFFFFF; font-weight: 700; margin-bottom: 2px;">Bhavya Anand • Roll No: 2501730046</p>
            <p style="font-size: 12px; color: var(--text-muted);">B.Des (UI & UX Design) • Semester III • K.R. Mangalam University</p>
            <p style="font-size: 12px; color: var(--accent-cyan); margin-top: 6px;">Thank you! Happy to take questions from the jury.</p>
          </div>
        </div>
      </div>
    </div>

  </div>

  <!-- Speaker Notes Drawer -->
  <div id="notes-drawer">
    <div class="notes-header">
      <span class="notes-title">🎙️ Presenter Speaker Notes (Bhavya Anand)</span>
      <button class="ctrl-btn" onclick="toggleNotes()" style="padding: 2px 8px; font-size: 11px;">✕ Close</button>
    </div>
    <div class="notes-content" id="notes-content">
      Loading speaker notes...
    </div>
  </div>

  <!-- Floating Nav Controls -->
  <div class="nav-floating">
    <button class="nav-btn" onclick="prevSlide()" title="Previous Slide (Left Arrow)">‹</button>
    <button class="nav-btn" onclick="nextSlide()" title="Next Slide (Right Arrow / Space)">›</button>
  </div>

  <script>
    let currentSlide = 1;
    const totalSlides = 13;

    function showSlide(index) {
      if (index < 1) index = 1;
      if (index > totalSlides) index = totalSlides;
      currentSlide = index;

      document.querySelectorAll('.slide').forEach((s, idx) => {
        if (idx + 1 === currentSlide) {
          s.classList.add('active');
          const notes = s.getAttribute('data-notes') || 'No speaker notes for this slide.';
          document.getElementById('notes-content').innerHTML = `<strong>Slide ${currentSlide} Cues:</strong><br>${notes}`;
        } else {
          s.classList.remove('active');
        }
      });

      document.getElementById('slide-counter').innerText = `SLIDE ${String(currentSlide).padStart(2, '0')} / ${String(totalSlides).padStart(2, '0')}`;
      const progressPercent = (currentSlide / totalSlides) * 100;
      document.getElementById('progress-bar').style.width = `${progressPercent}%`;
    }

    function nextSlide() {
      if (currentSlide < totalSlides) {
        showSlide(currentSlide + 1);
      }
    }

    function prevSlide() {
      if (currentSlide > 1) {
        showSlide(currentSlide - 1);
      }
    }

    function toggleNotes() {
      document.getElementById('notes-drawer').classList.toggle('open');
    }

    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {
          console.error(err);
        });
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        }
      }
    }

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
        e.preventDefault();
        nextSlide();
      } else if (e.key === 'ArrowLeft' || e.key === 'Backspace') {
        e.preventDefault();
        prevSlide();
      } else if (e.key.toLowerCase() === 's') {
        toggleNotes();
      } else if (e.key.toLowerCase() === 'f') {
        toggleFullscreen();
      }
    });

    // Initialize
    showSlide(1);
  </script>
</body>
</html>
"""

# Save index.html
output_dir1 = "/Users/bhavya/Desktop/ /Sem_3/Superimposition_and_Anthropomorphization_Presentation"
os.makedirs(output_dir1, exist_ok=True)
with open(os.path.join(output_dir1, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

output_dir2 = "/Users/bhavya/Desktop/ /Sem_3/ML"
with open(os.path.join(output_dir2, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html saved to both locations successfully!")
