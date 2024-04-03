#!/usr/bin/python3
"""Deploy archive"""


from fabric.api import *
from datetime import datetime
import os

env.hosts = ['18.207.207.223', '100.26.221.105']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"

def do_deploy(archive_path):
    """deploys archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    dest_folder = "/data/web_static/releases/"
    archive_fname = os.path.basename(archive_path).replace('.tgz', '')
    new_version_folder = "{}{}/".format(dest_folder, archive_fname)
    try:
        for host in env.hosts:
            put(archive_path, '/tmp')
            run("sudo mkdir -p {}".format(new_version_folder))
            run(" sudo tar -xzf /tmp/{} -C {}".format(os.path.basename(archive_path), new_version_folder))
            run("sudo rm -rf /tmp/{}".format(os.path.basename(archive_path)))
            with cd(new_version_folder):
                sudo("rsync -avz ./web_static/ .")
            run("sudo rm -rf {}web_static".format(new_version_folder))
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -s {} /data/web_static/current".format(new_version_folder))
        print("New version deployed!")
        return True
    except Exception as e:
        print("Error deploying archive: {}".format(e))
        return False
