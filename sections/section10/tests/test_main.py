import unittest
import time
from sections.section10.main import EfficiencyAdding


class TestEfficiency(unittest.TestCase):
    def setUp(self):
        self.EfficiencyAdding = EfficiencyAdding()
        self.efficiency_data = dict()

    def test_function_one(self):
        start_time = time.time()
        self.EfficiencyAdding.adding_two_first_method(50)
        end_time = time.time()
        self.efficiency_data["first_method"] = end_time - start_time

    def test_function_two(self):
        start_time = time.time()
        self.EfficiencyAdding.adding_two_second_method(50)
        end_time = time.time()
        self.efficiency_data["second_method"] = end_time - start_time

    def tearDown(self):
        self.EfficiencyAdding = None
        print(self.efficiency_data)
        self.efficiency_data.clear()


if __name__ == "__main__":
    unittest.main()
