# System Imports

# First Party Imports

# Third Party Imports


class UserInterface:
    """user interface class"""

    def get_size_of_collection(self) -> int:
        """method to get size of collection"""
        print("How many numbers do you want to sort?")
        quantity: int = self.__get_int()

    def __get_int(self):
        """get int method"""
