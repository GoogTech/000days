<p align="center">
	<a href="https://000days.com/">
        <img src="https://000days.com/images/000days-logo.PNG" width="800">
    </a>
</p>

# One Command One Plan

## How To Run
<details>
    <summary>python plan.py --help</summary>

    ```shell
    Administrator@191114gm MINGW64 /f/Git/workbench/workbench-github-website/000days/py (Hexobackup)
    $ python plan.py --help

    Usage: plan.py -coverTemplateFileName <coverTemplateFileName> -coverPicName <coverPicName> -moveCoverToDir <moveCoverToDir> -planTemplateFileName <planTemplateFileName> -hexoPostTitle <hexoPostTitle> -gitCommitMsg <gitCommitMsg>

    Options:
    -h, --help            show this help message and exit
    --ct=COVERTEMPLATEFILENAME, --coverTemplate=COVERTEMPLATEFILENAME
                            please enter the file name of cover template
    --cn=COVERPICNAME, --coverPicName=COVERPICNAME
                            please enter the name of cover picture
    --bg=COVERBGCOLOR, --coverBgColor=COVERBGCOLOR
                            please enter the background color of cover image
    --cd=MOVECOVERTODIR, --moveCoverToDir=MOVECOVERTODIR
                            please enter the dir name of cover image
    --pt=PLANTEMPLATEFILENAME, --planTemplateFileName=PLANTEMPLATEFILENAME
                            please enter the file name of plan template
    --ht=HEXOPOSTTITLE, --hexoPostTitle=HEXOPOSTTITLE
                            please enter the title of hexo post
    --cm=GITCOMMITMSG, --gitCommitMsg=GITCOMMITMSG
                            please enter the git commit message
    ```
</details>


## Example : How To Create New Post
<details>
    <summary>first step : modify the template file of cover</summary>

    ```shell
    template/coverTemplate.md
    ```
</details>
<details>
    <summary>second step : modify the template file of daily plan</summary>

    ```shell
    template/daily-plans-for-spe-2020/template-spe-2020-ch.md
    ```
