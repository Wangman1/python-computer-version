import pickle
from PIL import Image
from numpy import *
from pylab import *
from PCV.tools import imtools,pca

# Uses sparse pca codepath

# 获取图像列表和尺寸
imlist=imtools.get_imlist('E:/python/Python Computer Vision/Image data/fontimages/a_thumbs')
# open ont image to get the size
im=array(Image.open(imlist[0]))
# get the size of the images
m,n=im.shape[:2]
# get the number of images
imnbr=len(imlist)
print("The number of images is %d" % imnbr)

# create matrix to store all flattened images
immatrix = array([array(Image.open(imname)).flatten() for imname in imlist],'f')

# PCA降维
V,S,immean=pca.pca(immatrix)

# 保存均值和主成分
#f = open('../ch01/font_pca_modes.pkl', 'wb')
#pickle.dump(immean,f)
#pickle.dump(V,f)
#f.close()

# Show the images (mean and 7 first modes)
# This gives figure 1-8 (p15) in the book.

figure()
gray()
subplot(241)
axis('off')
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n))
    axis('off')

show()

