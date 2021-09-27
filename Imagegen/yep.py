# A class which will generate an image and weite that image to a file
import random, functools, math, os
from cv2 import imread, imwrite


class CreateImage():
    def __init__(self, fileLocation, h=640, w=480):
        self.filePath = fileLocation
        self.height = h
        self.width = w

    def save(self):
        print("Saving...")
        f = open(self.filePath, "w")
        f.write("P3\n")
        f.write(str(self.width) + " " + str(self.height) + "\n")
        f.write("255\n")
        for row in self.pixels:
            for col in row:
                for color in col:
                    f.write(str(color) + " ")
                f.write("  ")
            f.write("\n")
        f.close()
        print("Finished")

    def generateRandom(self):
        # Grid of pixels
        self.pixels = []
        print("Generating file...")
        for i in range(0, self.height):
            self.pixels.append([])
            for j in range(0, self.width):
                b = round(((math.sin((2.8*j*math.pi) / 180))**2) * 255)
                r,g= 0,0
                self.pixels[i].append([r,g,b])

        # Save a pixel
        self.save()

path = os.path.abspath("demo.ppm")
image = CreateImage(path, 256, 256)
image.generateRandom()

f = imread(path)
imwrite(os.path.abspath("demo.jpg"), f)

#1
# r,g,b = 0,0,0

#2
# r,g,b = 0,0,255

#3
# r= 255-i
# g,b = 0,0

#4
# g = j
# r,b = 0,0

#5
# b = 255 - j
# r,g = 0,0

#6
#b = 255-i
#g = j
#r = 0 

#7
# b = 2*j if 2*j <= 255 else 0
# r,g = 0,0

#8
# b = 2*j if 2*j <=255 else 255 - 2*j % 255
# r,g = 0,0

#9
# r = 255 - int(2.95*float(i)) % 255
# g,b = 0,0

#10
# b = (4*j) % 255
# r,g = 0,0

#11 SIN SOLUTION 
# b = round(((math.sin((2.8*j*math.pi) / 180))**2) * 255)
# r,g = 0,0