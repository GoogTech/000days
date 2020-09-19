## How to generate a picture

### First Step
*https://carbon.now.sh/ 的格式面板链接( 无内容 )*
```
https://carbon.now.sh/?bg=rgba(126%2C211%2C33%2C1)&t=one-light&wt=none&l=application%2Fx-sh&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=4x&wm=false&code=
```

### Second Step
*使用 https://www.bejson.com/enc/urlencode/ 对 template 中的日计划内容进行 encodeURIComponent 编码( 该编码方式会对特殊符号进行编码 ), 然后进行 URL 拼接*
```
https://carbon.now.sh/?bg=rgba(126%2C211%2C33%2C1)&t=one-light&wt=none&l=application%2Fx-sh&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=143%25&si=false&es=4x&wm=false&code=%25F0%259F%258E%2589%2520Day%2520000%2520of%2520plan
```

### Third Step
*使用 python 点击网页中的下载按钮, 将生成的图片下载到本地, 并将其移动到当前项目目录*
