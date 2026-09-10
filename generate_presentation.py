import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Initialize Presentation
prs = pptx.Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Color Palette (Dark Mode Studio Aesthetic)
BG_DARK = RGBColor(11, 15, 25)       # Obsidian #0B0F19
CARD_BG = RGBColor(24, 32, 47)       # Deep Slate #18202F
CARD_BG_LIGHT = RGBColor(33, 44, 63) # Elevated Slate #212C3F
CARD_BORDER = RGBColor(51, 65, 85)   # Border Slate #334155
TEXT_MAIN = RGBColor(248, 250, 252)  # White/Off-white #F8FAFC
TEXT_MUTED = RGBColor(148, 163, 184) # Muted Text #94A3B8
TEXT_DIM = RGBColor(100, 116, 139)   # Dim Text #64748B
ACCENT_BLUE = RGBColor(56, 189, 248) # Sky 400 #38BDF8
ACCENT_CYAN = RGBColor(45, 212, 191) # Teal 400 #2DD4BF
ACCENT_PURPLE = RGBColor(168, 85, 247) # Purple 500 #A855F7
ACCENT_ROSE = RGBColor(244, 63, 94)  # Rose 500 #F43F5E
ACCENT_AMBER = RGBColor(245, 158, 11)# Amber 500 #F59E0B
ACCENT_EMERALD = RGBColor(16, 185, 129) # Emerald #10B981

ASSETS_DIR = "/Users/bhavya/Desktop/ /Sem_3/Superimposition_and_Anthropomorphization_Presentation/assets"
PHOTO_PATH = os.path.join(ASSETS_DIR, "bhavya_photo.jpeg")
UNCANNY_PATH = os.path.join(ASSETS_DIR, "uncanny_valley.png")
Z_STACK_PATH = os.path.join(ASSETS_DIR, "z_stack.png")
EMOTIONAL_PATH = os.path.join(ASSETS_DIR, "emotional_design.png")
TOM_PATH = os.path.join(ASSETS_DIR, "tom_anthropomorphism.jpg")
MOUNTAIN_PATH = os.path.join(ASSETS_DIR, "mountain_superimposition.jpeg")

def set_slide_background(slide):
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_DARK
    bg.line.fill.background()
    return bg

def add_header(slide, category, title, subtitle=None):
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.42), Inches(11.5), Inches(0.32))
    tf_c = cat_box.text_frame
    tf_c.word_wrap = True
    tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
    p_c = tf_c.paragraphs[0]
    p_c.text = category.upper()
    p_c.font.size = Pt(9.5)
    p_c.font.bold = True
    p_c.font.color.rgb = ACCENT_BLUE
    p_c.font.name = "Arial"

    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.74), Inches(11.5), Inches(0.55))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(20)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_MAIN
    p_t.font.name = "Arial"

    if subtitle:
        sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.30), Inches(11.5), Inches(0.35))
        tf_s = sub_box.text_frame
        tf_s.word_wrap = True
        tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
        p_s = tf_s.paragraphs[0]
        p_s.text = subtitle
        p_s.font.size = Pt(11)
        p_s.font.color.rgb = TEXT_MUTED
        p_s.font.name = "Arial"

def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=CARD_BORDER):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1)
    else:
        card.line.fill.background()
    return card

def add_speaker_notes(slide, notes_text):
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = notes_text

blank_layout = prs.slide_layouts[6]

# ==========================================
# SLIDE 1: TITLE SLIDE (WITH STUDENT ID CARD)
# ==========================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1)

pill = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.6), Inches(6.2), Inches(0.36))
pill.fill.solid()
pill.fill.fore_color.rgb = CARD_BG_LIGHT
pill.line.color.rgb = ACCENT_BLUE
pill.line.width = Pt(1)
tf_p = pill.text_frame
p_p = tf_p.paragraphs[0]
p_p.text = "  K.R. MANGALAM UNIVERSITY • SCHOOL OF DESIGN & INNOVATION"
p_p.font.size = Pt(9.5)
p_p.font.bold = True
p_p.font.color.rgb = ACCENT_BLUE
p_p.alignment = PP_ALIGN.LEFT

t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.2), Inches(6.8), Inches(2.2))
tf = t_box.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

p1 = tf.paragraphs[0]
p1.text = "SUPERIMPOSITION &\nANTHROPOMORPHIZATION\nIN DESIGN"
p1.font.size = Pt(28)
p1.font.bold = True
p1.font.color.rgb = TEXT_MAIN
p1.font.name = "Arial"

p2 = tf.add_paragraph()
p2.text = "\nVisual Layering, Emotional Affordances & Cognitive Semiotics in Modern UI/UX"
p2.font.size = Pt(13)
p2.font.color.rgb = ACCENT_CYAN
p2.font.name = "Arial"

stmt_card = add_card(s1, Inches(0.8), Inches(3.9), Inches(6.8), Inches(2.8))
s_box = s1.shapes.add_textbox(Inches(1.1), Inches(4.1), Inches(6.2), Inches(2.4))
tf_s = s_box.text_frame
tf_s.word_wrap = True
tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0

ps1 = tf_s.paragraphs[0]
ps1.text = "STUDIO RESEARCH THESIS"
ps1.font.size = Pt(10)
ps1.font.bold = True
ps1.font.color.rgb = ACCENT_PURPLE

ps2 = tf_s.add_paragraph()
ps2.text = "How do digital interfaces transcend flat screens? By orchestrating visual depth through superimposition (where things exist in space) and emotional resonance through anthropomorphism (how things interact and empathize).\n\nKey Focus Areas:"
ps2.font.size = Pt(10.5)
ps2.font.color.rgb = TEXT_MUTED

focus_items = [
    "• Gestalt Figure-Ground & Spatial Z-Stack Architecture",
    "• Don Norman's 3 Levels of Emotional Design & Masahiro Mori's Uncanny Valley",
    "• Spatial Computing (VisionOS), Dynamic Island & Mascot Micro-interactions"
]
for item in focus_items:
    pf = tf_s.add_paragraph()
    pf.text = item
    pf.font.size = Pt(10)
    pf.font.color.rgb = TEXT_MAIN

# RIGHT SIDE: AUTHENTIC STUDENT ID CARD
id_card = add_card(s1, Inches(8.0), Inches(0.8), Inches(4.5), Inches(5.9), bg_color=CARD_BG, border_color=ACCENT_BLUE)

