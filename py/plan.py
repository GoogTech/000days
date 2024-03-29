'''
Author: Goog Tech
Date: 2020-09-18 00:36:43
LastEditTime: 2020-09-23 16:54:19
Description: one command one plan
Reference: https://www.jianshu.com/p/bca94c3dbdf4
Reference: https://docs.python.org/2/library/optparse.html
Reference: https://www.cnpython.com/qa/55055
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
import optparse
from termcolor import cprint

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
            self.coverPicDownloadPath = self.projectPath + "\\themes\\zhaoo\\source\\images\\2020\\100DaysOfPlan\\" + coverPic
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
      def moveFile(self, coverPicName):
            # 找到 Chrome 下载文件夹中最新下载的文件,并将其移动到当前文件夹中
            fileList = os.listdir(self.chromeDownloadPath)
            fileList.sort(key = lambda fn : os.path.getmtime(self.chromeDownloadPath + fn) if not os.path.isdir(self.chromeDownloadPath + fn) else 0)
            updateTime = datetime.datetime.fromtimestamp(os.path.getmtime(self.chromeDownloadPath + fileList[-1])) # 获取文件时间
            print('✅: the newest file name: ' + fileList[-1] + " and created time: " + updateTime.strftime("%Y-%m-%d %H-%M-%S") + '\n')
            # 移动并重命名文件
            shutil.move(self.chromeDownloadPath + fileList[-1], self.mkdir(self.coverPicDownloadPath) + '\\' + coverPicName + '.png')
            print('✅: file be renamed successfully and new name: ' + coverPicName + '.png')
            print('✅: picture be moved successfully \n')

      ''' 根据博客模板文件中的内容生成博客封面图片 '''
      def generateCoverPic(self, coverPicName):
            self.readTemplate(self.coverTemplatePath)
            self.clickButton()
            self.moveFile(coverPicName)
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
            # 当 "日计划模板文件" 中有中文或特殊符号时则会抛出如下异常: 
            # UnicodeDecodeError: 'gbk' codec can't decode byte 0xac in position 175: illegal multibyte sequence
            # 解决方案如下:  
            # https://stackoverflow.com/a/33291200/13689597
            # https://github.com/tanepiper/SublimeText-Nodejs/issues/64#issuecomment-305839994
            
            # 运行 Hexo 本地测试命令
            print(subprocess.getoutput('hexo clean'))
            print('✅: the command of <hexo clean> be executed successfully \n')
            # print(subprocess.getoutput('hexo generate'))
            subprocess.Popen('hexo generate', shell=True, universal_newlines = False)
            print('✅: the command of <hexo generate> be executed successfully \n')
            # Hexo服务器的启动不能占用当前进行,易卡顿,所以需创建一个子进程
            subprocess.Popen('hexo s', shell=True)
            # 打开网页
            webbrowser.open(self.hexoLocalServerUrl)

      ''' GitHub 提交程序 '''
      def gitPush(self, commitMsg):
            time.sleep(30)
            # git add --all
            subprocess.getoutput('git add -A')
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
      def run(self, coverTemplateFileName, coverPicName, coverBgColor, moveCoverToDir,
       newHexoPostTitle, planTemplateFileName, gitCommitMsg):
          tool = Tools(coverTemplateFileName, moveCoverToDir, coverBgColor)
          # 生成文章封面图,传入参数为: 模板文件,用于存储封面图片的文件夹,封面背景颜色
          tool.generateCoverPic(coverPicName) # 应该将上述的三个参数传入到 generateCoverPic() 函数中
          print('⚡: generated a cover picture successfully \n\n\n\n')
          # 生成 Hexo 博文,传入参数为:新文章的标题,日计划模板文件
          tool.hexoNew(newHexoPostTitle, planTemplateFileName)
          print('⚡: created a new hexo post successfully \n\n\n\n')
          # 运行 Hexo 本地测试程序,即运行命令 hexo clean & hexo generate && hexo server
          tool.hexoTesting()
          print('⚡: hexo cleaned && generated and runed hexo server successfully \n\n\n\n')
          # 将新添加的文件 Push 到远程 Github Repo, 参入的参数为 commit 的说明信息
          tool.gitPush(gitCommitMsg)
          print('⚡: push these new files to github successfully')
          print('⚡: Nice ! Everything be done successfully, See you again bro.')

      ''' 接收用户输入的参数,然后运行程序 '''
      def initParameter(self):
            parser = optparse.OptionParser("usage: %prog -coverTemplateFileName <coverTemplateFileName> -coverPicName <coverPicName> -moveCoverToDir <moveCoverToDir> -planTemplateFileName <planTemplateFileName> -hexoPostTitle <hexoPostTitle> -gitCommitMsg <gitCommitMsg>")
            parser.add_option('--ct', '--coverTemplate', dest='coverTemplateFileName', type='string', help='please enter the file name of cover template')
            parser.add_option('--cn', '--coverPicName', dest='coverPicName', type='string', help='please enter the name of cover picture')
            parser.add_option('--bg', '--coverBgColor', dest='coverBgColor', type='string', help='please enter the background color of cover image')
            parser.add_option('--cd', '--moveCoverToDir', dest='moveCoverToDir', type='string', help='please enter the dir name of cover image')
            parser.add_option('--pt', '--planTemplateFileName', dest='planTemplateFileName', type='string', help='please enter the file name of plan template')
            parser.add_option('--ht', '--hexoPostTitle', dest='hexoPostTitle', type='string', help='please enter the title of hexo post')
            parser.add_option('--cm', '--gitCommitMsg', dest='gitCommitMsg', type='string', help='please enter the git commit message')
            (options, args) = parser.parse_args()
            if (options.coverTemplateFileName == None) | (options.coverPicName == None ) | (options.coverBgColor == None) | (options.moveCoverToDir == None) | (options.planTemplateFileName == None) | (options.hexoPostTitle == None) | (options.gitCommitMsg == None):
                  print(parser.usage)
                  exit(0)
            else:
                  coverTemplateFileName = options.coverTemplateFileName
                  coverPicName = options.coverPicName
                  coverBgColor = options.coverBgColor
                  moveCoverToDir = options.moveCoverToDir
                  planTemplateFileName = options.planTemplateFileName
                  hexoPostTitle = options.hexoPostTitle
                  gitCommitMsg = options.gitCommitMsg
            Tools('', '', 'white').logo() # 输出 logo 样式
            print('\n\n\ncheck the parameters you entered: ')
            print('🔎: coverTemplateFileName : ' + coverTemplateFileName)
            print('🔎: coverPicName : ' + coverPicName)
            print('🔎: coverBgColor : ' + coverBgColor)
            print('🔎: moveCoverToDir : ' + moveCoverToDir)
            print('🔎: planTemplateFileName : ' + planTemplateFileName)
            print('🔎: hexoPostTitle : ' + hexoPostTitle)
            print('🔎: gitCommitMsg : ' + gitCommitMsg + '\n\n\n')
            # run : 应该将 Tools() 中的三个参数写到 generateCoverPic() 函数中
            # Tools('coverTemplate.md', 'Day003', 'brown').run('coverTemplate.md', 'brown', 'Day003', 'hexo-new-post-0045', 'template-spe-2020-ch.md', '🚨 testing : this is git commit message')
            Tools(coverTemplateFileName, moveCoverToDir, coverBgColor).run(coverTemplateFileName, coverPicName, coverBgColor, moveCoverToDir, hexoPostTitle, planTemplateFileName, gitCommitMsg)
            print('⚡ exited\n\n\n')

      ''' 将 logo 样式输出到控制台 '''
      def logo(self):   
            cprint('                                                                          ')
            cprint(' __  ___   ___        _                          __         _             ', 'cyan', attrs=['bold'])
            cprint('/_ |/ _ \ / _ \      | |                        / _|       | |            ', 'cyan', attrs=['bold'])
            cprint(' | | | | | | | |   __| | __ _ _   _ ___    ___ | |_   _ __ | | __ _ _ __  ', 'cyan', attrs=['bold'])
            cprint(' | | | | | | | |  / _` |/ _` | | | / __|  / _ \|  _| |  _ \| |/ _` |  _ \ ', 'yellow', attrs=['bold'])
            cprint(' | | |_| | |_| | | (_| | (_| | |_| \__ \ | (_) | |   | |_) | | (_| | | | |', 'yellow', attrs=['bold'])
            cprint(' |_|\___/ \___/   \__,_|\__,_|\__, |___/  \___/|_|   | .__/|_|\__,_|_| |_|', 'green', attrs=['bold'])
            cprint('                               __/ |                 | |                  ', 'green', attrs=['bold'])
            cprint('                              |___/                  |_|                  ', 'green', attrs=['bold'])
            cprint('                                                                          ')
            cprint('                                        Author: GoogTech And Version: v1.0', 'red')
            cprint('                            GitHub: https://github.com/YUbuntu0109/000days', 'red')   
            cprint('                                                                          ')                                                

# 运行程序, 其执行步骤及其核心功能说明如下所示(注意: 其中向 Tools() 中传入的三个参数时多余的,记得重构代码哟) : 
# 1. 将封面模板文件中的内容,及接收的样式参数拼接到 url, 然后打开浏览器并将该请求发送给 https://carbon.now.sh, 进而生成相应的图片.
# 2. 通过 chromeDriver 将 https://carbon.now.sh 网页生成封面图下载到本地, 然后将其重命名并移动到指定文件夹.
# 3. 根据接收的 hexo-post-title 等参数生成对应标题的博客文章, 然后将当月日计划模板中的内容(即今日的打卡内容)写入到该文章中.
# 4. 执行 hexo clean && hexo generate && hexo server, 然后打开浏览器并跳转到 http://127.0.0.1:4000 进行博文测试及预览.
# 5. 执行 git add -A && git commit -m && git pull origin Hexobackup, 即将本地新添加的博文及其封面图推送到远程 GitHub 仓库.
# 6. 最后博客网站的部署工作由已经集成到 GitHub 仓库的 Travis CI/CD 来完成, 至此发布及部署新博文的工作已全部完成 !
# Tools('coverTemplate.md', 'Day999', 'white').initParameter()
Tools('', '', 'white').initParameter()
