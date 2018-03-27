from PIL import Image
from pylab import *

# 添加中文字体支持
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)

# 读取图像到数组中
im = array(Image.open('E:/python/Python Computer Vision/Image data/empire.jpg'))
figure()

# 绘制有坐标轴的
subplot(121)
imshow(im)
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

# 使用红色星状标记绘制点
plot(x, y, 'r*')

# 绘制连接两个点的线（默认为蓝色）
plot(x[:2], y[:2])
title(u'绘制empire.jpg', fontproperties=font)

# 不显示坐标轴的
subplot(122)
imshow(im)
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

plot(x, y, 'r*')
plot(x[:2], y[:2])
axis('off')
title(u'绘制empire.jpg', fontproperties=font)

show()
# show()命令首先打开图形用户界面（GUI），然后新建一个窗口，该图形用户界面会循环阻断脚本，然后暂停，
# 直到最后一个图像窗口关闭。每个脚本里，只能调用一次show()命令，通常相似脚本的结尾调用。
