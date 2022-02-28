import os
import imageio

myfile = os.listdir('paint')
images = []
for i in range(len(myfile)):
    image = imageio.imread('paint/' + myfile[i])
    images.append(image)

imageio.mimsave('paint.gif' , images)