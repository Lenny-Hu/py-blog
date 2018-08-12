from fabric.api import local
from fabric.decorators import task

def test():
    print('我不会对外暴露');

@task
def hello():
    """😁"""
    print('hello world');

# 安装依赖
@task
def install(requirements_env='dev'):
    """安装所有依赖"""
    local('pip3 install -r requirements/%s.txt' % requirements_env);

@task
# 运行服务器
def runserver():
    """运行服务器"""
    local('./manage.py runserver');

@task
# 检查代码
def pep8():
    """使用pep8检查代码"""
    local('pep8 .');