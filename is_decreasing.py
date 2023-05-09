# Author: Justin Huang
# GitHub username: huangjus
# Date: 5/9/23
# Description: The function checks if the list has only one element, in which case it returns True. Otherwise, it
# compares the first two elements of the list and returns False if the first element is greater than or equal to
# the second. If the first element is less than the second, it recursively calls the function with the rest of the
# list (excluding the first element) and returns the result of that call. This process continues until the list is
# reduced to a length of 1, at which point the function returns True.

def is_decreasing(lst):
    """
    This function takes a list of numbers as input and recursively checks if the elements of the list are strictly
     decreasing or not.
    """
    if len(lst) <= 1:
        return True
    else:
        if lst[0] <= lst[1]:
            return False
        else:
            return is_decreasing(lst[1:])
