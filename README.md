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