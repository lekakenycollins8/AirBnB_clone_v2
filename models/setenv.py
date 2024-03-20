#!/usr/bin/python3

import os

def set_environment_variables():
    os.environ["HBNB_ENV"] = "dev"
    os.environ["HBNB_MYSQL_USER"] = "hbnb_dev"
    os.environ["HBNB_MYSQL_PWD"] = "hbnb_dev_pwd"
    os.environ["HBNB_MYSQL_HOST"] = "localhost"
    os.environ["HBNB_MYSQL_DB"] = "hbnb_dev_db"
    os.environ["HBNB_TYPE_STORAGE"] = "db"

if __name__ == "__main__":
    set_environment_variables()
