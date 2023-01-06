'''This file contains tests for section 4'''

import unittest
from section4.main import counter

class EasyTestCase(unittest.TestCase):
    '''
    This is a class for easy tests
    '''
    def test_easy_input(self):
        '''First easy test'''
        self.assertEqual(counter("Ramon"),5)

    def test_easy_input_two(self):
        '''Second easy test'''
        self.assertEqual(counter("Ramonster"),9)

class MediumTestCase(unittest.TestCase):
    '''
    This is a class for medium tests
    '''
    def test_medium_input(self):
        '''Second first test'''
        with self.assertRaises(UnicodeError):
            self.assertEqual(counter("Ramon@"),6)

    def test_medium_input_two(self):
        '''Second medium test'''
        self.assertEqual(counter("Ramon   "),5)

class HardTestCase(unittest.TestCase):
    '''
    This is a class for medium tests
    '''
    def test_hard_input(self):
        '''Second first test'''
        with self.assertRaises(Exception):
            self.assertEqual(counter(""),0)

    def test_hard_input_two(self):
        '''Second medium test'''
        with self.assertRaises(Exception):
            self.assertEqual(counter(None),0)

if __name__== '__main__':
    unittest.main()
