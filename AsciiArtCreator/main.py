from PIL import Image

image = Image.open('./AsciiArtCreator/sample.png')

width, height = 100, 100  # アスキーアートの幅と高さ
image = image.resize((width, height))

image = image.convert('L')  # グレースケールに変換

ascii_chars = '@%#*+=-:. '  # アスキーアートに使用する文字のリスト

pixels = image.getdata()  # 画像のピクセルデータを取得
ascii_image = ''

for pixel_value in pixels:
    ascii_index = int(pixel_value / 255 * (len(ascii_chars) - 1))
    ascii_image += ascii_chars[ascii_index]

    if len(ascii_image) % width == 0:  # 一行の文字数が幅に達したら改行する
        ascii_image += '\n'

print(ascii_image)
