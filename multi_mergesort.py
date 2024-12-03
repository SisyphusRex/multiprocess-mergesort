"""multi merge sort module"""

# System Imports
import multiprocessing
import os

# First Party Imports
from abstract_mergesort import AbstractMergeSort

# Third Party Imports


class MultiMergeSort(AbstractMergeSort):
    """Multiprocess merge sort class"""

    def __init__(self, processor_count):
        """constructor"""
        super().__init__()
        self._aux = []
        self._chunk_size: int = None
        self._final_chunk_size: int = None
        self._shared_collection: list[int] = None
        self._processor_count = processor_count

    # Main entry point to sort
    def sort(self, mergeable):
        """sort method"""

        self._shared_collection = multiprocessing.Array("i", mergeable, lock=True)
        collection_length = len(self._shared_collection)
        self._chunk_size = collection_length // self._processor_count

        self._multi_sort()
        self._merge_chunks()
        self._update_original_list(mergeable)

    def _merge_chunks(self):
        """method to merge separate sorted chunks formed by mult_sort"""
        for sublist_to_merge in range(self._processor_count):
            if sublist_to_merge < self._processor_count - 2:
                low = 0
                mid = self._chunk_size + sublist_to_merge * self._chunk_size - 1
                high = self._chunk_size * 2 + sublist_to_merge * self._chunk_size - 1
                sublist = self._shared_collection[: high + 1]
                self._final_merge(sublist, low, mid, high)
                self._shared_collection[: high + 1] = sublist

            else:
                low = 0
                mid = self._chunk_size + sublist_to_merge * self._chunk_size - 1
                high = len(self._shared_collection) - 1
                self._final_merge(self._shared_collection, low, mid, high)

    def _multi_sort(self):
        """divide array into subarrays and assign process to sort"""
        processes = []
        for core in range(self._processor_count):
            if core < self._processor_count - 1:
                p = multiprocessing.Process(
                    target=self._do_process,
                    args=(
                        self._shared_collection,
                        core * self._chunk_size,
                        self._chunk_size,
                    ),
                )
                processes.append(p)
                p.start()
            else:
                self._final_chunk_size = len(
                    self._shared_collection[core * self._chunk_size :]
                )
                p = multiprocessing.Process(
                    target=self._do_process,
                    args=(
                        self._shared_collection,
                        core * self._chunk_size,
                        self._final_chunk_size,
                    ),
                )
                processes.append(p)
                p.start()
        for p in processes:
            p.join()

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

    def _update_original_list(self, mergeable):
        """method to update original list"""
        for index, item in enumerate(self._shared_collection):
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
