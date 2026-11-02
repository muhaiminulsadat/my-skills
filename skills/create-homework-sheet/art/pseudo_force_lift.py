"""Art for Pseudo Force & Lift Homework Practice (100 x 64 box, y up) with LaTeX math labels."""
import math
from drawkit import *

def _elevator_frame(c, x=15, y=6, w=70, h=52, cable=True):
    """Draws a neat elevator cabin with ceiling, floor, and optional cable."""
    stroke_style(c, 1.4)
    c.setFillColor(PALE)
    c.rect(x, y, w, h, fill=1, stroke=1)
    # top beam / floor beam
    c.setFillColor(NAVY)
    c.rect(x - 2, y + h - 3, w + 4, 3, fill=1, stroke=0)
    c.rect(x - 2, y, w + 4, 3, fill=1, stroke=0)
    if cable:
        stroke_style(c, 1.5)
        c.line(x + w / 2, y + h, x + w / 2, 63)

@icon("pfl-q1")
def q1(c):
    # Elevator with person on a scale
    _elevator_frame(c, 16, 6, 68, 52)
    # scale on floor
    c.setFillColor(TEAL_L); stroke_style(c, 1.1)
    c.rect(36, 9, 28, 5, fill=1, stroke=1)
    # student block / figure
    block(c, 42, 14, 16, 24, TEAL, 2)
    mlab(c, 50, 24, r"$50\ \mathrm{kg}$", white, 6.2)
    # head
    ball(c, 50, 42, 4.5, TEAL)
    # acceleration arrows on side
    arrow(c, 90, 18, 90, 44, ORANGE, 1.8, 4.5)
    mlab(c, 90, 48, r"$\vec{a}$", ORANGE, 7.5)

@icon("pfl-q2")
def q2(c):
    # Dropping a ball inside elevator
    _elevator_frame(c, 16, 6, 68, 52)
    # ball near ceiling
    ball(c, 44, 44, 4.5, TEAL)
    # trajectory dashed line
    dashed(c, 44, 39, 44, 12, GREY, 1.0, 2, 2)
    # floor impact circle
    c.setFillColor(TEAL_L); stroke_style(c, 0.8)
    c.circle(44, 11, 2.5, fill=1, stroke=1)
    # dimension h
    dim_arrow(c, 32, 10, 32, 44, ORANGE, 1.1, 3.5)
    mlab(c, 24, 25, r"$1.8\ \mathrm{m}$", ORANGE, 6.2, "r")
    # arrow for lift acceleration
    arrow(c, 90, 20, 90, 42, TEAL, 1.8, 4.5)
    mlab(c, 90, 46, r"$\vec{a}$", TEAL, 7.5)

@icon("pfl-q3")
def q3(c):
    # Suspended 200 kg mass in lift
    _elevator_frame(c, 16, 6, 68, 52)
    # cable inside
    stroke_style(c, 1.3)
    c.line(50, 55, 50, 34)
    arrow(c, 50, 40, 50, 48, ORANGE, 1.5, 4.0)
    mlab(c, 56, 42, r"$T$", ORANGE, 7.5, "l")
    # suspended load
    block(c, 35, 14, 30, 20, TEAL, 2)
    mlab(c, 50, 22, r"$200\ \mathrm{kg}$", white, 6.8)
    # lift acceleration
    arrow(c, 90, 16, 90, 44, ORANGE, 1.8, 4.5)
    mlab(c, 90, 48, r"$\vec{a}$", ORANGE, 7.5)

@icon("pfl-q4")
def q4(c):
    # Truck flatbed with crate
    floor(c, 4, 96, 14, False)
    # Truck cabin on right, flatbed on left
    c.setFillColor(NAVY); stroke_style(c, 1.2)
    c.rect(64, 14, 26, 26, fill=1, stroke=1)
    c.setFillColor(white); c.rect(74, 24, 14, 12, fill=1, stroke=0)
    # flatbed platform
    c.setFillColor(HexColor("#4A607A")); stroke_style(c, 1.2)
    c.rect(10, 14, 54, 4, fill=1, stroke=1)
    # wheels
    for wx in (22, 48, 78):
        c.setFillColor(NAVY); c.circle(wx, 14, 4.5, fill=1, stroke=1)
        c.setFillColor(white); c.circle(wx, 14, 1.6, fill=1, stroke=0)
    # crate
    block(c, 24, 18, 20, 16, TEAL, 1.5)
    mlab(c, 34, 24, r"$20\ \mathrm{kg}$", white, 6.2)
    # truck acceleration arrow
    arrow(c, 64, 46, 92, 46, ORANGE, 2.0, 5)
    mlab(c, 78, 52, r"$\vec{a}$", ORANGE, 8)
    # friction arrow on crate
    arrow(c, 34, 16, 48, 16, TEAL, 1.5, 3.5)
    mlab(c, 41, 9, r"$f_s$", TEAL, 6.5)

