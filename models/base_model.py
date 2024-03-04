#!/usr/bin/python3
"""
Write a class BaseModel that defines all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ The BaseModel class defines all common 
        attributes/methods for other classes 
    """
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        """override the __str__ method so it returns [<class name>] (<self.id>) <self.__dict__>"""
        return f"[<self.__class__.__name__>] (<self.id>) <self.__dict__>"

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """returns a dictionary containing all key/value pairs of __dict__ of the instance"""
        attrs = {k: getattr(self, k) for k in self.__dict__ }
        return attrs