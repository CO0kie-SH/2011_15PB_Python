# os 模块提供了目录和文件能够执行的一些操作
import os

base = r'D:\OpenSSL\\'

# 通过循环获取到指定目录下的所有文件和文件夹
for name in os.listdir(base):
    # 判断目标名称是否为文件
    if os.path.isfile(base+name):
        # 输出文件名称以及后缀名
        print(os.path.splitext(name))