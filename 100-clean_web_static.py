#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *


env.hosts = ['54.162.36.27', '52.3.246.49']
env.user = "ubuntu"


def do_clean(number=0):
    """ CLEANS """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local(f'cd versions ; ls -t | tail -n +{number} | xargs rm -rf')

    path = '/data/web_static/releases'
    run(f'cd {path} ; ls -t | tail -n +{number} | xargs rm -rf')
