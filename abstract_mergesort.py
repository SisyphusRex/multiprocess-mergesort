"""abstract merge sort module"""

# System imports
from abc import ABC, abstractmethod
import time

# First Party Imports

# Third Party Imports


class AbstractMergeSort(ABC):
    """abstract mergesort class"""

    def __init__(self):
        # constructor
        self._run_time: float = None

    # region public methods
    @abstractmethod
    def sort(self, mergeable: list[int]) -> None:
        """method to run merge sort"""

    def timed_sort(self, mergeable: list[int]) -> None:
        """sort with timer"""
        start_time = time.perf_counter()
        self.sort(mergeable)
        end_time = time.perf_counter()
        self._run_time = end_time - start_time

    def get_run_time(self) -> float:
        """method to get run time"""
        return self._run_time

    # region private methods
    def __format_run_time(self) -> None:
        """format the run time"""
        return f"{self._run_time:5f}"
