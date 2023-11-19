#!/usr/bin/python3
"""
Importing the necessary libraries
"""
from sqlalchemy import MetaData, Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship

"""
This module contains a script that contains
the class definition of a State
Author: Nafeesah
"""


class City(Base):
    """
    A class of cities
    Attrubutes:
        id(int): represent cities id
        name(str): represents name of cities
        state_id(int): represents the state id
    Methods:
        None
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
