#!/usr/bin/python3
"""
Class Place that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Reviews made"""
    place_id = ""
    user_id = ""
    text = ""
