'''
Created on Dec 11, 2014

@author: jvalverd
'''
import unittest
import coconuts


class Test(unittest.TestCase):

    def setUp(self):
        self.american_coconut = coconuts.American()
        self.south_asian_coconut = coconuts.South_Asian()
        self.middle_eastern_coconut = coconuts.Middle_Eastern()
        self.south_asian_coconut.add(2)
        self.middle_eastern_coconut.add(1)

    def test_coconuts_string_error(self):
        self.assertRaises(AttributeError, self.american_coconut.add, "two")
    
    def test_coconuts_successes(self):
        self.assertNotEqual(self.american_coconut.weight, self.middle_eastern_coconut.weight,)
        self.assertNotEqual(self.american_coconut.weight, self.south_asian_coconut.weight,)
        self.assertNotEqual(self.middle_eastern_coconut.weight, self.south_asian_coconut.weight,)
        self.assertIsNone(self.american_coconut.add(3), "Adding a non string coconut")
        expected = 19
        actual = (self.american_coconut.total_weight() + 
                  self.middle_eastern_coconut.total_weight() +
                  self.south_asian_coconut.total_weight())
        self.assertEqual(actual, expected, "The weight is not the expected. Actual weight: {0}, Expected weight: {1}".format(actual, expected))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_coconuts_errors']
    unittest.main()