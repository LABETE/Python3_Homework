"""
property_address.py: Create a home data with specifications
"""
import re, logging, configparser
from optparse import OptionParser

config = configparser.RawConfigParser()
config.read("V:/workspace/Python3_Homework12/src/property_address.cfg")

LOG_FILENAME = config.get('log', 'output')
LOG_FORMAT = config.get('log', 'format')
DEFAULT_LOG_LEVEL = "info"
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
        self.regex_state = re.compile(config.get("validators", "state"))
        if self.regex_state.match(state):
            self._state = state
        else:
            raise StateError(state)
        self.regex_zip_code = re.compile(config.get("validators", "zip_code"))
        if self.regex_zip_code.match(zip_code):
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
        if self.regex_state.match(value):
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
        if self.regex_zip_code.match(value):
            logging.info("Setting a new zip code")
            self._zip_code = value
        else:
            raise ZipCodeError(value)

def main(options):
    "routes requests"
    if options.level:
        start_logging(level=options.level.lower())
    else:
        start_logging()
    if options.name and options.address and options.city and options.state and options.zip_code: 
        Address(name=options.name, street_address=options.address, city=options.city, state=options.state, zip_code=options.zip_code)
        
if __name__ == "__main__":
    
    parser = OptionParser()
    parser.add_option('-l', '--level', dest='level', action='store', help='sets the log level to DEBUG, INFO, WARNING, ERROR and CRITICAL')
    parser.add_option('-n', '--name', dest='name', action='store', help='requires -a, -c, -s, -z options. Sets the name value of the Addres object')
    parser.add_option('-a', '--address', dest='address', action='store', help='requires -n, -c, -s, -z options. Sets the street_addres value of the addres object')
    parser.add_option('-c', '--city', dest='city', action='store', help='requires -n, -a, -s, -z options. Sets the city value of the address object')
    parser.add_option('-s', '--state', dest='state', action='store', help='requires -n, -a, -c, -z options. Sets the state value of the Address object')
    parser.add_option('-z', '--zip_code', dest='zip_code', action='store', help='requires -n, -a, -c, -s options. Sets the zip_code value of the Address object')
    (options, args) = parser.parse_args()
    
    if (not options.name or not options.address or not options.city or 
        not options.state or not options.zip_code):
        parser.error('options -n, -a, -c, -s, -z are required')
    try:
        main(options)
    except StateError:
        parser.error('option -s requires two capital letters')
    except ZipCodeError:
        parser.error('option -z requires 5-digit US zip code')
