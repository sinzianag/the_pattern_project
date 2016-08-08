from PIL import Image
from random import randint

def getColor():
    randomColor = randint(0, 4)
    if randomColor == 0:
        color = (150, 206, 180)
    elif randomColor == 1:
        color = (255, 238, 173)
    elif randomColor == 2:
        color = (255, 111, 105)
    elif randomColor == 3:
        color = (255, 204, 92)

    return color

img = Image.new( 'RGB', (1080,1080), "white") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0, img.size[0], 30):
    for j in range(0, img.size[1], 30):

        color = getColor()

        if (i/30) % 2 == 0:
            orientation = (j/30) % 4;
        else :
            if (j / 30) % 4 == 0:
                orientation = 1
            if (j / 30) % 4 == 1 :
                orientation = 0
            if (j / 30) % 4 == 2:
                orientation = 3
            if (j / 30) % 4 == 3:
                orientation = 2
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

img.save('colorChevron.jpeg','jpeg')