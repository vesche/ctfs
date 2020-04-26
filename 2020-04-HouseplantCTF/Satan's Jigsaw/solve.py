import os
from PIL import Image

files = sorted(os.listdir('chall/'))

final_image = Image.new('RGB', (300, 300))

i = 0
pixels = []
for f in files:
    im = Image.open('chall/' + f)
    pixel = im.load()[0, 0]
    pixels.append(pixel)
    i += 1

final_image.putdata(pixels)
final_image.save('test.png')
