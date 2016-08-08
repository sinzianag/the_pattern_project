from PIL import Image
from random import randint

img = Image.new( 'RGB', (1080,1080), "white") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0, img.size[0], 30):
    for j in range(0, img.size[1], 30):
        orientation = randint(0,3)
        colorRand = randint(0,1)
        color = (0,67,88)
        for k in range(0,30) :
            pixels[i, j+k] = (255, 255, 255)
            for l in range(0,30) :
                pixels[i + l, j] = (255, 255, 255)
                if orientation == 0 :
                    if colorRand == 0 :
                        if ((k <= 10) & (l <= 10)) :
                            pixels[i + k, l + j] = color
                    else :
                        if ((k >= 10) | (l >= 10)):
                            pixels[i + k, l + j] = color
                if orientation == 1 :
                    if colorRand == 0:
                        if ((k <= 10) & (l >= 20)):
                            pixels[i + k, l + j] = color
                    else:
                        if ((k >= 10) | (l <= 20)):
                            pixels[i + k, l + j] = color
                if orientation == 2:
                    if colorRand == 0:
                        if ((k >= 20) & (l >= 20)):
                            pixels[i + k, l + j] = color
                    else:
                        if ((k <= 20) | (l <= 20)):
                            pixels[i + k, l + j] = color
                if orientation == 3:
                    if colorRand == 0:
                        if ((k >= 20) & (l <= 10)):
                            pixels[i + k, l + j] = color
                    else:
                        if ((k <= 20) | (l >= 10)):
                            pixels[i + k, l + j] = color

img.show()

img.save('smallSquareLittleSquare.jpeg','jpeg')