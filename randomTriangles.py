from PIL import Image
import numpy as np
from random import randint

def sameSide(p1,p2,a,b):
    cp1 = np.cross(b-a,p1-a)
    cp2 = np.cross(b-a,p2-a)
    if np.dot(cp1,cp2) >= 0 :
        return True
    return False

def pointInTriangle(p,a,b,c) :
    if sameSide(p,a,b,c) & sameSide(p,b,a,c) &  sameSide(p,c,a,b) :
        return True
    return False

def getColor():
    randomColor = randint(0, 3)
    if randomColor == 0:
        color = (198, 224, 112)
    elif randomColor == 1:
        color = (145, 196, 108)
    elif randomColor == 2:
        color = (40, 125, 125)
    elif randomColor == 3:
        color = (28, 52, 76)
    elif randomColor == 4:
        color = (245, 229, 192)

    return color

img = Image.new( 'RGB', (1080,1080), "white") # create a new black image
pixels = img.load() # create the pixel map

for i in range(0, img.size[0], 60):
    for j in range(0, img.size[1], 60):
        a = np.array([i + 4 + randint(0,50), j + 4 +  randint(0,50)])
        b = np.array([i + 4 + randint(0,50), j + 4 +  randint(0,50)])

        x = np.array([i + 4 + randint(0,50), j + 4 +  randint(0,50)])

        color = getColor()

        for k in range(0,60) :
            for l in range(0,60) :
                y = np.array([i+k,j+l])
                if pointInTriangle(y,x,a,b) :
                    pixels[i + k, l + j] = color

img.show()

img.save('randomTriangles4.jpeg','jpeg')


