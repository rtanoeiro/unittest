from collections import Counter


class ListChanger:
    def __init__(self, input_list: list):
        self._list = input_list

    def reverse_list(self):
        return list(reversed(self._list))

    def has_duplicates(self):
        set_list = set(self._list)
        return len(self._list) != len(set_list)

    def smallest_number(self):
        return min(self._list)

    def greatest_number(self):
        return max(self._list)

    def second_greatest_number(self):
        ordered_list = list(set(sorted(self._list, reverse=False)))
        return ordered_list[-2]

    def remove_first_and_last(self):
        self._list.pop(0)
        self._list.pop(-1)
        return self._list