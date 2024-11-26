# System Imports
import copy
import os

# First Party Imports
from user_interface import UserInterface
from mergesort import MergeSort
from random_numbers import RandomNumbers
from multi_mergesort import MultiMergeSort

# Third Party Imports


def main():
    """main program flow"""
    ui = UserInterface()
    ui.display_welcome()
    print(os.cpu_count())
    while True:

        size_of_collection: int = ui.get_size_of_collection()

        my_random_generated_numbers: RandomNumbers = RandomNumbers(size_of_collection)
        original_collection = my_random_generated_numbers.collection
        deep_copy_collection = copy.deepcopy(original_collection)
        regular_merge = MergeSort()
        multi_merge = MultiMergeSort()
        regular_merge.timed_sort(original_collection)
        multi_merge.timed_sort(deep_copy_collection)

        regular_time: float = regular_merge.get_run_time()

        multi_time: float = multi_merge.get_run_time()

        ui.display_run_times(regular_time, multi_time)

    exit()
