import unittest
from thing import add, mult



class ThingTest(unittest.TestCase):

    def test_add(self):

        result = add(2,3)
        self.assertEquals(result,5)


    def test_mult(self):

        result = mult(2,3)
        self.assertEquals(result,6)
        

    
