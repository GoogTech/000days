## How to generate a picture

### First Step
*https://carbon.now.sh/ 的格式面板链接( 无内容 )*
```
https://carbon.now.sh/?bg=rgba(126%2C211%2C33%2C1)&t=one-light&wt=none&l=text&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=4x&wm=false&code=
```

### Second Step
*使用 https://www.bejson.com/enc/urlencode/ 对 template 中的日计划内容进行 encodeURIComponent 编码( 该编码方式会对特殊符号进行编码 ), 然后进行 URL 拼接*
```
https://carbon.now.sh/?bg=rgba(126%2C211%2C33%2C1)&t=one-light&wt=none&l=text&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=4x&wm=false&code=%25F0%259F%2593%259D%2520The%2520template%2520of%2520daily%2520plans%2520in%2520September%2520of%25202020%2520be%2520showed%2520as%2520follows%252C%2520Stay%2520up%2520and%2520Keep%2520up%2520!%250A%250A%25F0%259F%258E%2589%2520Day%2520000%2520of%2520%2523100DaysOfCode%252C%2520%2523100DaysOfEnglish%2520and%2520%2523100DaysOfFitness%250A%250A%250A%25E2%259C%2585%25201.%2520Get%2520up%2520at%25205%2520at%2520morning%250A%250A%25E2%259C%2585%25202.%2520Morning%2520run%2520with%2520five%2520kilometers%250A%250A%25E2%259C%2585%25203.%2520Plank%2520with%2520fifteen%2520minutes%2520at%2520morning%250A%250A%25E2%259C%2585%25204.%2520Stomach%2520workout%2520with%2520nineteen%2520minutes%2520at%2520morning%250A%250A%25E2%259C%2585%25205.%2520fifty%2520Squats%2520at%2520morning%250A%250A%25E2%259C%2585%25206.%2520Stretch%2520with%2520ten%2520minutes%2520at%2520morning%250A%250A%25E2%259C%2585%25207.%2520Memorizing%2520twenty-five%2520words%2520of%2520english%250A%250A%25E2%259C%2585%25208.%2520Solve%2520two%2520problems%2520of%2520LeetCode%2520and%2520push%2520the%2520note%2520to%2520github%250A%250A%25E2%259C%2585%25209.%2520Night%2520running%2520with%2520three%2520kilometers%250A%250A%25E2%259C%2585%252010.%2520Plank%2520with%2520ten%2520minutes%2520at%2520night%250A%250A%25E2%259C%2585%252011.%2520Stomach%2520workout%2520with%2520nineteen%2520minutes%2520at%2520night%250A%250A%25E2%259C%2585%252012.%2520fifty%2520Squats%2520at%2520night%250A%250A%25E2%259C%2585%252013.%2520Stretch%2520with%2520five%2520minutes%2520at%2520night%250A%250A%25E2%259C%2585%252014.%2520Learn%2520data%2520structure%2520and%2520algorithms%250A%250A%25E2%259C%2585%252015.%2520Summarize%2520the%2520learning%2520note%2520of%2520daily%2520courses%250A%250A%25E2%259C%2585%252016.%2520No%2520eroticism%250A%250A%25E2%259C%2585%252017.%2520Keep%2520a%2520diary%250A%250A%25E2%259C%2585%252018.%2520Go%2520to%2520bed%2520at%252010%2520at%2520night%250A
```

### Third Step
*使用 python 点击网页中的下载按钮, 将生成的图片下载到本地, 并将其移动到当前项目目录*
