# System Imports
import builtins
import os

# First Party Imports
from colors import print_error, print_info, print_success, print_warning

# Third Party Imports


class UserInterface:
    """user interface class"""

    MAIN_MENU = [
        "Create list of random numbers",
        "Choose number of processors",
        "Run Merge Sorts",
        "Exit",
    ]
    # region public methods

    def display_main_menu(self):
        """displays main menu"""
        for index, text in enumerate(self.MAIN_MENU):
            print(f"{index}: {text}")

    def get_menu_choice(self) -> int:
        """get menu choice"""
        self.__get_menu_choice_prompt()
        choice = self.__get_input()
        while not self.__is_valid_menu_choice(choice):
            self.__get_menu_choice_prompt()
            choice = self.__get_input()

        return int(choice)

    def display_welcome(self) -> None:
        """method to display welcome"""
        print()
        print_success(
            "This program compares the runtime of multiprocess merge sort vs single process."
        )

        print()

    def get_number_of_processors(self) -> int:
        """method to get number of processors"""
        self.__get_processors_prompt()
        quantity = self.__get_input()

        while not self.__is_valid_processor_quantity(quantity):
            self.__get_processors_prompt()
            quantity = self.__get_input()

        return int(quantity)

    def get_size_of_collection(self) -> int:
        """method to get size of collection"""
        self.__get_size_prompt()

        quantity = self.__get_input()

        while not self.__is_int(quantity):
            self.__get_size_prompt()
            quantity = self.__get_input()

        return int(quantity)

    def display_creating_list_message(self):
        """method to display creating list message"""
        print("Populating the list with random numbers...", flush=True)
        print()

    def display_multi_process_message(self):
        """display single process message"""
        print("Performing multi process MergeSort...", flush=True)
        print()

    def display_multi_process_success(self, run_time):
        """display sucess message and runtime"""
        print("Multi process MergeSort completed in:")
        print_success(f"{run_time:5f} seconds")
        print()

    def display_single_process_message(self):
        """display single process message"""
        print("Performing single process MergeSort...", flush=True)
        print()

    def display_single_process_success(self, run_time: float):
        """display success message and runtime"""
        print("Single process MergeSort completed in:")
        print_success(f"{run_time:5f} seconds")
        print()

    def display_run_times(
        self,
        regular_run: float,
        multi_run: float,
        size_of_collection: int,
        number_of_processors: int,
    ) -> None:
        """method to display run times"""
        print_success(f"Size of list: {size_of_collection}")
        print_success(f"Number of Processors: {number_of_processors}")
        print_success(f"Single Process: {regular_run:5f}s")
        print_success(f"Multiprocess:   {multi_run:5f}s")
        print()

    def display_no_processors_error_message(self):
        """no processors message"""
        print_error("You must select a number of processors to use first.")
        print()

    def display_no_collection_error_message(self):
        """no collection message"""
        print_error("You must create a list of random numbers first.")
        print()

    # region private methods
    def __get_input(self) -> str:
        """get input method"""

        my_input = input(">")
        print()

        return my_input

    def __get_menu_choice_prompt(self):
        """method to display prompt"""
        print_info("Enter your selection.")

    def __get_processors_prompt(self) -> None:
        """method to display processor prompt"""
        total_processors = os.cpu_count()
        print_info(f"Your computer has {total_processors} processors.")
        print_info("How many would you like to use?")

    def __get_size_prompt(self) -> None:
        """method to display get size prompt"""
        print_info("How many numbers do you want to sort?")

    def __is_valid_menu_choice(self, choice):
        """method to validate menu choice"""
        if self.__is_int(choice):
            if int(choice) in range(len(self.MAIN_MENU)):
                return True
            else:
                self.__display_not_in_menu_error_message()
                return False
        else:
            return False

    def __is_valid_processor_quantity(self, quantity):
        """methd to verify if is valid processor quantity"""
        if self.__is_int(quantity):
            if 0 < int(quantity) <= os.cpu_count():
                return True
            else:
                self.__display_not_valid_cpu_count_error_message()
                return False
        else:
            return False

    def __is_int(self, to_test) -> bool:
        """method to verify if is int"""
        try:
            x: int = int(to_test)
        except ValueError:
            self.__display_not_int_error_message()
            return False
        return True

    def __display_not_in_menu_error_message(self):
        """method to display menu error message"""
        print_error("Not a valid menu choice.")
        print()

    def __display_not_valid_cpu_count_error_message(self):
        """displays not valid cpu count message"""
        print_error("Not a valid number of Processors.")
        print()

    def __display_not_int_error_message(self):
        """display not int error message"""
        print_error("Input is not an integer.")
        print()
