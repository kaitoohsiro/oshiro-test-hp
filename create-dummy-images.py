from PIL import Image, ImageDraw, ImageFont
import os

# 画像保存ディレクトリ
if not os.path.exists('images'):
    os.makedirs('images')

def create_dummy_image(width, height, text, color, filename):
    # 画像作成
    img = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(img)

    # グラデーション効果を追加
    for i in range(height):
        alpha = int(255 * (1 - i / height * 0.3))
        overlay = Image.new('RGBA', (width, 1), (*color, alpha))
        img.paste(overlay, (0, i), overlay)

    # テキスト描画
    try:
        font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', size=min(width, height) // 10)
    except:
        font = ImageFont.load_default()

    # テキストサイズ取得
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # 中央に配置
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # 影効果
    draw.text((x+2, y+2), text, fill=(0, 0, 0, 128), font=font)
    draw.text((x, y), text, fill='white', font=font)

    # サイズ表記
    size_text = f"{width}x{height}"
    bbox2 = draw.textbbox((0, 0), size_text, font=font)
    text_width2 = bbox2[2] - bbox2[0]
    x2 = (width - text_width2) // 2
    y2 = y + text_height + 20
    draw.text((x2, y2), size_text, fill='white', font=font)

    # 保存
    img.save(f'images/{filename}')
    print(f'Created: images/{filename}')

# 画像生成
images = [
    (1200, 800, '🥭 極上マンゴー', (255, 107, 53), 'hero-mango.jpg'),
    (800, 600, '🌴 大城農園', (42, 84, 52), 'farm.jpg'),
    (600, 600, '🥭 アップルマンゴー', (255, 140, 90), 'mango1.jpg'),
    (600, 600, '🥭 キーツマンゴー', (255, 165, 0), 'mango2.jpg'),
    (600, 600, '🥭 金蜜マンゴー', (255, 215, 0), 'mango3.jpg'),
    (800, 600, '🌱 マンゴー畑', (58, 107, 60), 'gallery1.jpg'),
    (800, 600, '📦 収穫', (255, 127, 80), 'gallery2.jpg'),
    (800, 600, '🌸 マンゴーの花', (255, 182, 193), 'gallery3.jpg'),
    (800, 600, '✨ 完熟', (255, 99, 71), 'gallery4.jpg'),
    (800, 600, '🍴 カット', (255, 160, 122), 'gallery5.jpg'),
    (800, 600, '👨‍🌾 農園作業', (74, 124, 78), 'gallery6.jpg')
]

for width, height, text, color, filename in images:
    create_dummy_image(width, height, text, color, filename)

print('All dummy images created successfully!')