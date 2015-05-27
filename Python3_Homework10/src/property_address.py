"""
property_address.py: Create a home data with specifications
"""
import re

class StateError(Exception):
    def __init__(self, expr):
        self.expr = expr
        self.msg = "The state should have only 2 capital letters, example: MN, LA"


class ZipCodeError(Exception):
    def __init__(self, expr):
        self.expr = expr
        self.msg = "The zip code must be in the format nnnnn"

class Address(StateError, ZipCodeError):
    def __init__(self, name, street_address, city, state, zip_code):
        """
        person name, street address, city, state: MN, zip code: 12345
        """
        self._name = name
        self._street_address = street_address
        self._city = city
        regex = re.compile("(^[A-Z][A-Z]$)")
        if regex.match(state):
            self._state = state
        else:
            raise StateError(state)
        regex = re.compile("(^\d\d\d\d\d$)")
        if regex.match(zip_code):
            self._zip_code = zip_code
        else:
            raise ZipCodeError(zip_code)
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        raise AttributeError("The name is read only, it can not be modified")
    
    @property
    def street_address(self):
        return self._street_address
    
    @street_address.setter
    def street_address(self, value):
        self._street_addres = value
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        self._city = value
        
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        regex = re.compile("(^[A-Z][A-Z]$)")
        if regex.match(value):
            self._state = value
        else:
            raise StateError(value)
    
    @property
    def zip_code(self):
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value): 
        regex = re.compile("(^\d\d\d\d\d$)")
        if regex.match(value):
            self._zip_code = value
        else:
            raise ZipCodeError(value)