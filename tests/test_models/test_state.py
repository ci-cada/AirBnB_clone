#!/usr/bin/env python3
"""model - test state"""

from models.state import State
from tests.test_models.test_base_model import TestBaseModel

class TestState(TestBaseModel):
    """testing the state model"""

    
    def __init__(self, *args, **kwargs):
        """init function"""

        super().__init__(*args,**kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """testing if state name is a str"""
        state = self.value()
        self.assertEqual(type(state.name), str)