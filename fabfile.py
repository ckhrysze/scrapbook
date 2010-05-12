from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['anaelise.net']

def deploy():
    pack()
    put('tmp/scrapbook.tgz', '~/webapps/anaelise_app1')
    with cd('~/webapps/anaelise_app1/scrapbook'):
        run('ls ~/webapps/anaelise_app1')


def pack():
    local('tar czf tmp/scrapbook.tgz scrapbook', capture=False)
