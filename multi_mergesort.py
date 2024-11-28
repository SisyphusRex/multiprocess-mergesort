"""multi merge sort module"""

# System Imports
import multiprocessing
import os

# First Party Imports
from abstract_mergesort import AbstractMergeSort

# Third Party Imports


class MultiMergeSort(AbstractMergeSort):
    """Multiprocess merge sort class"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self._aux = []

    # Main entry point to sort
    def sort(self, mergeable):
        """sort method"""

        processor_count: int = 5
        mergeable_length = len(mergeable)
        chunk_size = mergeable_length // processor_count
        shared_collection = multiprocessing.Array("i", mergeable, lock=True)

        processes = []
        for core in range(processor_count):
            if core < processor_count - 1:
                p = multiprocessing.Process(
                    target=self._do_process,
                    args=(shared_collection, core * chunk_size, chunk_size),
                )
                processes.append(p)
                p.start()
            else:
                final_chunk_size = len(shared_collection[core * chunk_size :])

                p = multiprocessing.Process(
                    target=self._do_process,
                    args=(shared_collection, core * chunk_size, final_chunk_size),
                )
                processes.append(p)
                p.start()
        for p in processes:
            p.join()

        self._update_original_list(mergeable, shared_collection)
        print(mergeable)

        # TODO: fix this mess

        for pair in range(chunk_size):
            if pair < chunk_size - 1:
                bottom_index = pair * chunk_size * 2
                low = 0
                top_index = (pair + 1) * 2 * chunk_size
                high = (2 * chunk_size) - 1
                mid = low + int((high - low) / 2)
                sub_list = shared_collection[bottom_index:top_index]
                print(f"Sublist Length: {len(sub_list)} {sub_list}")
                print(f"chunk size: {chunk_size}")
                print(f"Pair: {pair}, low: {low}, mid: {mid}, high: {high}")
                self._final_merge(sub_list, low, mid, high)
                shared_collection[bottom_index:top_index] = sub_list
                self._update_original_list(mergeable, shared_collection)
                print(f"Pair: {pair} {mergeable}")

            else:
                low = 0
                high = len(shared_collection) - 1
                mid = pair * chunk_size * 2 - 1
                self._final_merge(shared_collection, low, mid, high)

        self._update_original_list(mergeable, shared_collection)

    def _do_process(
        self, shared_collection: list[int], process_index: int, chunk_size: int
    ) -> None:
        """individual process for sorting sublist"""
        process_slice: list[int] = shared_collection[
            process_index : process_index + chunk_size
        ]
        self._populate_aux_initially(process_slice)
        # print(f"chunk size: {chunk_size}")
        self._sort(process_slice, 0, chunk_size - 1)
        shared_collection[process_index : process_index + chunk_size] = process_slice

    def _update_original_list(self, mergeable, shared_collection):
        """method to update original list"""
        for index, item in enumerate(shared_collection):
            mergeable[index] = item

    def _populate_aux_initially(self, mergeable) -> None:
        """method to populate aux array"""
        self._aux = [None for i in range(len(mergeable))]

    def _sort(self, mergeable, low, high):
        """recursive sort method"""
        if high <= low:
            return
        mid = low + int((high - low) / 2)
        self._sort(mergeable, low, mid)
        self._sort(mergeable, mid + 1, high)
        self._merge(mergeable, low, mid, high)

    def _final_merge(self, mergeable, low, mid, high):
        """final merge after processes"""
        self._populate_aux_initially(mergeable)
        self._merge(mergeable, low, mid, high)

    def _merge(self, mergeable, low, mid, high):
        """merge method"""

        self._copy_from_main_to_aux(mergeable, low, high)
        self._merge_from_aux_to_main(mergeable, low, mid, high)
        return

    def _copy_from_main_to_aux(self, mergeable, low, high) -> None:
        """method to copy from main array to aux"""
        for k in range(low, high + 1):
            # print(f"low: {low} high: {high}")
            # print(mergeable)
            self._aux[k] = mergeable[k]

    def _merge_from_aux_to_main(self, mergeable, low, mid, high) -> None:
        """method to merge from aux to main"""
        i = low
        j = mid + 1
        for k in range(low, high + 1):
            if i > mid:  # Index past left subarray max index
                mergeable[k] = self._aux[j]
                j += 1
            elif j > high:  # index past right subarray max index
                mergeable[k] = self._aux[i]
                i += 1
            elif self._aux[j] < self._aux[i]:  # compare
                mergeable[k] = self._aux[j]
                j += 1
            else:
                mergeable[k] = self._aux[i]
                i += 1
