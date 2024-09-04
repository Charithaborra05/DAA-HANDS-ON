from typing import List, Union

def insertion_sort(elements: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """Sorts a list using the insertion sort algorithm.
    
    Args:
        elements (List[Union[int, float, str]]): The list of elements to be sorted. Supports integers, floats, and strings.

    Returns:
        List[Union[int, float, str]]: The sorted list.

    Raises:
        TypeError: If elements are not of the same type or are not comparable.
    """
    # Check that all elements are of the same type
    if len(set(map(type, elements))) != 1:
        raise TypeError("All elements must be of the same type.")
    
    # Perform insertion sort
    for index in range(1, len(elements)):
        current_value = elements[index]
        position = index - 1
        while position >= 0 and current_value < elements[position]:
            elements[position + 1] = elements[position]
            position -= 1
        elements[position + 1] = current_value
    
    return elements

# Test Case 1: Random list of integers
test_case_1 = [29, 1, 16, 8, 44]
print("Sorted Test Case 1:", insertion_sort(test_case_1))

# Test Case 2: List with all elements already in ascending order
test_case_2 = [2, 4, 6, 8, 10]
print("Sorted Test Case 2:", insertion_sort(test_case_2))

# Test Case 3: List with elements in descending order
test_case_3 = [30, 25, 20, 15, 10]
print("Sorted Test Case 3:", insertion_sort(test_case_3))

# Test Case 4: List with repeated values
test_case_4 = [7, 7, 7, 7]
print("Sorted Test Case 4:", insertion_sort(test_case_4))

# Test Case 5: List with a mix of positive and negative numbers
test_case_5 = [-5, 3, -1, 8, 0]
print("Sorted Test Case 5:", insertion_sort(test_case_5))

# Test Case 6: List with float numbers
test_case_6 = [3.2, 1.1, 4.6, 2.5]
print("Sorted Test Case 6:", insertion_sort(test_case_6))

# Test Case 7: List with strings
test_case_7 = ["banana", "apple", "cherry", "date"]
print("Sorted Test Case 7:", insertion_sort(test_case_7))

# Test Case 8: Mixed types (will raise an exception)
test_case_8 = [2, "apple", 3]
try:
    print("Sorted Test Case 8:", insertion_sort(test_case_8))
except TypeError as e:
    print(f"Test Case 8 raised an error: {e}")

# Test Case 9: Empty list
test_case_9 = []
print("Sorted Test Case 9:", insertion_sort(test_case_9))

# Test Case 10: Single element list
test_case_10 = [42]
print("Sorted Test Case 10:", insertion_sort(test_case_10))
