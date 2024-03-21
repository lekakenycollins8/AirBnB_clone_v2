#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models


class Amenity(BaseModel, Base):
    """ Holds amenities of Airbnb"""
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        from models.place import place_amenity
        place_amenities = relationship("Place", secondary=place_amenity,
                back_populates="amenities")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """instantiates objects"""
        super().__init__(*args, **kwargs)
