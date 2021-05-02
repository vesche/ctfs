from PIL import Image

im = Image.open('out_copy.jpg')
pixels = im.load()
oc_width, _ = im.size

width = 304
height = oc_width//304

final_image = Image.new('RGB', (304, height))

col, row = 0, 0
for x in range(oc_width):
    final_image.putpixel((col, row), pixels[x, 0])
    row += 1
    if row == 92:
        row = 0
        col += 1

final_image.save('out_copy_solve.png')
