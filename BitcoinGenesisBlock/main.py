from PIL import Image
import pytesseract

# 画像の読み込み
img = Image.open('./BitcoinGenesisBlock/Bitcoin-Genesis-block.jpg')

# 画像からテキスト抽出
text = pytesseract.image_to_string(img, lang='eng')

print(text)
