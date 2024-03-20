#!/usr/bin/python3

import os

def test_environment_variables():
    env_vars = [
        "HBNB_ENV",
        "HBNB_MYSQL_USER",
        "HBNB_MYSQL_PWD",
        "HBNB_MYSQL_HOST",
        "HBNB_MYSQL_DB",
        "HBNB_TYPE_STORAGE"
    ]

    for var_name in env_vars:
        var_value = os.getenv(var_name)
        if var_value is None:
            print(f"Environment variable {var_name} is not set.")
        else:
            print(f"Environment variable {var_name} has value: {var_value}")

if __name__ == "__main__":
    test_environment_variables()

