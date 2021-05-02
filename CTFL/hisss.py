from PIL import Image

img1 = Image.open('hisss1.png')
img2 = Image.open('hisss2.png')

pixels1 = list(img1.getdata())
pixels2 = list(img2.getdata())

test = Image.new('RGB', (512, 512))

c = 0
for p1, p2 in zip(pixels1, pixels2):
    x, y = c%512, c//512
    if p1 == p2:
       test.putpixel((x, y), (255, 255, 255))
    else:
        test.putpixel((x, y), (0, 0, 0))
    c += 1

test.save('hisss_solve.png')
