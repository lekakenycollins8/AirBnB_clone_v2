#!/usr/bin/python3
"""Automated deployment script"""


from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['18.207.207.223', '100.26.221.105']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"

def do_pack():
    """creates .tgz archive from folder"""
    #generate archive name
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(time))

        return "versions/web_static_{}.tgz".format(time)
    except Exception as e:
        return None

def do_deploy(archive_path):
    """Deploys archive to web servers"""
    if not exists(archive_path):
        return False

    dest_folder = "/data/web_static/releases/"
    archive_fname = archive_path.split('/')[-1].split('.')[0]

    try:
        put(archive_path, '/tmp')
        run("sudo mkdir -p {}/{}".format(dest_folder, archive_fname))
        run("sudo tar -xzf /tmp/{}.tgz -C {}/{}"
            .format(archive_fname, dest_folder, archive_fname))
        run("sudo rm /tmp/{}.tgz".format(archive_fname))
        run("sudo mv {}/{}/web_static/* {}/{}"
            .format(dest_folder, archive_fname, dest_folder, archive_fname))
        run("sudo rm -rf {}/{}/web_static".format(dest_folder, archive_fname))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}/{} /data/web_static/current"
            .format(dest_folder, archive_fname))
        return True
    except Exception:
        return False

def deploy():
    """Automates deployment process"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
