from PIL import Image
import numpy as np

baseimg = Image.open('square.jpg')
basePixels = baseimg.load()
img = Image.new( 'RGB', (600,600), "white")
pixels = img.load()

for i in range(0, img.size[0], 60):
    for j in range(0, img.size[1], 30):
        a = np.array([i,j+30])
        b = np.array([i+60,j])
        x = np.array([i+60,j+30])
        if (i/60) % 2 == 0:
            orientation = (j/30) % 4;
        else :
            if (j / 30) % 4 == 0:
                orientation = 2
            if (j / 30) % 4 == 1 :
                orientation = 3
            if (j / 30) % 4 == 2:
                orientation = 0
            if (j / 30) % 4 == 3:
                orientation = 1
        for k in range(0,60) :
            for l in range(0,30) :
                if orientation == 0 :
                    if (((i+k)%60)/2 >= (l+j)%30) :
                        pixels[i + k, l + j] = basePixels[i + k, l + j]
                if orientation == 1 :
                    if (((i+k)%60)/2 < (l+j)%30) :
                        pixels[i + k, l + j] = basePixels[i + k, l + j]
                y = np.array([i+k,j+l])
                cp1 = np.cross(b-a,x-a)
                cp2 = np.cross(b-a,y-a)
                if np.dot(cp1,cp2) <= 0 :
                    if orientation == 2 :
                        pixels[i + k, l + j] = basePixels[i + k, l + j]
                else :
                    if orientation == 3 :
                        pixels[i + k, l + j] = basePixels[i + k, l + j]
                if k== 0 :
                    pixels[i + k, l + j] = basePixels[i + k, l + j]
img.show()

img.save('Squished3.jpeg','jpeg')