@icon("pfl-q5")
def q5(c):
    # Incline inside elevator
    _elevator_frame(c, 14, 6, 72, 52)
    # wedge inside
    th = math.radians(30)
    p = c.beginPath(); p.moveTo(20, 9); p.lineTo(66, 9); p.lineTo(66, 9 + 46 * math.tan(th)); p.close()
    c.setFillColor(HexColor("#E2E8F0")); stroke_style(c, 1.2); c.drawPath(p, fill=1, stroke=1)
    angle_arc(c, 20, 9, 14, 0, 30, "30°", NAVY, 1.0, 6)
    # block on slope
    x0 = 46; y0 = 9 + (x0 - 20) * math.tan(th)
    c.saveState(); c.translate(x0, y0); c.rotate(30)
    block(c, -8, 0, 16, 11, TEAL, 1.5)
    mlab(c, 0, 4.5, r"$m$", white, 6.5)
    c.restoreState()
    # lift acceleration
    arrow(c, 91, 16, 91, 44, ORANGE, 1.8, 4.5)
    mlab(c, 91, 48, r"$\vec{a}$", ORANGE, 7.5)

@icon("pfl-q6")
def q6(c):
    # Classic smooth wedge accelerated horizontally
    floor(c, 4, 96, 12)
    th = math.radians(32)
    p = c.beginPath(); p.moveTo(12, 12); p.lineTo(80, 12); p.lineTo(80, 12 + 68 * math.tan(th)); p.close()
    c.setFillColor(HexColor("#E2E8F0")); stroke_style(c, 1.3); c.drawPath(p, fill=1, stroke=1)
    angle_arc(c, 12, 12, 16, 0, 32, "θ", NAVY, 1.1, 7)
    # block on slope
    x0 = 50; y0 = 12 + (x0 - 12) * math.tan(th)
    c.saveState(); c.translate(x0, y0); c.rotate(32)
    block(c, -9, 0, 18, 12, TEAL, 1.5)
    mlab(c, 0, 4.5, r"$m$", white, 6.8)
    c.restoreState()
    # horizontal acceleration arrow
    arrow(c, 40, 54, 76, 54, ORANGE, 2.0, 5)
    mlab(c, 58, 59, r"$\vec{a}$", ORANGE, 8)

@icon("pfl-q7")
def q7(c):
    # Block on vertical front face of cart
    floor(c, 4, 96, 12)
    # Cart body
    c.setFillColor(HexColor("#CBD5E1")); stroke_style(c, 1.3)
    c.rect(14, 17, 44, 32, fill=1, stroke=1)
    # cart wheels
    for wx in (24, 48):
        c.setFillColor(NAVY); c.circle(wx, 17, 4.5, fill=1, stroke=1)
        c.setFillColor(white); c.circle(wx, 17, 1.6, fill=1, stroke=0)
    # Block against vertical front face (at x = 58)
    block(c, 58, 24, 14, 18, TEAL, 1.5)
    mlab(c, 65, 31, r"$3\ \mathrm{kg}$", white, 5.8)
    # acceleration arrow
    arrow(c, 24, 54, 60, 54, ORANGE, 2.0, 5)
    mlab(c, 42, 59, r"$\vec{a}$", ORANGE, 8)
    # friction arrow
    arrow(c, 65, 42, 65, 52, TEAL, 1.5, 3.5)
    mlab(c, 71, 45, r"$f_s$", TEAL, 6.5, "l")

