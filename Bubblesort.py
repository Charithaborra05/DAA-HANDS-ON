from typing import List, Union

def bubble_sort(sequence: List[Union[int, str]]) -> List[Union[int, str]]:
    """Sorts a list using the bubble sort algorithm with optimization to stop early if no swaps are needed.
    
    Args:
        sequence (List[Union[int, str]]): The list of integers or strings to be sorted.

    Returns:
        List[Union[int, str]]: The sorted list.
    """
    length = len(sequence)
    for pass_num in range(length):
        swapped = False  # Track if any swaps were made in this pass
        for index in range(0, length - pass_num - 1):
            if sequence[index] > sequence[index + 1]:
                # Swap if the current element is greater than the next
                sequence[index], sequence[index + 1] = sequence[index + 1], sequence[index]
                swapped = True
        if not swapped:
            break  # Stop if no swaps were made
    return sequence

# Test Case 1: Unordered list of integers
test_case_1 = [45, 3, 12, 7, 29]
print("Sorted Test Case 1:", bubble_sort(test_case_1))

# Test Case 2: List with duplicate integers
test_case_2 = [5, 5, 5, 5]
print("Sorted Test Case 2:", bubble_sort(test_case_2))

# Test Case 3: List with negative integers
test_case_3 = [-1, -3, 2, 0, -7]
print("Sorted Test Case 3:", bubble_sort(test_case_3))

# Test Case 4: List of strings (sorting lexicographically)
test_case_4 = ["apple", "orange", "banana", "pear"]
print("Sorted Test Case 4:", bubble_sort(test_case_4))

# Test Case 5: Empty list
test_case_5 = []
print("Sorted Test Case 5:", bubble_sort(test_case_5))

# Test Case 6: Single element list
test_case_6 = [42]
print("Sorted Test Case 6:", bubble_sort(test_case_6))

# Test Case 7: Already sorted list
test_case_7 = [1, 2, 3, 4, 5]
print("Sorted Test Case 7:", bubble_sort(test_case_7))

# Test Case 8: List with mixed types (integers and strings)
# This test will raise a TypeError because bubble_sort expects elements to be of the same type.
test_case_8 = [1, "apple", 2, "banana"]
try:
    print("Sorted Test Case 8:", bubble_sort(test_case_8))
except TypeError as e:
    print(f"Test Case 8 raised an error: {e}")
