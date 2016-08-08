from PIL import Image
from random import randint

img = Image.new( 'RGB', (1080,1080), "white") # create a new black image
pixels = img.load() # create the pixel map

f = open ( 'matrix.txt' , 'r')
matrix = [ map(int,line.split(' ')) for line in f if line.strip() != "" ]

for i in range(0, img.size[0], 30):
    for j in range(0, img.size[1], 30):
        orientation = randint(0,3)
        for k in range(0,30) :
            for l in range(0,30) :
                if orientation == 0 :
                    if (matrix[k][l] == 0) :
                        pixels[i + k, l + j] = ((i + k)/4,255,(l + j)/4)
                if orientation == 1 :
                    if (matrix[l][k] == 0):
                        pixels[i + k, l + j] = ((i + k) / 4, 255, (l + j) / 4)
                if orientation == 2:
                    if (matrix[29-k][l] == 0):
                        pixels[i + k, l + j] = ((i + k) / 4, 255, (l + j) / 4)
                if orientation == 3:
                    if (matrix[k][29-l] == 0):
                        pixels[i + k, l + j] = ((i + k) / 4, 255, (l + j) / 4)

img.show()

img.save('strips.jpeg','jpeg')
