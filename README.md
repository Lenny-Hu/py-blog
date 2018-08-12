# 设置pip国内的源

* 阿里云 http://mirrors.aliyun.com/pypi/simple/

* 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

* 豆瓣(douban) http://pypi.douban.com/simple/

* 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
  
* 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

> 临时使用在后面加上-i参数，指定pip源：pip install scrapy -i https://pypi.tuna.tsinghua.edu.cn/simple

## 永久修改

* Linux\mac，创建或修改~/.pip/pip.conf，windows则创建或修改c:\users\hl\pip\pip.ini，添加以下内容

```
[global]
index-url = https://pypi.doubanio.com/simple/
timeout = 1000
[install]
use-mirrors = true
mirrors = https://pypi.doubanio.com/
```

# 使用virtualenv搭建python隔离环境
```
pip3 install virtualenv # 安装

# 进入项目根目录，创建独立运行环境
virtualenv --no-site-packages venv

# 进入该独立运行环境（注意到命令提示符变了，有个(venv)前缀，表示当前环境是一个名为venv的Python环境）
source venv/bin/activate

# 进入后即可正常安装软件包，例如：
pip install jinja2

# 退出当前的venv环境，使用deactivate命令
deactivate
```

# django

pip安装好django后，用django-admin查看一些命令，以下为一些Django常用的
```
django-admin startproject APPNAME #创建项目

python3 manage.py runserver # 启动测试环境的服务器

python3 manage.py migrate # 数据库迁移

python3 manage.py createsuperuser # 创建超级管理员来登录后台，管理地址：/admin
```

# 软件依赖安装

python没有统一的包管理形式，通常使用requiremenets.txt作为配置文件管理依赖，例如
```
# 原来安装django
pip install Django==2.1

# 现在只需要将Django==2.1加入requiremenets.txt文件中，执行下面的命令安装依赖
pip install -r requiremenets.txt # 当有多个环境时，会创建一个requiremenets文件夹，其内放多个配置文件，如dev.txt，prod.txt
```

# 构建流

## 使用fabric搭建构建系统(像是配置nodejs中package.json中的start/dev等命令)
```
pip install fabric3 # 安装

# 在项目根目录下创建fabfile.py（文件内容见项目），然后执行fab hello，该命令会从fabfile文件中找对应的函数来执行。

# 像上述安装依赖的命令，可写在fabfile.py添加一个install函数中，利用fabric执行命令进行安装，类似nodejs中定义在package.json中的start/dev等命令，

# 如果使用了requiremenets文件夹，则可在install函数中添加一个参数，实现不同的环境安装不同的依赖。
fab install || fabinstall:prod # 前者使用dev.txt，后者使用prod.txt

# 添加运行测试服务器的命令
fab runserver

# 以此类推，添加其他的命令来简化开发，可用list参数列出已有的任务
fab --list

# 如果不希望有的方法被罗列出来，在那些希望暴露的函数添加@task装饰器即可
```


