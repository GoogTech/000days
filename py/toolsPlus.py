'''
Author: Goog Tech
Date: 2020-09-18 00:36:43
LastEditTime: 2020-09-21 00:37:39
Description: use a text of daily plans to generate a picture (v 2.0)
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
import subprocess
import webbrowser

class Tools:

      ''' 初始化文件路径及请求链接 '''
      def __init__(self, coverTemplate, coverPic, coverBackground):
            # Hexo 本地测试链接
            self.hexoLocalServerUrl = 'http://127.0.0.1:4000'
            # 获取当前目录的上级目录,即项目目录
            self.projectPath = os.path.abspath(os.path.dirname(os.getcwd())) 
            # 谷歌浏览器的文件下载路径
            self.chromeDownloadPath = 'C:\\Users\\Administrator.DESKTOP-3V51O0O\\Downloads\\'
            # Hexo 文章源文件的文件夹路径
            self.hexoPostPath = self.projectPath + "\\source\\_posts\\"
            # 封面模板存储路径
            self.coverTemplatePath = self.projectPath + "\\template\\" + coverTemplate
            # 当月日计划模板路径
            self.planTemplatePath = self.projectPath + "\\template\\daily-plans-for-spe-2020\\"
            # 封面图片存储路径
            self.coverPicDownloadPath = self.projectPath + "\\themes\\zhaoo\\source\\images\\2020\\" + coverPic
            # https://carbon.now.sh/ 固定样式的请求地址
            rgba = self.bg()
            self.requestUrl = "https://carbon.now.sh/?bg=" + rgba[coverBackground] + "&t=one-light" \
                              "&wt=none&l=application%2Fx-sh&ds=true&dsyoff" \
                              "=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px" \
                              "&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=4x&wm" \
                              "=false&code="

      ''' 根据颜色选择指定的封面背景 '''
      def bg(self):
            rgba = {}
            rgba['cyan'] = 'rgba(126%2C211%2C33%2C1)' # 青色
            rgba['purple'] = 'rgba(189%2C16%2C224%2C1)' # 紫色
            rgba['yellow'] = 'rgba(248%2C231%2C28%2C1)' # 黄色
            rgba['blue'] = 'rgba(80%2C227%2C194%2C1)' # 蓝色
            rgba['white'] = 'rgba(255%2C255%2C255%2C1)' #白色
            rgba['red'] = 'rgba(208%2C2%2C27%2C1)' #红色
            rgba['brown'] = 'rgba(245%2C166%2C35%2C1)' #棕色
            return rgba

      ''' 读取博客封面的模板文件 '''
      def readTemplate(self, filePath):
            try:
                  # fo = open(self.coverTemplatePath, "r+", encoding='UTF-8')  # 打开博客封面图的模板文件
                  fo = open(filePath, "r+", encoding='UTF-8')  # 打开博客封面图的模板文件
                  content = fo.read() # 读取文件内容
                  print('✅: check out the template of daily plans: \n'+ content + '\n') # 查看文件内容
                  return content; # 返回结果
                  fo.close() # 关闭连接
            except FileNotFoundError as e: print('❌: not found the coverTemplatePath \n')

      ''' 读取当月日计划模板中的内容,并将其写入到新生成的 Hexo 文章中 '''
      def writeTemplate(self, filePath, conent):
            try:
                  fo = open(filePath, "w", encoding='UTF-8') # fo = open(filePath, "a", encoding='UTF-8') : 为追加写入模式
                  fo.write(conent)
                  fo.close()
                  return True
            except FileNotFoundError as e: print('❌: not found the filePath \n')

      ''' 点击网页中图片的下载按钮 '''      
      def clickButton(self):
            # 初始化 https://carbon.now.sh/ 网站链接
            url = self.requestUrl + parse.quote(self.readTemplate(self.coverTemplatePath))
            # 反解码查看结果格式是否正确
            print('✅: check out resquest url: \n'+ parse.unquote(url) + '\n')
            # 点击网页中的图片下载按钮
            opt = webdriver.ChromeOptions()
            driver = webdriver.Chrome(options = opt)
            driver.get(url)
            driver.maximize_window()
            time.sleep(1)
            driver.find_element_by_class_name('jsx-1730877631 ').click()
            print('✅: picture be downloaded successfully \n')
            # 图片下载到本地需要时间哟
            time.sleep(30)

      ''' 创建指定路径的文件夹 '''
      def mkdir(self, path):
            path = path.strip() # 去除首位空格
            path = path.rstrip("\\") # 去除尾部 \ 符号
            isExist = os.path.exists(path) # 判断路径是否存在
            if not isExist:
                  try:
                        os.mkdir(path) # 创建该目录
                        print("✅: path be crated: " + path + '\n')
                        return path
                  except FileNotFoundError as e: print('❌: not found the coverPicDownloadPath \n')
            else: return path

      '''  将下载的图片移动到指定路径 '''
      def moveFile(self):
            # 找到 Chrome 下载文件夹中最新下载的文件,并将其移动到当前文件夹中
            fileList = os.listdir(self.chromeDownloadPath)
            fileList.sort(key = lambda fn : os.path.getmtime(self.chromeDownloadPath + fn) if not os.path.isdir(self.chromeDownloadPath + fn) else 0)
            updateTime = datetime.datetime.fromtimestamp(os.path.getmtime(self.chromeDownloadPath + fileList[-1])) # 获取文件时间
            print('✅: new file name: ' + fileList[-1] + " and created time: " + updateTime.strftime("%Y-%m-%d %H-%M-%S") + '\n')
            # 移动文件
            shutil.move(self.chromeDownloadPath + fileList[-1], self.mkdir(self.coverPicDownloadPath))
            print('✅: picture be moved successfully \n')

      ''' 根据博客模板文件中的内容生成博客封面图片 '''
      def generateCoverPic(self):
            self.readTemplate(self.coverTemplatePath)
            self.clickButton()
            self.moveFile()
            print('✅: had done and exited \n')

      ''' 创建今日打卡文章,并将这个月的日计划模板内容读取到此文件中 '''
      def hexoNew(self, postName, planTemplate):
            # same as execute the command: hexo new 'new-post-name'
            print(subprocess.getoutput('hexo new ' + postName))
            print('✅: new post be created successfully and title is: ' + postName + '\n')
            # 读取当月每日计划模板文件,并将其内容写入到当前创建的 postName 文章中
            planTemplate = self.planTemplatePath + planTemplate
            templateContent = self.readTemplate(planTemplate)
            newHexoPostPath = self.hexoPostPath + postName + ".md"
            self.writeTemplate(newHexoPostPath, templateContent)
            print('✅: writed the content of plan template to the <'+ postName +'> succesffully \n')

      ''' Hexo 本地测试程序 '''
      def hexoTesting(self):
            # 运行 Hexo 本地测试命令
            print(subprocess.getoutput('hexo clean'))
            print('✅: the command of <hexo clean> be executed successfully \n')
            print(subprocess.getoutput('hexo generate'))
            print('✅: the command of <hexo generate> be executed successfully \n')
            # Hexo服务器的启动不能占用当前进行,易卡顿,所以需创建一个子进程
            subprocess.Popen('hexo s', shell=True)
            # 打开网页
            webbrowser.open(self.hexoLocalServerUrl)

      ''' GitHub 提交程序 '''
      def gitPush(self, commitMsg):
            time.sleep(30)
            subprocess.getoutput('git add -A') # <git add *> same as <git add -A> ?
            print('\n\n\n✅: the command of <git add -A> be executed successfully \n')
            # git commit -a -m "this is commit infos"
            subprocess.getoutput('git commit -m' + ' " ' + commitMsg + ' " ')
            print('✅: the command of <git commit - m "commitMsg"> be executed successfully \n')
            # git push origin Hexobackup
            subprocess.Popen('git push origin Hexobackup', shell = True)
            print('✅: the command of <git push origin Hexobackup> be executed successfully \n')
            # git log -3
            subprocess.Popen('git log -3', shell = True)

      ''' run '''
      def run(self, coverTemplateFileName, coverBgColor, moveCoverToDir,
       newHexoPostTitle, planTemplateFileName, gitCommitMsg):
          tool = Tools(coverTemplateFileName, moveCoverToDir, coverBgColor)
          tool.generateCoverPic() # 应该将上述的三个参数传入到 generateCoverPic() 函数中
          print('⚡: generated a cover picture successfully \n\n\n\n')
          tool.hexoNew(newHexoPostTitle, planTemplateFileName)
          print('⚡: created a new hexo post successfully \n\n\n\n')
          tool.hexoTesting()
          print('⚡: hexo cleaned && generated and runed hexo server successfully \n\n\n\n')
          tool.gitPush(gitCommitMsg)
          print('⚡: push these new files to github successfully')
          print('⚡: Nice ! Everything be done successfully and exited, See you again bro. \n\n\n')
            
# tool = Tools('coverTemplate.md', 'Day100', 'red') 

# # 生成文章封面图,传入参数为: 模板文件,用于存储封面图片的文件夹,封面背景颜色
# tool.generateCoverPic()

# # 生成 Hexo 博文,传入参数为:新文章的标题,日计划模板文件
# tool.hexoNew('hexo-new-post-1909', 'template-spe-2020-ch.md')

# # 运行 Hexo 本地测试程序,即运行命令 hexo clean & hexo generate && hexo server
# tool.hexoTesting()

# # 将新添加的文件 Push 到远程 Github Repo, 参入的参数为 commit 的说明信息
# tool.gitPush("update tools.py")

# run : 应该将 Tools() 中的三个参数写到 generateCoverPic() 函数中
# how to run:
# Administrator@191114gm MINGW64 /f/Git/workbench/workbench-github-website/000days/py (Hexobackup)
# $ python toolsPlus.py 
Tools('coverTemplate.md', 'Day002', 'white').run('coverTemplate.md', 'white', 'Day002', 'hexo-new-post-0031', 'template-spe-2020-ch.md', '🚨 testing : this is git commit message')
