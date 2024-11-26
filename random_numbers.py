"""things to be sorted"""

# System Imports
import random

# First Party Imports

# Third Party Imports


class RandomNumbers:
    """random number class"""

    def __init__(self, list_length: int):
        """constructor"""
        self.collection: list[int] = self.__create_random_number_list(list_length)

    def __create_random_number_list(self, list_length: int) -> list[int]:
        """method to create list of random numbers"""
        i: int = 0
        random_number_list: list[int] = []
        while i < list_length:
            random_number_list.append(random.randint(0, 100))
            i += 1
        return random_number_list
