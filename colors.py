# Copyright 2025 Theodore Podewil
# GPL-3.0-or-later

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>. 


# System imports
import os

os.system(
    ""
)  # Required to get the terminal to ALWAYS show colors instead of raw escape codes.


# Decorator to convert Style class to a Singleton
def singleton(cls):
    """Singleton function"""
    return cls()


# Class of different Styles
@singleton
class Style:
    """Contains constants for colors"""

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"
    CLEAR = "\033[H\033[2J"

    def __getattribute__(self, name):
        """Override default dunder method"""
        value = super().__getattribute__(name)
        print(value, end="")
        return value


def print_success(message):
    """Print success message"""
    Style.GREEN  # pylint:disable=W0104
    print(message)
    Style.RESET  # pylint:disable=W0104


def print_warning(message):
    """Print warning message"""
    Style.YELLOW  # pylint:disable=W0104
    print(message)
    Style.RESET  # pylint:disable=W0104


def print_error(message):
    """Print error message"""
    Style.RED  # pylint:disable=W0104
    print(message)
    Style.RESET  # pylint:disable=W0104


def print_primary(message):
    """Print primary message"""
    Style.BLUE  # pylint:disable=W0104
    print(message)
    Style.RESET  # pylint:disable=W0104


def print_info(message):
    """Print info message"""
    Style.CYAN  # pylint:disable=W0104
    print(message)
    Style.RESET  # pylint:disable=W0104
