from PIL import Image
from pylab import *

im = array(Image.open('E:/python/Python Computer Vision/Image data/empire.jpg'))
print (im.shape, im.dtype)
im = array(Image.open('E:/python/Python Computer Vision/Image data/empire.jpg').convert('L'),'f')
print (im.shape, im.dtype)
