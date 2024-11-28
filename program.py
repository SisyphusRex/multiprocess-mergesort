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
    sorted_deep_copy = shared_memory_process_test(deep_copy_collection)
    print(sorted_deep_copy)

def shared_memory_process_test(collection: list[int]) -> list[int]:
    """method to pass shared memory array to processes"""
    processor_count: int = os.cpu_count()
    collection_length = len(collection)
    chunk_size: int = collection_length // processor_count
    shared_collection = multiprocessing.Array('i', collection, lock=True)

    processes = []
    for core in range(processor_count):
        p = multiprocessing.Process(target=do_process, args=(shared_collection, core * chunk_size, chunk_size,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

    sorted_collection = []
    for i in shared_collection:
        sorted_collection.append(i)
    return sorted_collection

def do_process(shared_collection, process_index, chunk_size):
    """do stuff with shared memory collection"""
    print(f"chunk size: {chunk_size}")
    first_str = ""
    for i in shared_collection:
        first_str += str(i)
        first_str += " "
    print(first_str)
    shared_collection[process_index : process_index + chunk_size] = sorted(shared_collection[process_index : process_index + chunk_size])
    second_str = ""
    for i in shared_collection:
        second_str += str(i)
        second_str += " "
    print(second_str)



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
