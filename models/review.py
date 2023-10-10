#!/usr/bin/env python3
"""model - review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class containing attributes for the review model"""
    place_id = ''
    user_id = ''
    text = ''