card_top = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(8.0), Inches(0.8), Inches(4.5), Inches(0.8))
card_top.fill.solid()
card_top.fill.fore_color.rgb = CARD_BG_LIGHT
card_top.line.color.rgb = ACCENT_BLUE
card_top.line.width = Pt(1)
tf_ct = card_top.text_frame
pct = tf_ct.paragraphs[0]
pct.text = "STUDENT CREDENTIAL CARD"
pct.font.size = Pt(11)
pct.font.bold = True
pct.font.color.rgb = ACCENT_BLUE
pct.alignment = PP_ALIGN.CENTER
pct2 = tf_ct.add_paragraph()
pct2.text = "B.Des (UI & UX Design) • Academic Year 2025–2029"
pct2.font.size = Pt(8.5)
pct2.font.color.rgb = TEXT_MUTED
pct2.alignment = PP_ALIGN.CENTER

if os.path.exists(PHOTO_PATH):
    s1.shapes.add_picture(PHOTO_PATH, Inches(8.3), Inches(1.8), Inches(1.3), Inches(1.65))

det_box = s1.shapes.add_textbox(Inches(9.8), Inches(1.8), Inches(2.5), Inches(1.7))
tf_d = det_box.text_frame
tf_d.word_wrap = True
tf_d.margin_left = tf_d.margin_top = tf_d.margin_right = tf_d.margin_bottom = 0

def add_field(tf, label, val, color=TEXT_MAIN, bold=False):
    p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
    p.text = f"{label}: "
    p.font.size = Pt(9)
    p.font.bold = True
    p.font.color.rgb = TEXT_MUTED
    run = p.add_run()
    run.text = val
    run.font.bold = bold
    run.font.color.rgb = color

add_field(tf_d, "NAME", "Bhavya Anand", ACCENT_CYAN, True)
add_field(tf_d, "ROLL NO", "2501730046", ACCENT_AMBER, True)
add_field(tf_d, "SEMESTER", "Semester III (Sec E)")
add_field(tf_d, "PROGRAM", "B.Des (UI/UX)")

bot_box = s1.shapes.add_textbox(Inches(8.3), Inches(3.6), Inches(3.9), Inches(2.8))
tf_b = bot_box.text_frame
tf_b.word_wrap = True
tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0

add_field(tf_b, "INSTITUTION", "K.R. Mangalam University, Gurugram")
add_field(tf_b, "DEPARTMENT", "School of Design & Innovation")
add_field(tf_b, "SUBJECT", "Visual Design Systems & Cognitive HCI")
add_field(tf_b, "SUBMISSION DATE", "September 2026")
add_field(tf_b, "CONTACT", "bhavya.bpr@gmail.com")

p_stat = tf_b.add_paragraph()
p_stat.text = "\nSTATUS: VERIFIED STUDENT WORK FOR JURY REVIEW"
p_stat.font.size = Pt(8.5)
p_stat.font.bold = True
p_stat.font.color.rgb = ACCENT_EMERALD

add_speaker_notes(s1, "Good morning respected faculty and peers. I am Bhavya Anand, roll number 2501730046, a 3rd-semester B.Des student specializing in UI/UX Design at K.R. Mangalam University. Today, I am presenting my research on two foundational principles of modern visual and interactive design: Superimposition and Anthropomorphization. As UI/UX designers, we constantly struggle with flat interfaces feeling lifeless or overwhelming. Today, we will unpack how layering spatial depth and injecting human emotional empathy create natural, delightful products.")

# ==========================================
# SLIDE 2: STUDIO ROADMAP
# ==========================================
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2)
add_header(s2, "DESIGN ROADMAP & AGENDA", "The Architectural Blueprint: Space vs. Soul", "Deconstructing how spatial layering and emotional projection unite in human-computer interaction")

cards_data = [
    ("PART 01: SUPERIMPOSITION", "The Spatial Dimension", [
        "• Historical roots: Bauhaus photomontage to Swiss typography",
        "• Cognitive mechanism: Gestalt Figure-Ground & Occlusion",
        "• UI/UX stack: Z-index, Glassmorphism, and Spatial HUDs"
    ], ACCENT_BLUE, Inches(0.8), Inches(1.8)),

    ("PART 02: ANTHROPOMORPHISM", "The Emotional Dimension", [
        "• Psychological roots: Pareidolia and human mental models",
        "• Don Norman's 3 levels: Visceral, Behavioral, Reflective",
        "• Touchpoints: Micro-physics, voice interfaces & mascots"
    ], ACCENT_PURPLE, Inches(6.8), Inches(1.8)),

    ("PART 03: THE CONVERGENCE", "Where Layers Meet Agents", [
        "• Spatial Empathy: Overlaying humanized agents in 3D",
        "• Mixed Reality case study: Apple VisionOS Personas",
        "• Everyday UI: Dynamic Island & mascot notification feeds"
    ], ACCENT_CYAN, Inches(0.8), Inches(4.4)),

    ("PART 04: STUDIO FRAMEWORK", "Heuristics & Ethics", [
        "• The Danger Zone: Masahiro Mori's Uncanny Valley (1970)",
        "• Ethical UX: Avoiding deceptive empathy and guilt traps",
        "• 5-point B.Des design checklist for classroom projects"
    ], ACCENT_ROSE, Inches(6.8), Inches(4.4))
]

for title, sub, items, col, x, y in cards_data:
    add_card(s2, x, y, Inches(5.7), Inches(2.4))
    tb = s2.shapes.add_textbox(x + Inches(0.3), y + Inches(0.25), Inches(5.1), Inches(1.9))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = col
    
    p_sub = tf.add_paragraph()
    p_sub.text = sub
    p_sub.font.size = Pt(13)
    p_sub.font.bold = True
    p_sub.font.color.rgb = TEXT_MAIN
    
    for itm in items:
        pi = tf.add_paragraph()
        pi.text = itm
        pi.font.size = Pt(9.5)
        pi.font.color.rgb = TEXT_MUTED

add_speaker_notes(s2, "Here is our studio roadmap. I have organized this presentation into four core modules. First, we examine Superimposition—the spatial dimension that controls where information lives. Second, Anthropomorphism—the emotional dimension that governs how systems behave and connect. Third, we explore the exciting intersection in spatial computing and modern UI. Finally, I will share the Heuristic Studio Framework I developed to guide our everyday design decisions.")

