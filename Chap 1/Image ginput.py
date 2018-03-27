from PIL import Image
from pylab import *

im = array(Image.open('E:/python/Python Computer Vision/Image data/empire.jpg'))
imshow(im)

print('Please click 3 points')
x = ginput(3)
print('you clicked:', x)
show()
