# System Imports
import builtins

# First Party Imports
from colors import print_error, print_info, print_success, print_warning

# Third Party Imports


class UserInterface:
    """user interface class"""

    # region public methods
    def display_welcome(self) -> None:
        """method to display welcome"""
        print(
            "This program compares the runtime of multiprocess merge sort vs regular."
        )
        print("Press ctrl + c to exit")
        print()

    def get_size_of_collection(self) -> int:
        """method to get size of collection"""
        self.__get_size_prompt()

        quantity = self.__get_input()

        while not self.__is_int(quantity):
            self.__get_size_prompt()
            quantity = self.__get_input()

        return int(quantity)

    def display_run_times(self, regular_run: float, multi_run: float) -> None:
        """method to display run times"""
        print(f"{regular_run:5f}s Regular")
        print(f"{multi_run:5f}s Multiprocess")

    # region private methods
    def __get_input(self) -> str:
        """get input method"""

        my_input = input(">")

        return my_input

    def __get_size_prompt(self) -> None:
        """method to display get size prompt"""
        print("How many numbers do you want to sort?")

    def __is_int(self, to_test) -> bool:
        """method to verify if is int"""
        try:
            x: int = int(to_test)
        except ValueError:
            self.__display_not_int_error_message()
            return False
        return True

    def __display_not_int_error_message(self):
        """display not int error message"""
        print_error("Input is not an integer.")
