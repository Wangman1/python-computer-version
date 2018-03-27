from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters

# 添加中文字体支持
from matplotlib.font_manager import FontProperties
font=FontProperties(fname=r"c:\windows\fonts\SimSun.ttc",size=14)

im=array(Image.open('E:/python/Python Computer Vision/Image data/empire.jpg').convert('L'))

figure()
gray()
axis('off')
subplot(141)
axis('off')
title(u'原图',fontproperties=font)
imshow(im)

for bi,blur in enumerate([2,5,10]):
    im2=zeros(im.shape)
    im2=filters.gaussian_filter(im,blur)
    im2=np.uint8(im2)
    imNum=str(blur)
    subplot(1,4,2+bi)
    axis('off')
    title(u'标准差为'+imNum,fontproperties=font)
    imshow(im2)

#如果是彩色图像，则分别对三个通道进行模糊
#for bi, blur in enumerate([2, 5, 10]):
#  im2 = zeros(im.shape)
#  for i in range(3):
#    im2[:, :, i] = filters.gaussian_filter(im[:, :, i], blur)
#  im2 = np.uint8(im2)
#  subplot(1, 4,  2 + bi)
#  axis('off')
#  imshow(im2)

show()