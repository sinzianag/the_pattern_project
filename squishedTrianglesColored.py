from PIL import Image
import numpy as np
from random import randint

def getColor():
    randomColor = randint(0, 4)
    if randomColor == 0:
        color = (234, 96, 69)
    elif randomColor == 1:
        color = (248, 202, 77)
    elif randomColor == 2:
        color = (63, 86, 102)
    elif randomColor == 3:
        color = (47, 52, 64)
    elif randomColor == 4:
        color = (245, 229, 192)

    return color


img = Image.new( 'RGB', (1080,1080), "white") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0, img.size[0], 60):
    for j in range(0, img.size[1], 30):
        a = np.array([i,j+30])
        b = np.array([i+60,j])
        x = np.array([i+60,j+30])

        color = getColor()

        orientation = randint(0,3)
        for k in range(0,60) :
            for l in range(0,30) :
                if orientation == 0 :
                    if (((i+k)%60)/2 >= (l+j)%30) :
                        pixels[i + k, l + j] = color
                if orientation == 1 :
                    if (((i+k)%60)/2 < (l+j)%30) :
                        pixels[i + k, l + j] = color
                y = np.array([i+k,j+l])
                cp1 = np.cross(b-a,x-a)
                cp2 = np.cross(b-a,y-a)
                if np.dot(cp1,cp2) <= 0 :
                    if orientation == 2 :
                        pixels[i + k, l + j] = color
                else :
                    if orientation == 3 :
                        pixels[i + k, l + j] = color
img.show()

img.save('coloredSquished2.jpeg','jpeg')

