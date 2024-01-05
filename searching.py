def linear_search(arr, target):
    """
    The linear_search function searches for a target value in an array and returns the index of the
    target if found, otherwise it returns -1.
    
    :param arr: The arr parameter is a list or array in which we want to search for the target value
    :param target: The target parameter is the value that we are searching for in the array
    :return: the index of the target element in the array if it is found, and -1 if the target element
    is not present in the array.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    """
    The binary_search function implements the binary search algorithm to find the index of a target
    element in a sorted array, returning -1 if the target is not found.
    
    :param arr: The `arr` parameter is the sorted array in which we want to search for the `target`
    value
    :param target: The target parameter is the value that we are searching for in the array
    :return: the index of the target element in the array if it is found, or -1 if the target element is
    not present in the array.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2 

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1