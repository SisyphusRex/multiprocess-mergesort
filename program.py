# System Imports
import copy
import os
import multiprocessing

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



    size_of_collection: int = ui.get_size_of_collection()

    my_random_generated_numbers: RandomNumbers = RandomNumbers(size_of_collection)
    original_collection = my_random_generated_numbers.collection
    deep_copy_collection = copy.deepcopy(original_collection)
    regular_merge = MergeSort()
    multi_merge = MultiMergeSort()
    regular_merge.timed_sort(original_collection)
    # multi_merge.timed_sort(deep_copy_collection)

    regular_time: float = regular_merge.get_run_time()

    # multi_time: float = multi_merge.get_run_time()

    ui.display_run_times(regular_time, 0.0)
    print(deep_copy_collection)
    shared_deep_copy = multiprocessing.Array('i', deep_copy_collection, lock=True)
    test_method_process(shared_deep_copy)
    my_list = []
    for i in shared_deep_copy:
        my_list.append(i)
    print(my_list)



def process_slice(data_slice: list[int]):
    """method to do something to slice"""
    data_slice.sort()


def test_method_process(collection):
    """test method using process"""
    processor_count: int = os.cpu_count()
    chunk_size: int = len(collection) // processor_count

    slices = [collection[i : i + chunk_size] for i in range(0, len(collection), chunk_size)]

    processes = []
    for slice_data in slices:
        p = multiprocessing.Process(target=process_slice, args=(slice_data,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


# NOTE: DO NOT RUN THIS METHOD!!!!!!!!!!!!!!!!!!! CPU will take off
def test_method_pool(collection):
    """test method using pool"""
    processor_count: int = os.cpu_count()
    chunk_size: int = len(collection) // processor_count

    slices = [collection[i : i + chunk_size] for i in range(0, len(collection), chunk_size)]

    with multiprocessing.Pool() as pool:
        pool.map(process_slice, slices)
