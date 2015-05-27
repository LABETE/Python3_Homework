'''
Created on Jan 13, 2015

@author: jvalverd
'''
import unittest
from ccn_safety import ccn_safety


text = """Have you ever noticed, in television and movies, that phone numbers and credit cards
are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number
that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and 
security experts. 1234-5678-9321, 3333-3333-3333-3333-3333 or 4444-4444-4444-4444-4444-4444.
"""

protected_text = """Have you ever noticed, in television and movies, that phone numbers and credit cards
are obviously fake numbers like 555-123-4567 or XXXX-XXXX-XXXX-5555? It is because a number
that appears to be real, such as XXXX-XXXX-XXXX-5678, triggers the attention of privacy and 
security experts. 1234-5678-9321, 3333-3333-3333-3333-3333 or 4444-4444-4444-4444-4444-4444.
"""

class TestRegex(unittest.TestCase):

    def test_ccn_safety(self):
        result, count = ccn_safety(text)
        self.assertFalse("5555-5555-5555-5555" in result)
        self.assertFalse("1234-5678-1234-5678" in result)
        self.assertTrue("555-123-4567" in result)
        self.assertTrue("1234-5678-9321" in result)
        self.assertTrue("3333-3333-3333-3333-3333" in result)
        self.assertTrue("4444-4444-4444-4444-4444-4444" in result)
        self.assertTrue("XXXX-XXXX-XXXX-5555" in result)
        self.assertTrue("XXXX-XXXX-XXXX-5678" in result)
        self.assertEqual(count, 2)
        self.assertEqual(result, protected_text)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ccn_safety']
    unittest.main()