'''
Created on Jan 12, 2015

@author: jvalverd
'''
import unittest
import find_regex

class Test(unittest.TestCase):
    
    def setUp(self):
        self.text = """In the 1950s, mathematician Stephen Cole Kleene described automata theory 
                  and formal language theory in a set of models using a notation called 
                  "regular sets" as a method to do pattern matching. Active usage of this 
                  system, called Regular Expressions, started in the 1960s and continued 
                  under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, 
                  Ken Thompson, and Henry Spencer."""
    
    def testFind_regex(self):
        self.start, self.end = find_regex.find(self.text)
        expected_start = 0
        expected_end = 491
        self.assertEquals(self.start, expected_start)
        self.assertEquals(self.end, expected_end)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFind_regex']
    unittest.main()