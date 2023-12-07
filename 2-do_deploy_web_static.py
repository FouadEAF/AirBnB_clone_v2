#!/usr/bin/python3
""" Function that compress a folder """
from datetime import datetime
from fabric.api import *
import shlex
import os


env.hosts = ['54.162.36.27', '52.3.246.49']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Deploy """
    if not os.path.exists(archive_path):
        return False
    try:
        name = archive_path.replace('/', ' ')
        name = shlex.split(name)
        name = name[-1]

        wname = name.replace('.', ' ')
        wname = shlex.split(wname)
        wname = wname[0]

        releases_path = os.path.join("/data/web_static/releases/", wname)
        tmp_path = os.path.join("/tmp", name)

        put(archive_path, "/tmp/")
        run(f"mkdir -p {releases_path}")
        run(f"tar -xzf {tmp_path} -C {releases_path}")
        run(f"rm {tmp_path}")
        run(f"mv {releases_path}web_static/* {releases_path}")
        run(f"rm -rf {releases_path}web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {releases_path} /data/web_static/current")
        print("New version deployed!")
        return True
    except:
        return False
