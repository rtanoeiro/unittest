'''This file contains tests for section 3'''

import unittest
from section3.main import avg

class EasyTestCase(unittest.TestCase):
    '''
    This is a class for easy tests
    '''
    def test_easy_input(self):
        '''First easy test'''
        self.assertEqual(avg([1,2,3]),2.0)

    def test_easy_input_two(self):
        '''Second easy test'''


if __name__== '__main__':
    unittest.main()
