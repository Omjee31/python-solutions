"""
Program: Remove duplicates from a list in Python
Description:
"""
def remove_duplicates_using_loop(list1):
    """
    Removes duplicates from a list while preserving the original order.

    Approach:
    - Create an empty list
    - Traverse the input list
    - Add an element only if it is not already present
    """
    new_list = []

    for element in list1:
        # Check if element is already added
        if element not in new_list:
            new_list.append(element)

    return new_list


def remove_duplicates_using_set(list1):
    """
    Removes duplicates using a set.

    Note:
    - This method is faster
    - Order of elements is NOT preserved
    """
    unique_list = list(set(list1))
    return unique_list


if __name__ == "__main__":
    # Input list with duplicate elements
    list1 = [12, 45, 67, 89, 89, 12, 34, 56, 76, 90, 34]

    # Remove duplicates using loop (order preserved)
    print("Using loop:", remove_duplicates_using_loop(list1))

    # Remove duplicates using set (order not preserved)
    print("Using set :", remove_duplicates_using_set(list1))
