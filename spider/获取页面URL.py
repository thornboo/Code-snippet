import requests
import re

#获取页面全部HTML信息
res = requests.get('https://www.runoob.com/')
res.encoding = 'utf-8'
html = res.text
#print(html)

#将HTML信息写入文件
f = open(r"D:\web_html.txt",'w+',encoding="utf-8") #w+:追以加方式打开文件
f.write(html)
f.close()

#读取HTML信息
f = open(r"D:\web_html.txt",'r+',encoding="utf-8") #r+:以读写方式打开文件
data = f.read() #data是字符串对象


res_h4 =  r"<h4>(.+?)</h4>"
value = re.findall(res_h4 , data, re.I|re.S|re.M)
for a in value:
    print(a)

#关闭文件
f.close()