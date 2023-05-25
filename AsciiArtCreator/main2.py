from PIL import Image

class AsciiArtCreator:
    def __init__(self, image_path, width=100, height=100):
        self.image_path = image_path
        self.width = width
        self.height = height
        self.ascii_chars = '@%#*+=-:. '

    def create_ascii_art(self):
        image = Image.open(self.image_path)
        image = image.resize((self.width, self.height))
        image = image.convert('L')

        pixels = image.getdata()
        ascii_image = ''

        for pixel_value in pixels:
            ascii_index = int(pixel_value / 255 * (len(self.ascii_chars) - 1))
            ascii_image += self.ascii_chars[ascii_index]

            if len(ascii_image) % self.width == 0:
                ascii_image += '\n'

        return ascii_image

# 使用例
creator = AsciiArtCreator('./AsciiArtCreator/sample.png', width=100, height=100)
result = creator.create_ascii_art()
print(result)
