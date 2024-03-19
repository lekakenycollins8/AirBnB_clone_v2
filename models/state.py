#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                cascade="all, delete-orphan")
    else:
        name = ""

    if os.environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """returns list of City instances"""
            from models import storage
            city_instances = stroage.all(City)
            return [city for city in city_instances.values() if city.state_id 
                    == self.id]
