'''This file contains tests for section 3'''

import unittest
from sections.section3.main import avg

class EasyTestCase(unittest.TestCase):
    '''
    This is a class for easy tests
    '''
    def test_easy_input(self):
        '''First easy test'''
        self.assertEqual(avg([1,2,3]),2)

    def test_easy_input_two(self):
        '''Second easy test'''
        self.assertEqual(avg([1,2,3,4,5]),3)

class MediumTestCase(unittest.TestCase):
    '''
    This is a class for medium tests
    '''
    def test_medium_input(self):
        '''Second first test'''
        with self.assertRaises(TypeError):
            self.assertEqual(avg([1,2,3,"Ramon"]),2)

    def test_medium_input_two(self):
        '''Second medium test'''
        self.assertEqual(avg([1,2,3,4,"5"]),2)

class HardTestCase(unittest.TestCase):
    '''
    This is a class for medium tests
    '''
    def test_hard_input(self):
        '''Second first test'''
        with self.assertRaises(TypeError):
            self.assertEqual(avg([1,2,3,None]),2)

    def test_hard_input_two(self):
        '''Second medium test'''
        self.assertEqual(avg([1,2,3,4,str(5)]),2)

    def test_hard_input_three(self):
        '''Second medium test'''
        with self.assertRaises(TypeError):
            self.assertEqual(avg([1,2,3,4, float]),2)

    def test_hard_input_four(self):
        '''Second medium test'''
        with self.assertRaises(TypeError):
            self.assertEqual(avg([1,2,3,4,frozenset]),2)

if __name__== '__main__':
    unittest.main()
