from PIL import Image
from random import randint

img = Image.new( 'RGB', (1080,1080), "white") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0, img.size[0], 30):
    for j in range(0, img.size[1], 30):
        orientation = randint(0,3)
        orientation = 0
        for k in range(0,30) :
            for l in range(0,30) :
                if orientation == 0 :
                    if ((i + k) % 30 >= (l + j) % 30):
                        if k >= 25 :
                            pixels[i + k, l + j] = ((i + k)/4,255,(l + j)/4)
                    if ((i + k) % 30 >= (l + j) % 30):
                        if l <= 5:
                            pixels[i + k, l + j] = ((i + k) / 4, 255, (l + j) / 4)
                if orientation == 1 :
                    if ((i+k)%30 >= (l+j)%30) :
                        pixels[i + k, l + j] = ((i + k)/4,255,(l + j)/4)
                if orientation == 2:
                    if ((k + l) > 30):
                        pixels[i + k, l + j] = ((i + k) / 4, 255, (l + j) / 4)
                if orientation == 3:
                    if ((k + l) < 30):
                        pixels[i + k, l + j] = ((i + k) / 4, 255, (l + j) / 4)

img.show()

img.save('stripes.jpeg','jpeg')