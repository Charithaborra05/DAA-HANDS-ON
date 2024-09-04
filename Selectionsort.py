from typing import List, Union

def selection_sort(data: List[Union[int, float, str]]) -> List[Union[int, float, str]]:
    """Sorts a list using the selection sort algorithm.
    
    Args:
        data (List[Union[int, float, str]]): The list of elements to be sorted. Supports integers, floats, and strings.

    Returns:
        List[Union[int, float, str]]: The sorted list.

    Raises:
        TypeError: If elements are not of the same type or are not comparable.
    """
    # Check that all elements are of the same type
    if not data:
        return data  # Return early if the list is empty
    
    first_type = type(data[0])
    if any(not isinstance(item, first_type) for item in data):
        raise TypeError("All elements must be of the same type.")

    length = len(data)
    for current_index in range(length):
        # Assume the minimum is the current index
        min_index = current_index
        # Compare against the elements after the current index to find the smallest
        for compare_index in range(current_index + 1, length):
            if data[compare_index] < data[min_index]:
                min_index = compare_index
        # Swap the found minimum element with the element at the current index
        data[current_index], data[min_index] = data[min_index], data[current_index]
    
    return data

# Test Case 1: List with random integers
test_case_1 = [45, 3, 12, 7, 29]
print("Sorted Test Case 1:", selection_sort(test_case_1))

# Test Case 2: List with elements already in ascending order
test_case_2 = [1, 2, 3, 4, 5]
print("Sorted Test Case 2:", selection_sort(test_case_2))

# Test Case 3: List with elements in descending order
test_case_3 = [9, 8, 7, 6, 5]
print("Sorted Test Case 3:", selection_sort(test_case_3))

# Test Case 4: List with all identical elements
test_case_4 = [4, 4, 4, 4]
print("Sorted Test Case 4:", selection_sort(test_case_4))

# Test Case 5: List with a mix of positive and negative numbers
test_case_5 = [-5, 2, -1, 7, 0]
print("Sorted Test Case 5:", selection_sort(test_case_5))

# Test Case 6: List with float numbers
test_case_6 = [3.1, 2.4, 5.6, 1.2]
print("Sorted Test Case 6:", selection_sort(test_case_6))

# Test Case 7: List with strings (sorting lexicographically)
test_case_7 = ["banana", "apple", "cherry", "date"]
print("Sorted Test Case 7:", selection_sort(test_case_7))

# Test Case 8: Mixed types (will raise an exception)
test_case_8 = [2, "apple", 3]
try:
    print("Sorted Test Case 8:", selection_sort(test_case_8))
except TypeError as e:
    print(f"Test Case 8 raised an error: {e}")

# Test Case 9: Empty list
test_case_9 = []
print("Sorted Test Case 9:", selection_sort(test_case_9))

# Test Case 10: Single element list
test_case_10 = [42]
print("Sorted Test Case 10:", selection_sort(test_case_10))

# Test Case 11: List with only one type but mixed comparable and non-comparable types (raises error)
test_case_11 = [2, 3.5, 3]  # mixing int and float
try:
    print("Sorted Test Case 11:", selection_sort(test_case_11))
except TypeError as e:
    print(f"Test Case 11 raised an error: {e}")
