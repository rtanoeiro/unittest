from unittest import TestCase
from sections.section13.challenge import ListChanger


class TestListChanger(TestCase):

	def setUp(self):
		self._list_changer_obj_1 = ListChanger([1, 2, 3, 4, 5, 6, 6])
		self._list_changer_obj_2 = ListChanger(["CA", "FL", "MC", "NY"])
		self._list_changer_obj_3 = ListChanger([True, False, True, False])
		
	def test_reverse_list(self):
		self.assertEqual(self._list_changer_obj_1.reverse_list(), [6, 6, 5, 4, 3, 2, 1])
		self.assertEqual(self._list_changer_obj_2.reverse_list(), [ "NY", "MC", "FL", "CA"])
		self.assertEqual(self._list_changer_obj_3.reverse_list(), [False, True, False, True])

	def test_has_duplicates(self):
		self.assertEqual(self._list_changer_obj_1.has_duplicates(), True)
		self.assertEqual(self._list_changer_obj_2.has_duplicates(), False)
		self.assertEqual(self._list_changer_obj_3.has_duplicates(), True)

	def test_smallest_number(self):
		self.assertEqual(self._list_changer_obj_1.smallest_number(), 1)

	def test_greatest_number(self):
		self.assertEqual(self._list_changer_obj_1.greatest_number(), 6)
	
	def test_second_greatest_number(self):
		self.assertEqual(self._list_changer_obj_1.second_greatest_number(), 5)
	
	def test_remove_first_and_last(self):
		self.assertEqual(self._list_changer_obj_1.remove_first_and_last(), [2, 3, 4, 5, 6])

	def tearDown(self):
		self._list_changer_obj_1 = None
		self._list_changer_obj_2 = None
		self._list_changer_obj_3 = None