</details>
<details>
    <summary>third step : run plan.py and init the necessary parameters</summary>

    ```shell
    Administrator@191114gm MINGW64 /f/Git/workbench/workbench-github-website/000days/py (Hexobackup)
    $ python plan.py --ct coverTemplate.md --cn cover$ python plan.py --ct coverTemplate.md --cn coverPic --bg red --cd Day000 --pt template-spe-2020-ch.md --ht hexo-new-post-000 --cm testing\ :\ this\ is\ commit\ message
                                                                            
    __  ___   ___        _                          __         _             
    /_ |/ _ \ / _ \      | |                        / _|       | |            
    | | | | | | | |   __| | __ _ _   _ ___    ___ | |_   _ __ | | __ _ _ __  
    | | | | | | | |  / _` |/ _` | | | / __|  / _ \|  _| |  _ \| |/ _` |  _ \ 
    | | |_| | |_| | | (_| | (_| | |_| \__ \ | (_) | |   | |_) | | (_| | | | |
    |_|\___/ \___/   \__,_|\__,_|\__, |___/  \___/|_|   | .__/|_|\__,_|_| |_|
                                __/ |                 | |                  
                                |___/                  |_|                  
                                                                            
                                            Author: GoogTech And Version: v1.0
                                GitHub: https://github.com/YUbuntu0109/000days
                                                                            



    check the parameters you entered:
    🔎: coverTemplateFileName : coverTemplate.md
    🔎: coverPicName : coverPic
    🔎: coverBgColor : red
    🔎: moveCoverToDir : Day000
    🔎: planTemplateFileName : template-spe-2020-ch.md
    🔎: hexoPostTitle : hexo-new-post-000
    🔎: gitCommitMsg : testing : this is commit message



    ✅: check out the template of daily plans:
    🎉 Day 000 of plan

    ✅: check out the template of daily plans:
    🎉 Day 000 of plan

    ✅: check out resquest url:
    https://carbon.now.sh/?bg=rgba(208,2,27,1)&t=one-light&wt=none&l=application/x-sh&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&pl=1&fm=Hack&fs=14px&lh=143%&si=false&es=4x&wm=false&code=🎉 Day 000 of plan


    DevTools listening on ws://127.0.0.1:50360/devtools/browser/766e1f03-cfa9-4ed7-81db-d32de9a2302b
    ✅: picture be downloaded successfully 

    ✅: the newest file name: carbon.png and created time: 2020-09-21 15-47-00

    ✅: file be renamed successfully and new name: coverPic.png

    ✅: picture be moved successfully

    ✅: had done and exited

    ⚡: generated a cover picture successfully 




    (node:10136) ExperimentalWarning: The fs.promises API is experimental
    INFO  Validating config
    INFO  Created: F:\Git\workbench\workbench-github-website\000days\source\_posts\hexo-new-post-000.md
    ✅: new post be created successfully and title is: hexo-new-post-000

    ✅: check out the template of daily plans:
    ---
    title: hexo-new-post-000
    date: 2020-09-21 15:37:40
    image: /images/2020/Day000/coverPic.png
    tags: Testing Blog
    ---

    ## For Testing
    📝 2020年年 9月份日计划表的模板文件如下所示示,坚持住住 !

    🎉 第 000天自律打卡卡 !
    #100DaysOfCode
    #100DaysOfEnglish
    #100DaysOfFitness


    ✅ 1. 早晨 5 点起床

    ✅ 2. 晨跑 5 公里

    ✅ 3. 平板支撑 15 分钟( 早晨 )

    ✅ 4. 腹肌训练 19 分钟( 早晨 )

    ✅ 5. 50 个深蹲( 早晨 )

    ✅ 6. 蛙式拉伸 10 分钟( 早晨 )

    ✅ 7. 记忆 25 个英文单词

    ✅ 8. 解答 2 个 LeetCode 题目,并将代码及解析上传到 www.algorithm.show

    ✅ 9. 夜跑 3 公里

    ✅ 10. 平板支撑 10 分钟( 晚上 )

    ✅ 11. 腹肌训练 19 分钟( 晚上 )

    ✅ 12. 50 个深蹲( 晚上 )

    ✅ 13. 蛙式拉伸 5 分钟( 晚上 )

    ✅ 14. 学习数据结构与算法

    ✅ 15. 总结课程笔记

    ✅ 16. 无心动挑战

    ✅ 17. 写日记

    ✅ 18. 十点上床睡觉


    ✅: writed the content of plan template to the <hexo-new-post-000> succesffully

    ⚡: created a new hexo post successfully




    (node:1456) ExperimentalWarning: The fs.promises API is experimental
    INFO  Validating config
    INFO  Deleted database.
    INFO  Deleted public folder.
    ✅: the command of <hexo clean> be executed successfully

    (node:8044) ExperimentalWarning: The fs.promises API is experimental
    INFO  Validating config
    INFO  Start processing
    INFO  Files loaded in 280 ms
    INFO  Generated: archives/2020/index.html
    INFO  Generated: archives/2020/09/index.html
    INFO  Generated: archives/index.html
    INFO  Generated: about/index.html
    INFO  Generated: tags/index.html
    INFO  Generated: tags/Hexo-Blog-Testing/index.html
    INFO  Generated: tags/Spe-2020/index.html
    INFO  Generated: tags/Testing-Blog/index.html
    INFO  Generated: archives/2020/page/2/index.html
    INFO  Generated: archives/2020/09/page/2/index.html
    INFO  Generated: CNAME
    INFO  Generated: archives/page/2/index.html
    INFO  Generated: images/icons/favicon-144x144.png
    INFO  Generated: images/icons/favicon-32x32.png
    INFO  Generated: images/icons/favicon-16x16.png
    INFO  Generated: images/icons/apple-touch-icon.png
    INFO  Generated: images/theme/loading.gif
    INFO  Generated: js/modules.js
    INFO  Generated: index.html
    INFO  Generated: 2020/09/20/hexo-new-post-0016/index.html
    INFO  Generated: 2020/09/21/hexo-new-post-1228/index.html
    INFO  Generated: 2020/09/21/hexo-new-post-1015/index.html
    INFO  Generated: 2020/09/21/hexo-new-post-000/index.html
    INFO  Generated: js/utils.js
    INFO  Generated: js/script.js
    INFO  Generated: js/zui.js
    INFO  Generated: images/icons/zhaoo-logo.png
    INFO  Generated: 2020/09/20/hexo-new-post-0045/index.html
    INFO  Generated: css/style.css
    INFO  Generated: 2020/09/20/hexo-new-post-0023/index.html
    INFO  Generated: 2020/09/20/hexo-new-post-0031/index.html
    INFO  Generated: 2020/09/20/hexo-new-post-1909/index.html
    INFO  Generated: 2020/09/18/hello-world/index.html
    INFO  Generated: 2020/09/19/Travis-Testing/index.html
    INFO  Generated: lib/fancybox/fancybox.css
    INFO  Generated: lib/pjax/pjax.js
    INFO  Generated: lib/lazyload/lazyload.js
    INFO  Generated: lib/highlight/a11y-dark.css
    INFO  Generated: lib/justifiedGallery/justifiedGallery.css
    INFO  Generated: 2020/09/18/The-Template-Of-Daily-Plans-For-Spe-2020/index.html
    INFO  Generated: images/theme/pexels-tirachard-kumtanom-544115.jpg
    INFO  Generated: lib/justifiedGallery/justifiedGallery.js
    INFO  Generated: images/theme/pexels-tirachard-kumtanom-574283.jpg
    INFO  Generated: images/2020/Day002/carbon.png
    INFO  Generated: images/2020/Day100/testing-pic.png
    INFO  Generated: images/2020/Day1015/carbon.png
    INFO  Generated: images/2020/Day000/carbon.png
    INFO  Generated: images/2020/Day000/coverPic.png
    INFO  Generated: images/2020/Day001/carbon.png
    INFO  Generated: images/2020/Day003/carbon.png
    INFO  Generated: images/2020/Day1228/Day1228.png
    INFO  Generated: lib/highlight/highlight.js
    INFO  Generated: images/testing.png
    INFO  Generated: images/testing2.png
    INFO  Generated: images/theme/pexels-stas-knop-3760323.jpg
    INFO  Generated: images/theme/cloud.png
    INFO  Generated: images/theme/Nicholas-Stevenson-Folio-animation-people-animals-Illustration-Personal-Friday-Animation-Loop.gif
    INFO  Generated: images/theme/pexels-bich-tran-760710.jpg
    INFO  Generated: images/theme/welcome-image.jpg
    INFO  Generated: images/theme/post-image.jpg
    INFO  Generated: lib/fancybox/fancybox.js
    INFO  Generated: images/theme/Rebecca-Mock-Folio-illustration-animation-gifPop-Up-Magazine-death-book-01.gif
    INFO  Generated: images/theme/Bodil-Jane-Folio-Art-Digital-Illustration-Animation-Reading_Girl.gif
    INFO  Generated: images/template-spe-2020.png
    INFO  Generated: images/theme/brishnas-story-2.gif
    INFO  Generated: lib/jquery/jquery.js
    INFO  Generated: lib/gitalk/gitalk.js
    INFO  68 files generated in 877 ms
    ✅: the command of <hexo generate> be executed successfully

    ⚡: hexo cleaned && generated and runed hexo server successfully




    (node:6780) ExperimentalWarning: The fs.promises API is experimental
    INFO  Validating config
    INFO  Start processing
    INFO  Hexo is running at http://localhost:4000 . Press Ctrl+C to stop.



    ✅: the command of <git add -A> be executed successfully

    ✅: the command of <git commit - m "commitMsg"> be executed successfully

    ✅: the command of <git push origin Hexobackup> be executed successfully

    ⚡: push these new files to github successfully
    ⚡: Nice ! Everything be done successfully, See you again bro.
    ⚡ exited



    commit e973ee18bc9dd4c3c5c25e7ab521a7f38411b9d0 (HEAD -> Hexobackup)
    Author: HuangYuhui <Gentleman_0109@outlook.com>
    Date:   Mon Sep 21 15:48:04 2020 +0800

        testing : this is commit message

    commit 45ac4a0b14077e6948b4ebbde8367465b42ae029 (origin/Hexobackup)
    Author: HuangYuhui <Gentleman_0109@outlook.com>
    Date:   Mon Sep 21 15:24:15 2020 +0800

        update plan.py

    commit 2d9b43da390a7a5174f48109e238c9b256abfdf5
    Author: HuangYuhui <Gentleman_0109@outlook.com>
    Date:   Mon Sep 21 13:00:42 2020 +0800

        update toolPlus.py

    Administrator@191114gm MINGW64 /f/Git/workbench/workbench-github-website/000days/py (Hexobackup)
    $ Enumerating objects: 28, done.
    Counting objects: 100% (28/28), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (15/15), done.
    Writing objects: 100% (16/16), 121.17 KiB | 5.05 MiB/s, done.
    Total 16 (delta 6), reused 0 (delta 0)
    remote: Resolving deltas: 100% (6/6), completed with 6 local objects.
    To https://github.com/YUbuntu0109/000days.git
    45ac4a0..e973ee1  Hexobackup -> Hexobackup
    INFO  Bye!

    终止批处理操作吗(Y/N)?
    Administrator@191114gm MINGW64 /f/Git/workbench/workbench-github-website/000days/py (Hexobackup)
    $
    ```
</details>

* [post info](https://000days.com/2020/09/21/hexo-new-post-000/)
* [commit info](https://github.com/YUbuntu0109/000days/commit/e973ee18bc9dd4c3c5c25e7ab521a7f38411b9d0)
* [travis-ci build info](https://travis-ci.com/github/YUbuntu0109/000days/builds/185559842)