# ==========================================
# SLIDE 3: DECONSTRUCTING SUPERIMPOSITION
# ==========================================
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3)
add_header(s3, "MODULE 01 • SPATIAL ARCHITECTURE", "Superimposition: Meaning, Lineage & Perception", "How the deliberate stacking of visual planes constructs depth and cognitive hierarchy")

add_card(s3, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
tb_l = s3.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.1), Inches(4.4))
tf_l = tb_l.text_frame
tf_l.word_wrap = True
tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0

p = tf_l.paragraphs[0]
p.text = "CORE DESIGN DEFINITION"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = ACCENT_BLUE

p = tf_l.add_paragraph()
p.text = "Superimposition is the deliberate overlapping, layering, or compositing of distinct visual elements, planes, or textures onto a shared viewport to create depth, contextual hierarchy, and emergent narrative."
p.font.size = Pt(11)
p.font.color.rgb = TEXT_MAIN

p = tf_l.add_paragraph()
p.text = "\nHISTORICAL EVOLUTION IN GRAPHIC DESIGN:"
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = ACCENT_CYAN

history = [
    ("Bauhaus & Dada Photomontage (1920s)", "Artists like László Moholy-Nagy and Hannah Höch used superimposed clippings to break linear perspective and critique industrialization."),
    ("Swiss Typography & Screenprinting (1950s)", "Layering transparent colored inks created geometric optical interactions and rigorous informational grids."),
    ("Postmodern Digital Chaos (1990s)", "David Carson and Ray Gun magazine layered typography over photography to evoke raw emotional expression over strict legibility.")
]
for h_title, h_desc in history:
    p = tf_l.add_paragraph()
    p.text = f"• {h_title}: "
    p.font.size = Pt(9)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    run = p.add_run()
    run.text = h_desc
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED

add_card(s3, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
tb_r = s3.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.1), Inches(4.4))
tf_r = tb_r.text_frame
tf_r.word_wrap = True
tf_r.margin_left = tf_r.margin_top = tf_r.margin_right = tf_r.margin_bottom = 0

p = tf_r.paragraphs[0]
p.text = "COGNITIVE PSYCHOLOGY MECHANISMS"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = ACCENT_AMBER

p = tf_r.add_paragraph()
p.text = "Why does superimposition work so effortlessly in the human brain?"
p.font.size = Pt(11)
p.font.color.rgb = TEXT_MAIN

cog = [
    ("Figure-Ground Segregation (Edgar Rubin)", "The visual cortex automatically distinguishes between focal objects (figures) and the contextual background (ground). Superimposition sharpens this separation."),
    ("Monocular Occlusion Cues", "When Object A partially blocks Object B, the brain instinctively deduces that A is physically closer in 3D space than B. No 3D glasses needed!"),
    ("Context Preservation (Zero Memory Penalty)", "Superimposing a drawer or tooltip over a form allows users to inspect reference data without losing their input state, preventing working memory overload.")
]
for c_title, c_desc in cog:
    p = tf_r.add_paragraph()
    p.text = f"\n• {c_title}:\n"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    run = p.add_run()
    run.text = c_desc
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED

p_bot = tf_r.add_paragraph()
p_bot.text = "\nUI/UX Heuristic: Always provide clear depth cues (elevation shadow, border, blur) so users understand what is interactive vs. what is background context."
p_bot.font.size = Pt(8.5)
p_bot.font.color.rgb = ACCENT_EMERALD

add_speaker_notes(s3, "In this slide, we examine the theoretical roots of Superimposition. In graphic design history, Moholy-Nagy and the Bauhaus pioneers used photomontage to combine disparate planes into one narrative. In cognitive psychology, Edgar Rubin proved that our brains instantly separate figure from ground. Occlusion—one object partially hiding another—is the strongest monocular depth cue humans possess. In UI/UX, we harness this cue to keep users situated in their workflow while presenting secondary information.")

# ==========================================
# SLIDE 4: SUPERIMPOSITION IN MODERN UI/UX
# ==========================================
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4)
add_header(s4, "MODULE 01 • INTERFACE PATTERNS", "Superimposition in Modern UI/UX Architecture", "From CSS Z-Index Stacking to Spatial Glassmorphism and Heads-Up Displays")

if os.path.exists(Z_STACK_PATH):
    s4.shapes.add_picture(Z_STACK_PATH, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.9))

add_card(s4, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.9))
tb_p = s4.shapes.add_textbox(Inches(7.2), Inches(2.0), Inches(5.0), Inches(4.5))
tf_p = tb_p.text_frame
tf_p.word_wrap = True
tf_p.margin_left = tf_p.margin_top = tf_p.margin_right = tf_p.margin_bottom = 0

p = tf_p.paragraphs[0]
p.text = "CORE DIGITAL IMPLEMENTATIONS"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = ACCENT_BLUE

patterns = [
    ("1. Glassmorphism & Translucency", "CSS backdrop-filter: blur(20px) allows users to perceive that content continues beneath the active sheet (e.g. iOS Control Center, macOS Sonoma). It creates depth while maintaining orientation."),
    ("2. Persistent Floating Controls (FAB & Bottom Sheets)", "Floating Action Buttons and persistent action bars live at z-index 50. According to Fitts's Law, their superimposed position keeps high-frequency triggers within immediate thumb reach."),
    ("3. Spatial Computing & Heads-Up Displays (HUDs)", "In Apple VisionOS and automotive windshield HUDs, digital UI windows are superimposed directly onto the physical environment, using real-time ambient lighting cast shadows to look grounded.")
]
for p_title, p_desc in patterns:
    p = tf_p.add_paragraph()
    p.text = f"\n{p_title}"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p_d = tf_p.add_paragraph()
    p_d.text = p_desc
    p_d.font.size = Pt(9)
    p_d.font.color.rgb = TEXT_MUTED

p_warn = tf_p.add_paragraph()
p_warn.text = "\nCRITICAL UX WARNING: The 'Layer Cake' Trap\nStacking more than 3 distinct active layers causes cognitive friction and fails WCAG AA contrast standards. Always enforce scrim dimming."
p_warn.font.size = Pt(8.5)
p_warn.font.color.rgb = ACCENT_ROSE

