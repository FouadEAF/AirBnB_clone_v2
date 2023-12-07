#!/usr/bin/python3
""" Function that compress a folder """
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        time_zero = datetime.now()
        fixedDate = "%Y%m%d%H%M%S"
        archive_path = f'versions/web_static_{time_zero.strftime(fixedDate)}.tgz'
        local(f'tar -cvzf {archive_path} web_static')
        return archive_path
    except:
        return None
