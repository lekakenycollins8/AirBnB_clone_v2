#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref


# association table
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
            Column('place_id', String(60), ForeignKey("places.id"),
                primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey("amenities.id"),
                primary_key=True, nullable=False)
            )


class Place(BaseModel, Base):
    """ A place to stay """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                viewonly=False, back_populates="place_amenities")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """instasntiates objects"""
        super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """returns list of reviews instances"""
            from models import storage
            review_instances = storage.all(Review).values()
            return [review for review in review_instances
                    if review.place_id == self.id]
        @property
        def amenities(self):
            """returns list of amenities"""
            from models import storage
            amen_instances = storage.all(Amenity).values()
            return [amenity for amenity in amen_instances
                    if self.id in amenity.amenity_ids]
        @amenities.setter
        def amenities(self, value):
            """sets amenities"""
            if isinstance(value, list):
                self.amenity_ids = [amenity.id for amenity in value]