@icon("pfl-q8")
def q8(c):
    # Atwood machine in elevator
    _elevator_frame(c, 14, 6, 72, 52)
    # pulley
    px, py = 50, 45
    stroke_style(c, 1.3); c.line(px, 55, px, py + 6)
    c.setFillColor(white); c.circle(px, py, 7, fill=1, stroke=1)
    c.setFillColor(NAVY); c.circle(px, py, 1.6, fill=1, stroke=0)
    # strings & masses
    stroke_style(c, 1.1)
    c.line(px - 7, py, px - 7, 26)
    c.line(px + 7, py, px + 7, 18)
    block(c, px - 15, 14, 16, 14, TEAL, 1.5)
    mlab(c, px - 7, 19, r"$m_1$", white, 6.2)
    block(c, px + 1, 8, 13, 11, ORANGE, 1.5)
    mlab(c, px + 7.5, 12, r"$m_2$", NAVY, 5.8)
    # lift acceleration
    arrow(c, 91, 16, 91, 44, ORANGE, 1.8, 4.5)
    mlab(c, 91, 48, r"$\vec{a}_0$", ORANGE, 7.5)

@icon("pfl-q9")
def q9(c):
    # Person pulling themselves in cage
    # Ceiling beam
    hatch(c, 20, 62, 80, 62, 5, 3.5, 1)
    stroke_style(c, 1.3); c.line(20, 62, 80, 62)
    # Pulley at ceiling
    px, py = 50, 54
    stroke_style(c, 1.2); c.line(px, 62, px, py + 5)
    c.setFillColor(white); c.circle(px, py, 6, fill=1, stroke=1)
    c.setFillColor(NAVY); c.circle(px, py, 1.5, fill=1, stroke=0)
    # Cage
    cx, cy, cw, ch = 34, 8, 38, 34
    c.setFillColor(PALE); stroke_style(c, 1.3); c.rect(cx, cy, cw, ch, fill=1, stroke=1)
    c.setFillColor(NAVY); c.rect(cx - 2, cy, cw + 4, 3, fill=1, stroke=0)
    # rope from cage roof to pulley
    stroke_style(c, 1.2)
    c.line(cx + 8, cy + ch, px - 6, py)
    # rope from pulley down to person's hands
    c.line(px + 6, py, cx + 24, cy + 20)
    # person inside cage
    ball(c, cx + 20, cy + 26, 3.5, TEAL)
    block(c, cx + 14, cy + 3, 12, 20, TEAL, 1.5)
    mlab(c, cx + 20, cy + 11, r"$50\ \mathrm{kg}$", white, 5.2)

@icon("pfl-q10")
def q10(c):
    # Accelerating cart with corner pulley and two blocks
    floor(c, 4, 96, 10)
    # Cart body
    c.setFillColor(HexColor("#E2E8F0")); stroke_style(c, 1.3)
    p = c.beginPath(); p.moveTo(14, 15); p.lineTo(74, 15); p.lineTo(74, 46); p.lineTo(14, 46); p.close()
    c.drawPath(p, fill=1, stroke=1)
    # Wheels
    for wx in (26, 62):
        c.setFillColor(NAVY); c.circle(wx, 15, 4.5, fill=1, stroke=1)
        c.setFillColor(white); c.circle(wx, 15, 1.5, fill=1, stroke=0)
    # Pulley at top-right corner
    px, py = 74, 46
    c.setFillColor(white); stroke_style(c, 1.1); c.circle(px, py, 4.5, fill=1, stroke=1)
    c.setFillColor(NAVY); c.circle(px, py, 1.2, fill=1, stroke=0)
    # Block A on top
    block(c, 36, 46, 16, 11, TEAL, 1.5)
    mlab(c, 44, 50, r"$A$", white, 6.5)
    # Block B hanging vertically
    block(c, 75, 24, 10, 14, ORANGE, 1.5)
    mlab(c, 80, 29, r"$B$", NAVY, 6.5)
    # String
    stroke_style(c, 1.0)
    c.line(52, 51.5, px, 51.5)
    c.line(px + 4.5, py, px + 4.5, 38)
    # Acceleration arrow
    arrow(c, 24, 30, 56, 30, ORANGE, 1.8, 4.5)
    mlab(c, 40, 35, r"$\vec{a}$", ORANGE, 8)
