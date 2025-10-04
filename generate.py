import requests
from PIL import Image, ImageDraw, ImageFont

VISITORS_FILE = 'visitors.txt'
OUTPUT_IMAGE = 'profile_readme.png'
FONT_PATH = ''
FONT_SIZE = 80
IMAGE_SIZE = (3200, 1600)
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
AVATAR_SIZE = (200, 200)
AVATAR_MARGIN = 10

def get_visitors():
    with open(VISITORS_FILE, 'r') as f:
        visitors = [line.strip() for line in f if line.strip()]
    return visitors

def fetch_avatar(username):
    url = f'https://github.com/{username}.png'
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'{username}.png', 'wb') as f:
            f.write(response.content)
        return response.content
    else:
        print(f"Failed to fetch avatar for {username}")
        return None

def generate_image(visitors):
    if len(visitors) < 12:
        global IMAGE_SIZE, FONT_SIZE
        IMAGE_SIZE = (1600, 600)
    image = Image.new('RGB', IMAGE_SIZE, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE) if FONT_PATH else ImageFont.load_default(FONT_SIZE)

    x_offset = AVATAR_MARGIN
    y_offset = (IMAGE_SIZE[1] - AVATAR_SIZE[1]) // 2
    draw.text((x_offset, 10), "Recent Visitors", fill=TEXT_COLOR, font=font)
    y_offset += FONT_SIZE + AVATAR_MARGIN

    for visitor in visitors:
        avatar = fetch_avatar(visitor)
        avatar = Image.open(f'{visitor}.png').resize(AVATAR_SIZE) if avatar else None
        if avatar:
            image.paste(avatar, (x_offset + len(visitor) * 10, y_offset))
            text_x = x_offset
            text_y = y_offset + (AVATAR_SIZE[1] + FONT_SIZE) / 2 + 50
            draw.text((text_x, text_y), visitor, fill=TEXT_COLOR, font=font)
            x_offset += AVATAR_SIZE[0] + FONT_SIZE * len(visitor) // 2 + AVATAR_MARGIN

    image.save(OUTPUT_IMAGE)
    print(f"Image saved as {OUTPUT_IMAGE}")

def main():
    global AVATAR_MARGIN
    visitors = get_visitors()
    if visitors:
        if len(visitors) > 20:
            AVATAR_MARGIN = 5
        generate_image(visitors)
    else:
        print("No visitors found.")

main()