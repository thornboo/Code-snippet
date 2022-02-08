# 做练习的地方

import psutil

# 获取的盘符信息为字符串
value = psutil.disk_partitions()
for i in value:
    print(i.device, type(i.device))

# 定时器测试
import time

while 1 == 1:
    time.sleep(1)
    print('运行了')

# 获取系统时间
import datetime


def get_time():
    theTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return theTime


# 创建文件夹
import os

os.makedirs("D:\\zhaozhuang001\\zhao\\" + get_time())