add_speaker_notes(s4, "Notice our custom Z-stack diagram on the left. In digital architecture, superimposition is quantified through the Z-axis. From background canvas, to content cards, floating buttons, modal scrims, and spatial AR reticles. On the right, we break down how glassmorphism in iOS and macOS maintains spatial continuity without tearing the user away from their context. But as designers, we must watch out for the 'Layer Cake' trap: when too many layers overlap, contrast collapses and users become disoriented.")

# ==========================================
# SLIDE 5: DECONSTRUCTING ANTHROPOMORPHIZATION
# ==========================================
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5)
add_header(s5, "MODULE 02 • EMOTIONAL AFFORDANCE", "Anthropomorphization: Evolutionary Roots & Relational UX", "Attributing human traits, emotional states, and social intent to digital interfaces")

add_card(s5, Inches(0.8), Inches(1.8), Inches(5.7), Inches(5.0))
tb_l = s5.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.1), Inches(4.4))
tf_l = tb_l.text_frame
tf_l.word_wrap = True
tf_l.margin_left = tf_l.margin_top = tf_l.margin_right = tf_l.margin_bottom = 0

p = tf_l.paragraphs[0]
p.text = "CORE DESIGN DEFINITION"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = ACCENT_PURPLE

p = tf_l.add_paragraph()
p.text = "Anthropomorphism is the innate human tendency to attribute human traits, intentions, emotional expressions, or personality to non-human objects, software, and computational interfaces."
p.font.size = Pt(11)
p.font.color.rgb = TEXT_MAIN

p = tf_l.add_paragraph()
p.text = "\nTHE BIOLOGICAL ENGINE: PAREIDOLIA"
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = ACCENT_AMBER

bio_points = [
    ("Fusiform Face Area (FFA)", "Human neurobiology is optimized to detect two eyes and a mouth within milliseconds. We see friendly 'faces' in car headlights, plugs, and app icons."),
    ("Social Brain Hypothesis", "Humans process computer interactions using the exact same social heuristics we use with other humans (Byron Reeves & Clifford Nass, 'The Media Equation')."),
    ("Infantile Schema (Kindchenschema)", "Konrad Lorenz identified that large heads, large eyes, and soft curved contours trigger instinctual parental warmth and protection.")
]
for b_t, b_d in bio_points:
    p = tf_l.add_paragraph()
    p.text = f"• {b_t}: "
    p.font.size = Pt(9)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    run = p.add_run()
    run.text = b_d
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED

add_card(s5, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
tb_r = s5.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.1), Inches(4.4))
tf_r = tb_r.text_frame
tf_r.word_wrap = True
tf_r.margin_left = tf_r.margin_top = tf_r.margin_right = tf_r.margin_bottom = 0

p = tf_r.paragraphs[0]
p.text = "STRATEGIC VALUE IN UI/UX DESIGN"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = ACCENT_CYAN

ux_points = [
    ("1. Immediate Cognitive Familiarity", "Instead of reading lengthy documentation, users rely on innate social protocols (greetings, turn-taking, nodding) to navigate complex digital systems."),
    ("2. Reducing Technophobia & Onboarding Fear", "Intimidating financial, medical, or tax software feels approachable when a humble, humanlike guide walks the user step-by-step."),
    ("3. The 'Pratfall Effect' & Error Tolerance", "When an interface displays genuine humanlike humility (e.g. 'Oops, we dropped the ball!'), users exhibit significantly higher patience and lower churn than when confronted with robotic HTTP error codes."),
    ("4. Brand Recall & Emotional Stickiness", "Users don't form emotional relationships with database engines; they form relationships with personalities (e.g. Duolingo's Duo, Github's Octocat, Apple's Siri).")
]
for u_t, u_d in ux_points:
    p = tf_r.add_paragraph()
    p.text = f"\n{u_t}"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p_sub = tf_r.add_paragraph()
    p_sub.text = u_d
    p_sub.font.size = Pt(9)
    p_sub.font.color.rgb = TEXT_MUTED

add_speaker_notes(s5, "Now we explore Anthropomorphism. Why do we treat our phones, cars, and software like they have thoughts and feelings? Because of pareidolia and our evolutionary Fusiform Face Area. Clifford Nass and Byron Reeves proved in 'The Media Equation' that humans unconsciously treat digital interfaces according to social rules. If an app is polite, we like it; if an app is rude or cold, we reject it. As UI/UX designers, we can leverage this to reduce technophobia and dramatically increase user forgiveness during system errors.")

# ==========================================
# SLIDE 6: DON NORMAN'S THREE LEVELS OF EMOTIONAL DESIGN
# ==========================================
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6)
add_header(s6, "MODULE 02 • THEORETICAL FRAMEWORK", "Don Norman's 3 Levels of Emotional Design", "Mapping Visceral, Behavioral, and Reflective layers to UI Anthropomorphism")

if os.path.exists(EMOTIONAL_PATH):
    s6.shapes.add_picture(EMOTIONAL_PATH, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.9))

add_card(s6, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.9))
tb_e = s6.shapes.add_textbox(Inches(7.2), Inches(2.0), Inches(5.0), Inches(4.5))
tf_e = tb_e.text_frame
tf_e.word_wrap = True
tf_e.margin_left = tf_e.margin_top = tf_e.margin_right = tf_e.margin_bottom = 0

p = tf_e.paragraphs[0]
p.text = "TRANSLATING NORMAN'S TRIAD TO INTERFACES"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = ACCENT_AMBER

triad_notes = [
    ("1. Visceral Level (Pre-Cognitive / Gut Reaction)", "Processed in <50ms. Triggered by baby-schema geometry, warm color harmonies, rounded button corners, and friendly visual symmetry. It asks: 'Does this look safe and delightful?'"),
    ("2. Behavioral Level (Usability & Organic Physics)", "How the interface feels during direct manipulation. Springs that compress on drag, loading skeletons that breathe with human lung cadence, micro-switches that snap like tactile physical toggles. It asks: 'Does this respond naturally?'"),
    ("3. Reflective Level (Identity, Pride & Storytelling)", "The post-interaction narrative. How users feel about their own identity after engaging. Duolingo's mascot celebrating user language milestones, Spotify Wrapped diagnosing music personalities. It asks: 'What does this product say about who I am?'")
]
for t_title, t_desc in triad_notes:
    p = tf_e.add_paragraph()
    p.text = f"\n{t_title}"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p_d = tf_e.add_paragraph()
    p_d.text = t_desc
    p_d.font.size = Pt(9)
    p_d.font.color.rgb = TEXT_MUTED

