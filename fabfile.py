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
    local("pip3 install -r requirements/%s.txt" % requirements_env);

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

@task
# 创建标签并发布到GitHub上
def tag_version(version):
    """创建标签并发布到GitHub上"""
    local("git tag %s" % version);
    local("git push origin %s"%version);

@task
# 下载GitHub上指定版本的代码
def fetch_version(version):
    """从github上下载指定tag的代码"""
    local("wget https://github.com/Lenny-Hu/py-blog/archive/%s.tar.gz"%version);

@task
def test():
    """运行测试"""
    local('python3 manage.py test');