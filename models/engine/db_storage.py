#!/usr/bin/python3
"""Database Storage Engine"""

import os
from models.base_model import Base
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


classes = {"Amenity": Amenity, "City": City, "Place": Place,
        "Review": Review, "State": State, "User": User}

class DBStorage:
    """database storage
    Attributes: private class attributes: __engine, __session
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    os.environ.get('HBNB_MYSQL_USER'),
                    os.environ.get('HBNB_MYSQL_PWD'),
                    os.environ.get('HBNB_MYSQL_HOST'),
                    os.environ.get('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on current database session depending on class name"""
        objects = {}
        if cls is not None and cls in classes.values():
            query_result = self.__session.query(cls).all()
            for obj in query_result:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """ adds object to current database session"""
        self.__session.add(obj)

    def save(self):
        """ commit changes of current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates database tables and current database session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