add_speaker_notes(s6, "Here we see Don Norman's famous Emotional Design triad applied directly to interface anthropomorphism. At the Visceral level, rounded organic corners and soft palettes trigger subconscious safety signals. At the Behavioral level, organic easing curves—like spring physics and breathing loaders—make the interface feel organically alive. At the Reflective level, brand personality creates long-term user attachment. A great UI/UX designer designs across all three levels simultaneously.")

# ==========================================
# SLIDE 7: ANTHROPOMORPHISM ACROSS DIGITAL TOUCHPOINTS
# ==========================================
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7)
add_header(s7, "MODULE 02 • TOUCHPOINTS & MASCOTS", "Digital Touchpoints: Mascots, Physics & Microcopy", "How subtle human gestures and brand personas turn mechanical tools into companions")

add_card(s7, Inches(0.8), Inches(1.8), Inches(4.2), Inches(5.0))
if os.path.exists(TOM_PATH):
    s7.shapes.add_picture(TOM_PATH, Inches(1.1), Inches(2.0), Inches(3.6), Inches(3.6))

tb_tm = s7.shapes.add_textbox(Inches(1.1), Inches(5.7), Inches(3.6), Inches(0.9))
tf_tm = tb_tm.text_frame
tf_tm.word_wrap = True
tf_tm.margin_left = tf_tm.margin_top = tf_tm.margin_right = tf_tm.margin_bottom = 0
p = tf_tm.paragraphs[0]
p.text = "Mascot Persona in Action"
p.font.size = Pt(10)
p.font.bold = True
p.font.color.rgb = ACCENT_AMBER
p2 = tf_tm.add_paragraph()
p2.text = "Classic anthropomorphic animation: projecting human social drama (mugshot, smirk) onto a character. Digital UI uses this same technique to make brand mascots unforgettable."
p2.font.size = Pt(8)
p2.font.color.rgb = TEXT_MUTED

add_card(s7, Inches(5.3), Inches(1.8), Inches(7.2), Inches(5.0))
tb_t = s7.shapes.add_textbox(Inches(5.6), Inches(2.1), Inches(6.6), Inches(4.4))
tf_t = tb_t.text_frame
tf_t.word_wrap = True
tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0

p = tf_t.paragraphs[0]
p.text = "THREE PILLARS OF INTERFACE ANTHROPOMORPHISM"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = ACCENT_BLUE

pillars = [
    ("A. Micro-Interactions & Organic Physics", "Instead of robotic linear transitions (ease-in-out), modern UI uses damping springs and gravity. When you drag a card on iOS, it squishes slightly like rubber; when you refresh, the spinner stretches like elastic dough. This simulates natural biological tactile feedback."),
    ("B. Contextual Peek-a-Boo & Mascot Reactions", "On login pages like Readme.com, the mascot covers its eyes when the user clicks into the password input field, then peeks when the user toggles 'show password'. This humanizes the routine act of authentication, eliciting a genuine smile."),
    ("C. Conversational Voice & Microcopy Rhythm", "Robotic error: 'Error 404: Object Null Reference'. Anthropomorphic microcopy: 'We looked everywhere, but we couldn't find that page. Let's get you back home.' Conversational phrasing restores user confidence and eliminates technological intimidation.")
]
for p_title, p_desc in pillars:
    p = tf_t.add_paragraph()
    p.text = f"\n{p_title}"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p_d = tf_t.add_paragraph()
    p_d.text = p_desc
    p_d.font.size = Pt(9.5)
    p_d.font.color.rgb = TEXT_MUTED

add_speaker_notes(s7, "On this slide, look at the classic Tom character on the left. In animation and design, giving an animal human postures and social context creates instant empathy. On the right, we examine how this translates into UI. It's not just drawing a cartoon; it's in the physics of our animations. When an element stretches like rubber or an owl mascot covers its eyes when you type a password, we are injecting biological playfulness into dry digital workflows.")

# ==========================================
# SLIDE 8: THE UNCANNY VALLEY IN UX DESIGN
# ==========================================
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8)
add_header(s8, "MODULE 02 • THE DANGER ZONE", "Masahiro Mori's Uncanny Valley (1970) in UX", "Why hyper-realistic avatars creep users out, and why honest abstraction always wins")

if os.path.exists(UNCANNY_PATH):
    s8.shapes.add_picture(UNCANNY_PATH, Inches(0.8), Inches(1.8), Inches(5.8), Inches(4.9))

add_card(s8, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.9))
tb_u = s8.shapes.add_textbox(Inches(7.2), Inches(2.0), Inches(5.0), Inches(4.5))
tf_u = tb_u.text_frame
tf_u.word_wrap = True
tf_u.margin_left = tf_u.margin_top = tf_u.margin_right = tf_u.margin_bottom = 0

p = tf_u.paragraphs[0]
p.text = "THE PSYCHOLOGICAL REJECTION THRESHOLD"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = ACCENT_ROSE

p = tf_u.add_paragraph()
p.text = "Formulated by Japanese roboticist Masahiro Mori in 1970: As an artificial entity becomes more human-like, user comfort increases up to a cliff where near-human imperfections trigger evolutionary disgust and distrust."
p.font.size = Pt(9.5)
p.font.color.rgb = TEXT_MAIN

pitfalls = [
    ("The Metaverse Avatar Trap", "Early VR attempts at photorealistic 3D human avatars resulted in lifeless, glazed eyes, mismatched lip sync, and stiff micro-expressions that alienated users."),
    ("The Synthetic Bank Teller Failure", "AI customer service agents with rendered 3D human faces make users hyper-scrutinize every glitch. Users report feeling watched by a digital zombie."),
    ("The Sweet Spot: Honest Stylization", "Duolingo, Pixar characters, Discord Wumpus, and Slack emoji stay safely on the left peak. Because they are stylized cartoons, the user's imagination fills in the emotional warmth without expecting anatomical perfection.")
]
for p_t, p_d in pitfalls:
    p = tf_u.add_paragraph()
    p.text = f"\n• {p_t}:"
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER
    p_sub = tf_u.add_paragraph()
    p_sub.text = p_d
    p_sub.font.size = Pt(9)
    p_sub.font.color.rgb = TEXT_MUTED

