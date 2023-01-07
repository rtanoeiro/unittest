'''This file contains tests for section 5'''

import unittest
from sections.section5.main import Counter

class EasyTestCase(unittest.TestCase):
    '''
    This is a class for easy tests
    '''
    def setUp(self) -> object: #(?) TODO: CHECK IF IT RETURNS AN OBJECT
        '''Setting up the Class to be used on tests'''
        self.counter = Counter()

    def test_easy_input(self):
        '''First easy test'''
        self.assertEqual(self.counter.get_value(), 0)

    def test_easy_input_two(self):
        '''Second easy test'''
        self.counter.clear()
        self.assertEqual(self.counter.get_value(), 0)

    def tearDown(self) -> None:
        '''Clearing up the object used on tests'''
        self.counter = None

class MediunTestCase(unittest.TestCase):
    '''
    This is a class for Medium tests
    '''
    def setUp(self) -> object: #(?) TODO: CHECK IF IT RETURNS AN OBJECT
        '''Setting up the Class to be used on tests'''
        self.counter = Counter()

    def test_medium_input(self):
        '''First medium test'''
        self.counter.add()
        self.counter.add()
        self.counter.add()
        self.counter.add()
        self.assertEqual(self.counter.get_value(), 4)

    def test_medium_input_two(self):
        '''Second medium test'''
        self.counter.remove()
        self.counter.remove()
        self.counter.remove()
        self.counter.remove()
        self.assertEqual(self.counter.get_value(), 0)

    def test_medium_input_three(self):
        '''Third medium test'''
        self.counter.add()
        self.counter.add()
        self.counter.add()
        self.counter.add()
        self.counter.remove()
        self.counter.remove()
        self.counter.remove()
        self.counter.remove()
        self.assertEqual(self.counter.get_value(), 0)

    def tearDown(self) -> None:
        '''Clearing up the object used on tests'''
        self.counter = None

class HardTestCase(unittest.TestCase):
    '''
    This is a class for easy tests
    '''
    def setUp(self) -> object: #(?) TODO: CHECK IF IT RETURNS AN OBJECT
        '''Setting up the Class to be used on tests'''
        self.counter = Counter()

    def test_hard_input(self):
        '''First hard test'''
        for _ in range(0,1000):
            self.counter.add()
        self.assertEqual(self.counter.get_value(),1000)

    def tearDown(self) -> None:
        '''Clearing up the object used on tests'''
        self.counter = None
