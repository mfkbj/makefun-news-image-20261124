#!/usr/bin/env python3
"""Draw entry.png: a 1024x1024 news infographic for Tuesday 24 November 2026.
Built with PIL only, so every word is set in a real font (no AI-image garbling).
Stories are the events first reported on 24 November 2026, as carried that day
by the Japan Times, Times of India, SCMP and Manila Times news pages.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), "#F4F1EA")
d = ImageDraw.Draw(img)

NAVY = "#0F2A44"
GOLD = "#C9A227"
INK = "#1A1A1A"
GREY = "#555555"
CARD = "#FFFFFF"
LINE = "#D8D2C4"

# ---- header ----
d.rectangle([0, 0, W, 168], fill=NAVY)
d.rectangle([0, 168, W, 174], fill=GOLD)
d.text((32, 22), "TUESDAY, 24 NOVEMBER 2026", font=font(BOLD, 52), fill="#FFFFFF")
d.text((32, 92), "THE WORLD IN ONE IMAGE", font=font(BOLD, 30), fill="#F2C94C")
d.text((32, 132), "Six stories that defined the day  \u00b7  Events first reported on 24 November 2026",
       font=font(REG, 21), fill="#C7D2DE")

STORIES = [
    ("1", "TECH", "#0B6E4F", "Nvidia brings back Huang as CEO",
     "Board reinstates Jensen Huang after pressure from President Trump, who says he \u201cmade the deal\u201d."),
    ("2", "WAR", "#8B1E1E", "Ukraine hits Russian warship off Libya",
     "Kyiv says the strike, far from home waters, shows the war\u2019s reach is widening."),
    ("3", "ASIA", "#1D4E89", "Suspect North Korean jet enters South\u2019s airspace",
     "Seoul says a suspected North Korean aircraft breached its airspace; Ulleung Island residents told to take shelter."),
    ("4", "U.S. POLITICS", "#5B2D8E", "Democrats clinch 258+ House seats",
     "Final counts give Democrats their largest US House majority since 1992."),
    ("5", "SPORT", "#0E7A5F", "2031 Women\u2019s World Cup: US to host",
     "The US, Mexico, Costa Rica and Jamaica will stage 2031; the UK gets the 2035 edition."),
    ("6", "ENERGY", "#9A6A00", "Three tankers hit mines in Hormuz",
     "Iran claims three oil tankers struck naval mines and caught fire in the Strait of Hormuz."),
]

# ---- 2 x 3 grid ----
gx, gy = 24, 190
cw, ch, gap = 476, 240, 20
for i, (num, tag, color, head, body) in enumerate(STORIES):
    x = gx + (i % 2) * (cw + gap)
    y = gy + (i // 2) * (ch + gap)
    d.rounded_rectangle([x, y, x + cw, y + ch], radius=14, fill=CARD, outline=LINE, width=2)
    d.rounded_rectangle([x, y, x + cw, y + 10], radius=5, fill=color)
    # number badge
    d.ellipse([x + 18, y + 26, x + 62, y + 70], fill=color)
    d.text((x + 40, y + 30), num, font=font(BOLD, 30), fill="#FFFFFF", anchor="ma")
    d.text((x + 76, y + 32), tag, font=font(BOLD, 20), fill=color)
    # headline, wrapped to fit
    lines = []
    for ln in textwrap.wrap(head, width=24):
        lines.append(ln)
    yy = y + 82
    for ln in lines[:2]:
        d.text((x + 18, yy), ln, font=font(BOLD, 27), fill=INK)
        yy += 34
    # body
    blines = textwrap.wrap(body, width=42)
    yy += 6
    for ln in blines[:3]:
        d.text((x + 18, yy), ln, font=font(REG, 20), fill=GREY)
        yy += 27

# ---- footer ----
fy = gy + 3 * ch + 2 * gap + 12
d.text((32, fy), "Sources: reports published 24 November 2026 \u00b7 make.fun \u2014 news-image-20261124",
       font=font(REG, 18), fill="#777777")
d.text((32, fy + 26), "One day, six stories. Nothing here happened on any other day.",
       font=font(REG, 18), fill="#777777")

img.save("entry.png", "PNG", optimize=True)
print("saved entry.png", img.size)
