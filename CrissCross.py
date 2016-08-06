from PIL import Image
from random import randint

img = Image.new( 'RGB', (1080,1080), "white") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0, img.size[0], 30):
    for j in range(0, img.size[1], 30):
        if (i/30) % 2 == 0:
            orientation = (j/30) % 4;
        else :
            if (j / 30) % 4 == 0:
                orientation = 1
            if (j / 30) % 4 == 1 :
                orientation = 2
            if (j / 30) % 4 == 2:
                orientation = 3
            if (j / 30) % 4 == 3:
                orientation = 0
        for k in range(0,30) :
            for l in range(0,30) :
                if orientation == 0 :
                    if ((i+k)%30 <= (l+j)%30) :
                        pixels[i + k, l + j] = ((i + k)/4,255,(l + j)/4)
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

img.save('dwada.jpeg','jpeg')