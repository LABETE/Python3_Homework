"""
property_address.py: Create a home data with specifications
"""
import re, logging
LOG_FILENAME = "property_address.log"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
DEFAULT_LOG_LEVEL = "warning"
LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL
          }

def start_logging(filename=LOG_FILENAME, level=DEFAULT_LOG_LEVEL):
    "Start logging with given filename and level."
    logging.basicConfig(filename=filename, level=LEVELS[level], format=LOG_FORMAT)

class StateError(Exception):
    def __init__(self, expr):
        self.expr = expr
        self.msg = "STATE exception"
        logging.error(self.msg)

class ZipCodeError(Exception):
    def __init__(self, expr):
        self.expr = expr
        self.msg = "ZIPCODE exception"
        logging.error(self.msg)

class Address(StateError, ZipCodeError):
    def __init__(self, name, street_address, city, state, zip_code):
        """
        person name, street address, city, state: MN, zip code: 12345
        """
        logging.info("Creating a new address")
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
        logging.info("Getting the name")
        return self._name
    
    @name.setter
    def name(self, value):
        msg = "Name exception"
        logging.error(msg)
        raise AttributeError(msg)
    
    @property
    def street_address(self):
        logging.info("Getting the street address")
        return self._street_address
    
    @street_address.setter
    def street_address(self, value):
        logging.info("Setting a new street address")
        self._street_addres = value
    
    @property
    def city(self):
        logging.info("Getting the city")
        return self._city
    
    @city.setter
    def city(self, value):
        logging.info("Setting a new city")
        self._city = value
        
    @property
    def state(self):
        logging.info("Getting the state")
        return self._state
    
    @state.setter
    def state(self, value):
        regex = re.compile("(^[A-Z][A-Z]$)")
        if regex.match(value):
            logging.info("Setting a new state")
            self._state = value
        else:
            raise StateError(value)
    
    @property
    def zip_code(self):
        logging.info("Getting the zip code")
        return self._zip_code
    
    @zip_code.setter
    def zip_code(self, value): 
        regex = re.compile("(^\d\d\d\d\d$)")
        if regex.match(value):
            logging.info("Setting a new zip code")
            self._zip_code = value
        else:
            raise ZipCodeError(value)
