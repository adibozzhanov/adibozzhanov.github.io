import unittest
from thing import add, mult, div



class ThingTest(unittest.TestCase):

    def test_add(self):

        result = add(2,3)
        self.assertEquals(result,5)


    def test_mult(self):

        result = mult(2,3)
        self.assertEqual(result,6)


    def test_div(self):

        result = div(6,2)
        self.assertEqual(3,result)
        

    
