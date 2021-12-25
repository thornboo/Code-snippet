#自动登录QQ邮箱
from selenium import webdriver
import datetime
import time

start = time.perf_counter()


#阻止图片和css加载
options=webdriver.ChromeOptions()

prefs = {
	"profile.managed_default_content_settings.images": 2, #2是禁用的意思
	"permissions.default.stylesheet": 2
	}

options.add_experimental_option('prefs', prefs)

#在本地未添加环境变量时
driver = webdriver.Chrome(executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe", chrome_options=options)

#添加过环境变量时
driver = webdriver.Chrome()

#浏览器窗口全屏显示
driver.maximize_window()

#网址
url = "https://mail.qq.com"
driver.get(url)
driver.switch_to.frame('login_frame')

#通过id定位账号和密码元素
driver.find_element_by_id("u").send_keys("username")
driver.find_element_by_id("p").send_keys("password")

#点击确定按钮
driver.find_element_by_xpath('//*[@id="login_button"]').click()

#添加延迟
time.sleep(1)
print("标题为：",driver.title)

#添加延迟
time.sleep(1)

#通过title实现简单判断
if driver.title == "QQ邮箱":
    print("登录成功！\n")
else:
    print("登录失败！\n")

#点击收件箱
driver.find_element_by_id('folder_1').click()

#切换到收信iframe框架里
main_frame = driver.find_element_by_id('mainFrame')
driver.switch_to.frame(main_frame)

#进入邮件里面
driver.find_element_by_id('div_showtoday').click()


#获取邮件标题
subject = driver.find_element_by_id('subject').text

#获取邮件的内容
content = driver.find_element_by_id('mailContentContainer').text

print("邮件标题：", subject)

print("内容：", content)

#退出浏览器
driver.quit()
# driver.close()

end = time.perf_counter()

print("\n程序执行时间:", end - start, "秒。")
