from fabric.decorators import task
from fabric.operations import local


@task
def install():
    local('python setup.py install')