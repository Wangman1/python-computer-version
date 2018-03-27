from PIL import Image
from pylab import *

# 添加中文字体支持
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)
# 打开图像，并转成灰度图像
im = array(Image.open('E:/python/Python Computer Vision/Image data/empire.jpg').convert('L'))

# 新建一个图像
figure()
subplot(121)
# 不使用颜色信息
gray()
# 在原点的左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')
title(u'图像轮廓图', fontproperties=font)

subplot(122)
# 利用hist来绘制直方图
# 第一个参数为一个一维数组
# 因为hist只接受一维数组作为输入，所以要用flatten()方法将任意数组按照行优先准则转化成一个一维数组
# 第二个参数指定bin的个数
hist(im.flatten(), 128)
title(u'图像直方图', fontproperties=font)
# plt.xlim([0,250])
# plt.ylim([0,12000])

show()
