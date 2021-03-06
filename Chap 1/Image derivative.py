from PIL import Image
from pylab import *
from scipy.ndimage import  filters
import numpy

# 添加中文字体支持
from matplotlib.font_manager import FontProperties
font=FontProperties(fname=r"c:\windows\fonts\SimSun.ttc",size=14)

im=array(Image.open('E:/python/Python Computer Vision/Image data/empire.jpg').convert('L'))
gray()

subplot(141)
axis('off')
title(u'(a)原图',fontproperties=font)
imshow(im)

# sobel derivative filters
imx=zeros(im.shape)
filters.sobel(im,1,imx)
subplot(142)
axis('off')
title(u'(b)x方向差分',fontproperties=font)
imshow(imx)

imy=zeros(im.shape)
filters.sobel(im,0,imy)
subplot(143)
axis('off')
title(u'(c)y方向差分',fontproperties=font)
imshow(imy)

mag=255-numpy.sqrt(imx**2+imy**2)
subplot(144)
title(u'(d)梯度幅值',fontproperties=font)
axis('off')
imshow(mag)

show()