p_rule = tf_u.add_paragraph()
p_rule.text = "\nB.Des Studio Rule: 'Stylize the form, humanize the behavior. Never fake human biology.'"
p_rule.font.size = Pt(9.5)
p_rule.font.bold = True
p_rule.font.color.rgb = ACCENT_EMERALD

add_speaker_notes(s8, "Every UX student must understand the Uncanny Valley curve shown on the left. In 1970, Masahiro Mori discovered that when an entity looks almost human, but has a 1% imperfection—like dead eyes or unnatural blinking—our brain classifies it as a diseased corpse or threat, causing revulsion. That's why hyper-realistic 3D AI bank tellers fail. Honest stylization—like Duolingo or Pixar—bypasses this trap entirely. Our takeaway: never try to fake human biology; use clean, expressive abstraction.")

# ==========================================
# SLIDE 9: THE CONVERGENCE
# ==========================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9)
add_header(s9, "MODULE 03 • THE NEXUS", "When Superimposition Meets Anthropomorphism", "Spatial Empathy: Anchoring humanized agents onto multi-layered reality")

add_card(s9, Inches(0.8), Inches(1.8), Inches(4.2), Inches(5.0))
if os.path.exists(MOUNTAIN_PATH):
    s9.shapes.add_picture(MOUNTAIN_PATH, Inches(1.1), Inches(2.0), Inches(3.6), Inches(3.6))

tb_mp = s9.shapes.add_textbox(Inches(1.1), Inches(5.7), Inches(3.6), Inches(0.9))
tf_mp = tb_mp.text_frame
tf_mp.word_wrap = True
tf_mp.margin_left = tf_mp.margin_top = tf_mp.margin_right = tf_mp.margin_bottom = 0
p = tf_mp.paragraphs[0]
p.text = "Visual Art Case: Spatial Superimposition"
p.font.size = Pt(9.5)
p.font.bold = True
p.font.color.rgb = ACCENT_CYAN
p2 = tf_mp.add_paragraph()
p2.text = "Superimposing humanoid figures onto a mountain landscape imbues cold geography with emotional presence and divine protection."
p2.font.size = Pt(8)
p2.font.color.rgb = TEXT_MUTED

add_card(s9, Inches(5.3), Inches(1.8), Inches(7.2), Inches(5.0))
tb_c = s9.shapes.add_textbox(Inches(5.6), Inches(2.1), Inches(6.6), Inches(4.4))
tf_c = tb_c.text_frame
tf_c.word_wrap = True
tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0

p = tf_c.paragraphs[0]
p.text = "THREE SPATIAL EMPATHY PARADIGMS IN UI/UX"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = ACCENT_PURPLE

convergences = [
    ("1. Apple VisionOS 'Spatial Personas'", "Apple solved the isolation of VR by superimposing real-time 3D volumetric avatars into the user's living room during FaceTime. By synchronizing micro-gaze tracking and spatial audio, it creates the cognitive illusion of another human sharing your physical room."),
    ("2. Real-Time AR Face Tracking & Lenses (Snapchat / Instagram)", "Superimposing anthropomorphic animal features, blush, and exaggerated eyes directly onto the user's live video feed. This merges the user's own identity with an expressive avatar layer in real time."),
    ("3. Spatial AI Companions & Ambient Assistants", "In future smart home and automotive interfaces, AI agents won't be confined to flat rectangles; they will be superimposed as ambient spatial holographic entities on kitchen counters or dashboards, gesturing and making eye contact.")
]
for c_title, c_desc in convergences:
    p = tf_c.add_paragraph()
    p.text = f"\n{c_title}"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN
    p_d = tf_c.add_paragraph()
    p_d.text = c_desc
    p_d.font.size = Pt(9.5)
    p_d.font.color.rgb = TEXT_MUTED

add_speaker_notes(s9, "Now we arrive at the nexus where both principles collide. On the left, look at how superimposing humanoid figures onto a mountain terrain immediately transforms cold rock into an emotional, spiritual presence. In digital design, this is Spatial Empathy. Apple VisionOS uses Spatial Personas to project your friend's volumetric avatar directly onto the carpet of your living room. It's the ultimate marriage of Z-depth superimposition and human micro-expression.")

# ==========================================
# SLIDE 10: COMPARATIVE HEURISTIC MATRIX
# ==========================================
s10 = prs.slides.add_slide(blank_layout)
set_slide_background(s10)
add_header(s10, "MODULE 03 • CASE STUDY TEARDOWN", "Comparative Heuristic Matrix: Industry Case Studies", "A structured breakdown of modern digital products utilizing both design levers")

table_shape = s10.shapes.add_table(5, 5, Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.8))
table = table_shape.table

col_widths = [Inches(1.8), Inches(2.5), Inches(2.5), Inches(2.6), Inches(2.3)]
for i, w in enumerate(col_widths):
    table.columns[i].width = w

headers = ["PRODUCT / USE CASE", "SUPERIMPOSITION TYPE", "ANTHROPOMORPHIC TRAIT", "UX IMPACT & METRIC", "FAILURE RISK"]
for j, h in enumerate(headers):
    cell = table.cell(0, j)
    cell.fill.solid()
    cell.fill.fore_color.rgb = CARD_BG_LIGHT
    cell.text = h
    p = cell.text_frame.paragraphs[0]
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = ACCENT_BLUE
    p.alignment = PP_ALIGN.CENTER

rows_data = [
    ("Duolingo Streak HUD", "Floating Lockscreen Widget & Dynamic Island overlay", "Urgent, weeping, or ecstatic mascot persona (Duo)", "+18% Day-30 retention; builds intense daily habit loop", "Emotional fatigue; user annoyance at aggressive guilt"),
    ("Apple Dynamic Island", "Morphing black pill superimposed on status bar", "Organic 'breathing' elasticity and fluid squash/stretch", "Glanceable background awareness with zero context switch", "Occlusion of top screen content; thumb reach strain"),
    ("Apple VisionOS Personas", "Volumetric 3D spatial mesh rendered in user's room", "Synchronized eye gaze, mouth shape & head tilts", "Deep psychological co-presence in remote collaboration", "Occasional uncanny eye tracking glitches; processing lag"),
    ("Automotive AR HUD (Mercedes / Tesla)", "Windshield optical projection directly over roadway", "Pedestrian stick-figure avatars with gaze vectors", "Reduces driver reaction time by 280ms during night driving", "Cognitive visual clutter; driver target fixation risk")
]

