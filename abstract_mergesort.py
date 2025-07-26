# Copyright 2025 Theodore Podewil
# GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 


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
