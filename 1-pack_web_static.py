#!/usr/bin/python3
"""creates a .tgz archive from contents of web_static"""


from fabric.api import local
from datetime import datetime

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
