# -*- coding:utf-8 -*-
import csv


# 向csv文件中写入数据
def csvWrite():
    with open('score.csv', 'a+', newline="") as csvData:
        csv_write = csv.writer(csvData, dialect="excel")
        value = input("是否写入数据：")
        while value == "yes":
            name = input("科目名称：")
            credit = input("标定学分：")
            point = input("成绩绩点：")
            score = input("所得分数：")
            csv_write.writerow([name, credit, point, score])
            value = input("是否继续：")


# 读取csv数据并计算结果
def csvRead():
    average_point = sum_credit = temp = 0
    with open("score.csv", 'r') as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            if line[0] == "科目名称":
                continue
            temp = temp + 1
            sum_credit = float(line[1]) + sum_credit
            average_point = float(line[1]) * float(line[2]) + average_point
        print("统计科目数目：", temp)
        print("已修学分：", sum_credit)
        print("成绩绩点为：", '%.3f' % (average_point / sum_credit))
        input("是否继续：")


if __name__ == "__main__":
    csvWrite()
    csvRead()
