from PIL import Image
from random import randint

img = Image.new( 'RGB', (1080,1080), "white") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0, img.size[0], 30):
    for j in range(0, img.size[1], 30):
        orientation = randint(0,3)
        randomColor = randint(0, 5)
        if randomColor == 0:
            color = (0, 47, 50)
        elif randomColor == 1:
            color = (66, 130, 108)
        elif randomColor == 2:
            color = (165, 199, 127)
        elif randomColor == 3:
            color = (255, 200, 97)
        elif randomColor == 4:
            color = (200,70, 99)

        gradient = randint(0,2)

        if (i < 100) | (i > 900) | (j < 100) | (j > 900) :
            if gradient == 0 :
                color = (255,255,255)
            gradient = randint(0, 2)
            if gradient == 0:
                color = (255, 255, 255)
            gradient = randint(0, 2)
            if gradient == 0:
                color = (255, 255, 255)


        if (i < 200) | (i > 800) | (j < 200) | (j > 800):
            gradient = randint(0, 2)
            if gradient == 0:
                color = (255, 255, 255)

        if (i < 300) | (i > 700) | (j < 300) | (j > 700):
            gradient = randint(0, 2)
            if gradient == 0:
                color = (255, 255, 255)


        for k in range(0,30) :
            for l in range(0,30) :
                if orientation == 0 :
                    if ((i+k)%30 <= (l+j)%30) :
                        pixels[i + k, l + j] = color
                if orientation == 1 :
                    if ((i+k)%30 >= (l+j)%30) :
                        pixels[i + k, l + j] = color
                if orientation == 2:
                    if ((k + l) > 30):
                        pixels[i + k, l + j] = color
                if orientation == 3:
                    if ((k + l) < 30):
                        pixels[i + k, l + j] = color

img.show()

img.save('sparseTriangles.jpeg','jpeg')