import sys
import time
import random

from PIL import Image
import unicornhathd


def img_path(name):
    return "images/{}.png".format(name)


class UnicornHatHD:

    def __init__(self):
        self.hat = unicornhathd
        self.hat.rotation(90)
        self.hat.brightness(0.6)

    def draw_emoji(self, name):
        width, height = self.hat.get_shape()

        img = Image.open(img_path(name))
        img = img.convert('RGB')
        img = img.resize((width, height), Image.Resampling.BILINEAR)

        for x in range(width):
            for y in range(height):
                r, g, b = img.getpixel((x, y))
                self.hat.set_pixel(x, y, r, g, b)

        self.hat.show()

    def clear(self):
        self.hat.off()


if __name__ == "__main__":
    hat = UnicornHatHD()
    hat.draw_emoji('microphone')

    time.sleep(3)
    hat.clear()