for i, row in enumerate(rows_data):
    for j, val in enumerate(row):
        cell = table.cell(i+1, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = CARD_BG if i % 2 == 0 else CARD_BG_LIGHT
        cell.text = val
        p = cell.text_frame.paragraphs[0]
        p.font.size = Pt(8.5)
        p.font.color.rgb = TEXT_MAIN if j == 0 else TEXT_MUTED
        if j == 0:
            p.font.bold = True
            p.font.color.rgb = ACCENT_CYAN
        elif j == 4:
            p.font.color.rgb = ACCENT_ROSE

add_speaker_notes(s10, "To ground our research in rigorous UI/UX methodology, I built this comparative heuristic matrix. Look at how Duolingo pairs a floating lock-screen widget with an urgent mascot persona, driving an 18% lift in retention. Meanwhile, Apple's Dynamic Island uses organic elastic physics to make a hardware sensor cutout feel like a responsive living organ. Each technique comes with real trade-offs—such as visual distraction or emotional fatigue—which we must balance as designers.")

# ==========================================
# SLIDE 11: ETHICAL FRONTIER & DARK PATTERNS
# ==========================================
s11 = prs.slides.add_slide(blank_layout)
set_slide_background(s11)
add_header(s11, "MODULE 04 • ETHICAL DESIGN", "The Dark Side: Deceptive Empathy & Sensory Clutter", "When emotional anthropomorphism turns manipulative and visual layering breaks accessibility")

cards_eth = [
    ("DARK PATTERN 01: DECEPTIVE EMPATHY", "Weaponizing Guilt (Confirmshaming)", [
        "• What is it?: Using cute anthropomorphic mascots crying or looking heartbroken when a user tries to cancel a subscription or delete an account.",
        "• Example: 'Are you really going to make Duo cry?' or pet apps showing shivering animals to prevent cancellation.",
        "• The Ethical Breach: Coercing user decisions through artificial emotional distress rather than functional value."
    ], ACCENT_ROSE, Inches(0.8), Inches(1.8)),

    ("DARK PATTERN 02: OVER-SUPERIMPOSITION", "The Layer Cake & Visual Hostage", [
        "• What is it?: Stacking multiple translucent modals, persistent banners, chat bubbles, and consent overlays until the base content is completely obscured.",
        "• Accessibility Violation: Fails WCAG 2.1 contrast standards (4.5:1 ratio) on low-end screens or under direct sunlight.",
        "• Cognitive Consequence: Induces sensory overload, micro-frustration, and loss of mental spatial mapping."
    ], ACCENT_AMBER, Inches(6.8), Inches(1.8)),

    ("DARK PATTERN 03: FALSE SENTIENCE", "Misleading Trust in Generative AI", [
        "• What is it?: Designing conversational bots that claim to 'feel sad' or 'remember your friendship' when they are simply statistical LLM token predictors.",
        "• Vulnerable Users: Elderly, children, and lonely users form parasocial dependencies and reveal sensitive private data.",
        "• Design Mandate: Honest AI disclosure—always convey system limitations clearly."
    ], ACCENT_PURPLE, Inches(0.8), Inches(4.5)),

    ("THE B.DES ETHICAL MANIFESTO", "Our Studio Guiding Principle", [
        "• 'Humanize to assist, never to manipulate.'",
        "• 'Layer to clarify, never to obscure.'",
        "• Empathy must be a conduit for user empowerment, not a mechanism for dark-pattern entrapment."
    ], ACCENT_EMERALD, Inches(6.8), Inches(4.5))
]

for title, sub, items, col, x, y in cards_eth:
    add_card(s11, x, y, Inches(5.7), Inches(2.3))
    tb = s11.shapes.add_textbox(x + Inches(0.3), y + Inches(0.2), Inches(5.1), Inches(1.9))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = col
    
    p_sub = tf.add_paragraph()
    p_sub.text = sub
    p_sub.font.size = Pt(12)
    p_sub.font.bold = True
    p_sub.font.color.rgb = TEXT_MAIN
    
    for itm in items:
        pi = tf.add_paragraph()
        pi.text = itm
        pi.font.size = Pt(8.5)
        pi.font.color.rgb = TEXT_MUTED

add_speaker_notes(s11, "As designers, we cannot ignore ethics. Anthropomorphism becomes toxic when it turns into 'Deceptive Empathy'—like a streaming app showing a crying cartoon to guilt you out of unsubscribing. That is manipulative confirmshaming. Similarly, over-superimposition destroys accessibility for users with visual impairments. In our studio work, our manifesto must be clear: humanize to assist, never to manipulate; layer to clarify, never to obscure.")

# ==========================================
# SLIDE 12: MY B.DES STUDIO FRAMEWORK
# ==========================================
s12 = prs.slides.add_slide(blank_layout)
set_slide_background(s12)
add_header(s12, "MODULE 04 • PRACTICAL TOOLKIT", "My B.Des Studio Framework: 5 Golden Heuristics", "A ready-to-use checklist for designing spatial layers and humanized micro-interactions")

rules = [
    ("RULE 01", "Establish Strict Z-Axis Roles", "Every superimposed element must justify its elevation. Layer 0 = Surface, Layer 1 = Content, Layer 2 = Floating triggers, Layer 3 = Modals. Never stack arbitrarily.", ACCENT_BLUE),
    ("RULE 02", "Respect the Uncanny Boundary", "Always choose stylized geometric abstraction over pseudorealistic 3D human renders. An expressive 2D mascot is infinitely more empathetic than a creepy synthetic human.", ACCENT_PURPLE),
    ("RULE 03", "Anchor Motion in Natural Physics", "Use cubic-bezier spring curves (damping ratio 0.7) and organic mass rather than linear motion. Let buttons stretch and bounce with biological playfulness.", ACCENT_CYAN),
    ("RULE 04", "Enforce Strict WCAG Accessibility", "Ensure any superimposed text or icon maintains at least 4.5:1 contrast against blurred backdrops. Always provide non-motion fallbacks for vestibular disorders.", ACCENT_AMBER),
    ("RULE 05", "Preserve Total User Autonomy", "Never use mascot tears or simulated grief to guilt-trip users during cancellation or settings flows. Emotional design must serve clarity, never manipulation.", ACCENT_EMERALD)
]

for i, (r_num, r_title, r_desc, col) in enumerate(rules):
    y_pos = Inches(1.8 + i * 1.0)
    card = add_card(s12, Inches(0.8), y_pos, Inches(11.7), Inches(0.85))
    
    badge = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), y_pos + Inches(0.18), Inches(1.2), Inches(0.48))
    badge.fill.solid()
    badge.fill.fore_color.rgb = CARD_BG_LIGHT
    badge.line.color.rgb = col
    badge.line.width = Pt(1)
    tf_bg = badge.text_frame
    p = tf_bg.paragraphs[0]
    p.text = r_num
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = col
    p.alignment = PP_ALIGN.CENTER
    
    tb = s12.shapes.add_textbox(Inches(2.4), y_pos + Inches(0.12), Inches(9.8), Inches(0.65))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    p = tf.paragraphs[0]
    p.text = r_title + " — "
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    run = p.add_run()
    run.text = r_desc
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED

