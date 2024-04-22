
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os

p = open('guests.txt')
lines = p.readlines()

os.makedirs('invitation_cards', exist_ok=True)

LOGO_FILENAME = 'catlogo.png'

SQUARE_FIT_SIZE = 300
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

for line in lines:
    im = Image.new('RGBA', (288, 360), 'white')
    draw = ImageDraw.Draw(im)
    Font = ImageFont.truetype("/usr/share/fonts/freetype/FreeSerifBold.ttf", 28, encoding="unic")
    draw.text((75, 160), line, fill='purple', font=Font)
    draw.text((15, 90), "You have been invited", fill='black', font=Font)
    draw.line([(0, 0), (287, 0), (287, 359), (0, 359), (0, 0)], fill='red')

    logoIm = logoIm.resize((100,100))
    # Add logo.
    print('Making invitations to %s...' % (line))
    im.paste(logoIm, (85, 260), logoIm)

    im.save(os.path.join('invitation_cards', line + '.png'))
