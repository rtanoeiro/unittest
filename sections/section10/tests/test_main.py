import unittest
import time
from sections.section10.main import EfficiencyAdding


class TestEfficiency(unittest.TestCase):
    def setUp(self) -> None:
        self.efficiency_adding = EfficiencyAdding()
        self.efficiency_data = dict()

    def function_one(self):
        start_time = time.time()
        self.efficiency_adding.adding_two_first_method(50)
        end_time = time.time()
        self.efficiency_data["first_method"] = end_time - start_time

    def function_two(self):
        start_time = time.time()
        self.efficiency_adding.adding_two_second_method(50)
        end_time = time.time()
        self.efficiency_data["second_method"] = end_time - start_time

    def tearDown(self) -> None:
        print(self.efficiency_data)
        self.efficiency_adding = None
        self.efficiency_data.clear()
