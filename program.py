# System Imports

# First Party Imports
from user_interface import UserInterface
from mergesort import MergeSort
from random_numbers import RandomNumbers

# Third Party Imports


def main():
    """main program flow"""

    ui = UserInterface()

    size_of_collection: int = ui.get_size_of_collection()

    my_things_to_sort: RandomNumbers = RandomNumbers(size_of_collection)

    regular_merge = MergeSort()

    regular_merge.timed_sort(my_things_to_sort)

    regular_time: float = regular_merge.get_run_time()

    ui.display_run_times(regular_time, 0.0)
