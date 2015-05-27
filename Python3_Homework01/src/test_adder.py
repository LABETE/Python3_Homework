'''
Created on Dec 6, 2014

@author: jvalverd
'''
import unittest
from adder import adder_errors

class Test(unittest.TestCase):


    def test_adder_errors(self):
        "Test ensuring errors in data cause validation failures."
        self.assertRaises(TypeError, adder_errors, "a", 3)
    
    def test_adder_successes(self):
        "Test ensuring that valid data passes."
        self.assertIsNone(adder_errors(3, 4), "Not accepting int values")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_adder_errors']
    unittest.main()