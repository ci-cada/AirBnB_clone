#!/usr/bin/env python3
"""model - user"""

from models.base_model import BaseModel


class User(BaseModel):
    """this class contains the users attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
