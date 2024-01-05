def bubble_sort(arr):
    """
    The bubble_sort function implements the bubble sort algorithm to sort an array in ascending order.
    
    :param arr: The parameter "arr" is a list of elements that you want to sort using the bubble sort
    algorithm
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break

def insertion_sort(arr):
    """
    The `insertion_sort` function implements the insertion sort algorithm to sort an array in ascending
    order.
    
    :param arr: The parameter "arr" is a list of elements that you want to sort using the insertion sort
    algorithm
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    """
    The selection_sort function implements the selection sort algorithm to sort an array in ascending
    order.
    
    :param arr: The parameter "arr" is a list of elements that you want to sort using the selection sort
    algorithm
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def merge_sort(arr):
    """
    The `merge_sort` function implements the merge sort algorithm to sort an input array in ascending
    order.
    
    :param arr: The parameter `arr` is a list of elements that needs to be sorted using the merge sort
    algorithm
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    """
    The quick_sort function implements the quicksort algorithm to sort an array in ascending order.
    
    :param arr: The parameter `arr` is a list of elements that you want to sort using the quicksort
    algorithm
    :return: a sorted version of the input array.
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)