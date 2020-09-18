'''
Author: Goog Tech
Date: 2020-09-18 00:36:43
LastEditTime: 2020-09-18 18:09:29
Description: use a text of daily plans to generate a picture
Reference: https://blog.csdn.net/www89574622/article/details/87974931
Reference: https://selenium-python-zh.readthedocs.io/en/latest/locating-elements.html#class-name
Reference: https://blog.csdn.net/liudinglong1989/article/details/78731754?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.channel_param
'''

from selenium import webdriver
import time
from urllib import parse
import os
import shutil
import datetime

chromeFileDir = "C:\\Users\\Administrator.DESKTOP-3V51O0O\\Downloads\\"
thisMonthDir = os.getcwd() + "\\the template of daily plans for spe 2020\\"

# 打开模板文件
fo = open(thisMonthDir + "template-spe-2020.md", "r+", encoding='UTF-8')
# 读取文件内容
text = fo.read()
# 查看文件内容
print(text)
# 关闭打开的文件
fo.close()
# 初始化链接
url = "https://carbon.now.sh/?bg=rgba(126%2C211%2C33%2C1)&t=one-light&wt=none&l=text&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=4x&wm=false&code=" + parse.quote(text)

# 反解码查看结果格式是否正确
# print(parse.unquote(url))

# 点击网页中的下载按钮
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=opt)
driver.get(url)
driver.maximize_window()
time.sleep(1)
driver.find_element_by_class_name('jsx-1730877631 ').click()
print('ok: picture be downloaded successfully')
time.sleep(30) # 文件下载到本地需要时间滴

# 找到 Chrome 下载文件夹中最新下载的文件,并将其移动到当前文件夹中
fileList=os.listdir(chromeFileDir)
fileList.sort(key = lambda fn : os.path.getmtime(chromeFileDir + fn) if not os.path.isdir(chromeFileDir + fn) else 0)
updateTime = datetime.datetime.fromtimestamp(os.path.getmtime(chromeFileDir + fileList[-1])) # 获取文件时间
print('ok: new file name: ' + fileList[-1] + ",and update time: " + updateTime.strftime("%Y-%m-%d %H-%M-%S"))

# 移动文件
shutil.move(chromeFileDir + fileList[-1], thisMonthDir)
print('ok: picture be moved successfully')
