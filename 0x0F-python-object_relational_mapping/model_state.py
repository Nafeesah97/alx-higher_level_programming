#!/usr/bin/python3
"""
Importing the necessary libraries
"""
from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""
This module contains a script that contains 
the class definition of a State
Author: Nafeesah
"""


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """
    A class of state
    
    Attrubutes:
        id(int): represent state id
        name(str): represents nameof state

    Methods:
        None
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)