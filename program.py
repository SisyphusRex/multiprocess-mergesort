# System Imports
import copy
import os
import multiprocessing
import sys

# First Party Imports
from user_interface import UserInterface
from mergesort import MergeSort
from random_numbers import RandomNumbers
from multi_mergesort import MultiMergeSort
from errors import NoCollection, NoProcessors

# Third Party Imports


def main():
    """main program flow"""
    ui = UserInterface()
    ui.display_welcome()
    original_collection = None
    deep_copy_collection = None
    number_of_processors = None

    while True:
        ui.display_main_menu()
        choice = ui.get_menu_choice()

        match choice:
            case 0:
                size_of_collection: int = ui.get_size_of_collection()
                my_random_generated_numbers: RandomNumbers = RandomNumbers(
                    size_of_collection
                )
                original_collection = my_random_generated_numbers.collection
                deep_copy_collection = copy.deepcopy(original_collection)
            case 1:
                number_of_processors = ui.get_number_of_processors()
            case 2:
                try:
                    if original_collection is None:
                        raise NoCollection
                    if number_of_processors is None:
                        raise NoProcessors
                    regular_merge = MergeSort()
                    multi_merge = MultiMergeSort(number_of_processors)
                    regular_merge.timed_sort(original_collection)
                    multi_merge.timed_sort(deep_copy_collection)
                    regular_time: float = regular_merge.get_run_time()
                    multi_time: float = multi_merge.get_run_time()
                    ui.display_run_times(
                        regular_time,
                        multi_time,
                        size_of_collection,
                        number_of_processors,
                    )
                except NoProcessors:
                    ui.display_no_processors_error_message()
                except NoCollection:
                    ui.display_no_collection_error_message()
            case 3:
                sys.exit()
