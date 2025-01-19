# def tim_sort(arr):
#     if len(arr) <= 50 and len(arr) > 5:
#         min_run = 5
#     elif len(arr) < 5:
#         min_run = len(arr)
#     else:
#         min_run = len(arr) // 10
#     n = len(arr)
#
#     # Perform insertion sort for each subarray
#     for i in range(0, n, min_run):
#         insertion_sort(arr, i, min(i + min_run - 1, n - 1))
#
#     # Iteratively merge subarrays of increasing size
#     size = min_run
#     while size < n:
#         for start in range(0, n, size * 2):
#             mid = min(start + size - 1, n - 1)  # Ensure 'mid' doesn't go out of bounds
#             end = min((start + size * 2 - 1), (n - 1))  # Ensure 'end' doesn't go out of bounds
#             if mid < end:  # Only merge if mid is less than end
#                 merge(arr, start, mid, end)
#         size *= 2
#
# def insertion_sort(arr, left, right):
#     for i in range(left + 1, right + 1):
#         key_item = arr[i]
#         j = i - 1
#         while j >= left and arr[j] > key_item:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key_item
#
# def merge(arr, start, mid, end):
#     if mid == end:
#         return
#     merged_arr = []
#     left_idx = start
#     right_idx = mid + 1
#
#     # Merge elements while both indices are within bounds
#     while left_idx <= mid and right_idx <= end:
#         if arr[left_idx] < arr[right_idx]:
#             merged_arr.append(arr[left_idx])
#             left_idx += 1
#         else:
#             merged_arr.append(arr[right_idx])
#             right_idx += 1
#
#     # If there are remaining elements in the left half, add them
#     while left_idx <= mid:
#         merged_arr.append(arr[left_idx])
#         left_idx += 1
#
#     # If there are remaining elements in the right half, add them
#     while right_idx <= end:
#         merged_arr.append(arr[right_idx])
#         right_idx += 1
#
#     # Copy the sorted elements back into the original array
#     for i, sorted_item in enumerate(merged_arr):
#         arr[start + i] = sorted_item

import random


# Insertion Sort is used for small runs
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item


# Merge function to merge two sorted subarrays
def merge(arr, start, mid, end):
    if mid == end:
        return
    merged_arr = []
    left_idx = start
    right_idx = mid + 1

    # Merge elements while both indices are within bounds
    while left_idx <= mid and right_idx <= end:
        if arr[left_idx] < arr[right_idx]:
            merged_arr.append(arr[left_idx])
            left_idx += 1
        else:
            merged_arr.append(arr[right_idx])
            right_idx += 1

    # If there are remaining elements in the left half, add them
    while left_idx <= mid:
        merged_arr.append(arr[left_idx])
        left_idx += 1

    # If there are remaining elements in the right half, add them
    while right_idx <= end:
        merged_arr.append(arr[right_idx])
        right_idx += 1

    # Copy the sorted elements back into the original array
    for i, sorted_item in enumerate(merged_arr):
        arr[start + i] = sorted_item


# The Timsort algorithm combining Insertion Sort and Merge Sort
def tim_sort(arr):
    n = len(arr)

    # A typical value for min_run in Timsort
    min_run = 32  # This can be fine-tuned for specific scenarios

    # Sort small chunks with insertion sort
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, n - 1))

    # Now start merging sorted subarrays of increasing size
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(start + size - 1, n - 1)
            end = min(start + size * 2 - 1, n - 1)
            if mid < end:
                merge(arr, start, mid, end)
        size *= 2