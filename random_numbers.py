# Copyright 2025 Theodore Podewil
# GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 


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
            random_number_list.append(random.randint(0, 1000))
            i += 1
        return random_number_list
