import os
def ger_imlist(path):
    """返回目录中所有JPG图像的文件名列表"""
    return[os.path.join(path,f)for f in os.listdir(path) if f.endswith('.jpg')]