add_speaker_notes(s12, "From this research, I created this 5-point studio framework for our UI/UX design projects. Before presenting any prototype in our jury or critique, we can audit it: Did we justify the Z-axis? Did we stay out of the Uncanny Valley? Are our physics organic? Is our contrast accessible? And do we respect user autonomy? This gives us a concrete design methodology.")

# ==========================================
# SLIDE 13: CONCLUSION, REFERENCES & Q&A
# ==========================================
s13 = prs.slides.add_slide(blank_layout)
set_slide_background(s13)
add_header(s13, "CONCLUSION & BIBLIOGRAPHY", "Harmonizing Space and Soul in Design", "Summary thesis, academic references, and jury discussion")

add_card(s13, Inches(0.8), Inches(1.8), Inches(5.7), Inches(4.9))
tb_th = s13.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.1), Inches(4.3))
tf_th = tb_th.text_frame
tf_th.word_wrap = True
tf_th.margin_left = tf_th.margin_top = tf_th.margin_right = tf_th.margin_bottom = 0

p = tf_th.paragraphs[0]
p.text = "CORE THESIS SUMMARY"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = ACCENT_BLUE

p = tf_th.add_paragraph()
p.text = "\n'Great digital product design lives in the deliberate harmony of Space and Soul.'"
p.font.size = Pt(13)
p.font.bold = True
p.font.color.rgb = ACCENT_CYAN

points = [
    ("Superimposition governs SPACE", "It structures visual priority, preserves context along the z-axis, and eliminates cognitive disjunction in 2D and 3D viewports."),
    ("Anthropomorphism governs SOUL", "It sparks emotional resonance, builds intuitive mental models via social cues, and turns cold computational tools into trusted partners."),
    ("The Ultimate Goal", "To craft interfaces that are spatially transparent, emotionally dignified, and ergonomically effortless.")
]
for p_t, p_d in points:
    p = tf_th.add_paragraph()
    p.text = f"\n• {p_t}: "
    p.font.size = Pt(9.5)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN
    run = p.add_run()
    run.text = p_d
    run.font.bold = False
    run.font.color.rgb = TEXT_MUTED

add_card(s13, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.9))
tb_rf = s13.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.1), Inches(4.3))
tf_rf = tb_rf.text_frame
tf_rf.word_wrap = True
tf_rf.margin_left = tf_rf.margin_top = tf_rf.margin_right = tf_rf.margin_bottom = 0

p = tf_rf.paragraphs[0]
p.text = "ACADEMIC & INDUSTRY REFERENCES"
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = ACCENT_AMBER

refs = [
    "1. Norman, Donald A. (2004). Emotional Design: Why We Love (or Hate) Everyday Things. Basic Books.",
    "2. Mori, Masahiro (1970). The Uncanny Valley. Energy, 7(4), pp. 33–35.",
    "3. Reeves, Byron & Nass, Clifford (1996). The Media Equation: How People Treat Computers Like Real People. Cambridge University Press.",
    "4. Rubin, Edgar (1915). Synsoplevede Figurer (Figure-Ground Perception). Gyldendalske.",
    "5. Nielsen Norman Group (NN/g). (2024). Emotional Ergonomics & Spatial Overlay Guidelines in XR."
]
for ref in refs:
    p = tf_rf.add_paragraph()
    p.text = ref
    p.font.size = Pt(8.5)
    p.font.color.rgb = TEXT_MUTED

p_cr = tf_rf.add_paragraph()
p_cr.text = "\nSTUDENT PRESENTER:"
p_cr.font.size = Pt(10)
p_cr.font.bold = True
p_cr.font.color.rgb = ACCENT_PURPLE

p_cr2 = tf_rf.add_paragraph()
p_cr2.text = "Bhavya Anand • Roll No: 2501730046\nB.Des (UI & UX Design) • Semester III • K.R. Mangalam University\nEmail: bhavya.bpr@gmail.com\n\nTHANK YOU! HAPPY TO TAKE QUESTIONS FROM THE JURY."
p_cr2.font.size = Pt(9)
p_cr2.font.bold = True
p_cr2.font.color.rgb = TEXT_MAIN

add_speaker_notes(s13, "To conclude: Space and Soul. Superimposition choreographs spatial depth and mental models, while Anthropomorphism choreographs relational warmth and empathy. I have cited foundational literature here from Don Norman, Masahiro Mori, and Edgar Rubin. Thank you so much for your time and attention. I am eager to hear your feedback, critique, and questions!")

# ==========================================
# SAVE PRESENTATION
# ==========================================
output_dir = "/Users/bhavya/Desktop/ /Sem_3/Superimposition_and_Anthropomorphization_Presentation"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "Superimposition_and_Anthropomorphization_in_Design_Bhavya_Anand.pptx")
prs.save(output_file)

workspace_copy = "/Users/bhavya/Desktop/ /Sem_3/ML/Superimposition_and_Anthropomorphization_in_Design_Bhavya_Anand.pptx"
prs.save(workspace_copy)

print("SUCCESS: Presentation PPTX created at:")
print(f"1. {output_file}")
print(f"2. {workspace_copy}")
