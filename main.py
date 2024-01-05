from truth_table import truth_table
from generate_qr_code import generate_qr_code
from link_shortner import link_shortner
from count_lines import count_lines
from count_words import count_words
from get_fact import get_fact
from lotto_numbers import lotto_numbers
from collect_filenames import collect_filenames
from merge_files_by_extension import merge_files_by_extension
from sorting import bubble_sort, merge_sort, insertion_sort, selection_sort, quick_sort
from searching import binary_search, linear_search
import os

if __name__ == "__main__":
    print("short link:", link_shortner("https://www.youtube.com/watch?v=Un6sYuYTZyI"))
        
    print(get_fact(5))
        
    print("Number of lines in the file:", count_lines("test.txt"))
    print("Unique words in the file:")
    word_counts = count_words("test.txt")
    for word in word_counts:
        print(word, word_counts[word])
        
    print("filenames have been collected:", collect_filenames('.py'))
    os.remove("filenames.txt")
        
    print("Merged file created:", merge_files_by_extension(".py"))
    os.remove("merged.py")

    print("lotto numbers are in the file:", lotto_numbers("combinations.txt"))
    os.remove("combinations.txt")

    generate_qr_code("https://www.bbc.com/news/technology-64718842", "qr_code.png")
    os.remove("qr_code.png")

    expression = "((A and B) or C) and D or R"
    truth_table(expression)

    # Create an unsorted list for testing
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]

    # Demonstrate each sorting algorithm
    print("Unsorted List:", unsorted_list)

    # Bubble Sort
    bubble_sorted = unsorted_list.copy()
    bubble_sort(bubble_sorted)
    print("Bubble Sort:", bubble_sorted)

    # Insertion Sort
    insertion_sorted = unsorted_list.copy()
    insertion_sort(insertion_sorted)
    print("Insertion Sort:", insertion_sorted)

    # Selection Sort
    selection_sorted = unsorted_list.copy()
    selection_sort(selection_sorted)
    print("Selection Sort:", selection_sorted)

    # Merge Sort
    merge_sorted = unsorted_list.copy()
    merge_sort(merge_sorted)
    print("Merge Sort:", merge_sorted)

    # Quick Sort
    quick_sorted = unsorted_list.copy()
    quick_sorted = quick_sort(quick_sorted)
    print("Quick Sort:", quick_sorted)

    my_list = [1, 3, 5, 7, 9, 11]
    target_value = 7

    # Using linear search
    linear_result = linear_search(my_list, target_value)

    if linear_result != -1:
        print(f"Linear Search: {target_value} found at index {linear_result}.")
    else:
        print(f"Linear Search: {target_value} not found in the list.")

    # Using binary search (assuming the list is sorted)
    binary_result = binary_search(my_list, target_value)

    if binary_result != -1:
        print(f"Binary Search: {target_value} found at index {binary_result}.")
    else:
        print(f"Binary Search: {target_value} not found in the list.")