#!/usr/bin/python3
"""Script to clean up old archives"""

from fabric.api import local, run, env
from datetime import datetime
from os.path import exists

env.hosts = ['18.207.207.223', '100.26.221.105']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_clean(number=0):
    """Deletes out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1

    try:
        local_archives = local("ls -t versions", capture=True).split('\n')
        for arch in local_archives[number:]:
            local("rm versions/{}".format(arch))

        remote_archives = run("ls -t /data/web_static/releases").split('\n')
        for arch in remote_archives[number:]:
            run("rm -rf /data/web_static/releases/{}".format(arch))
        return True
    except Exception:
        return False
