import unittest
from sections.section5.challenge import Car


class EasyTestCase(unittest.TestCase):

    def setUp(self):
        # Todo: create an object named car from the Car class
        # Todo: use the object car to start the car.
        self.car = Car()

    def test_easy_input(self):
        # Todo: use the object car to add speed 4 times.
        # Todo: make sure that the current speed is 20.
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.car.add_speed()
        self.assertEqual(self.car.current_speed(), 20)

    def test_easy_input_two(self):
        # Todo: use the object car to add speed 2 times.
        # Todo: use the object car to stop the car.
        # Todo: make sure that the current speed is 0 not -10.
        pass

    def tearDown(self):
        # Todo: stop the car.
        # Todo: turn off the car.
        # Todo: set the object car to None.
        pass


class MediumTestCase(unittest.TestCase):

    def setUp(self):
        # Todo: create an object named car from the Car class
        # Todo: use the object car to start the car.
        pass

    def test_medium_input(self):
        # Todo: raise an exception if the user tried to start the car while it's already on.
        pass

    def test_medium_input_two(self):
        # Todo: use the object car to remove speed 4 times.
        # Todo: raise an exception if the user tried to turn off the car in a speed greater than 0.
        pass

    def tearDown(self):
        # Todo: stop the car.
        # Todo: turn off the car.
        # Todo: set the object car to None.
        pass


class HardTestCase(unittest.TestCase):

    def setUp(self):
        # Todo: create an object named car from the Car class
        # Todo: use the object car to start the car.
        pass

    def test_hard_input(self):
        # Todo: use the object car to add speed 2 times.
        # Todo: use the object car to remove speed 4 times.
        # Todo: make sure that the current speed is 0. 
        pass

    def test_hard_input_two(self):
        # Todo: use the object car to add speed 2 times.
        # Todo: stop the car.
        # Todo: stop the car.
        # Todo: stop the car.
        # Todo: make sure that the current speed is 0.
        pass

    def tearDown(self):
        # Todo: stop the car.
        # Todo: turn off the car.
        # Todo: set the object car to None.
        pass


if __name__ == '__main__':
    unittest.main()