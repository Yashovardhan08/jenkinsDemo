import unittest

from program import *

class TestingSum(unittest.TestCase):

    # add
    def add_test(self):
        self.assertEqual(add(10000000000,1),10000000001)

    #sub
    def sub_test(self):
        self.assertEqual(sub(10000000000,1),9999999999)

    #multiply
    def mul_test(self):
        self.assertEqual(multiply(111,9),999)

if __name__ =='__main__':
    unittest.main()
