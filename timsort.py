def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item



def merge(arr, start, mid, end):
    if mid == end:
        return
    merged_arr = []
    left_idx = start
    right_idx = mid + 1

    
    while left_idx <= mid and right_idx <= end:
        if arr[left_idx] < arr[right_idx]:
            merged_arr.append(arr[left_idx])
            left_idx += 1
        else:
            merged_arr.append(arr[right_idx])
            right_idx += 1

    
    while left_idx <= mid:
        merged_arr.append(arr[left_idx])
        left_idx += 1

    
    while right_idx <= end:
        merged_arr.append(arr[right_idx])
        right_idx += 1

    
    for i, sorted_item in enumerate(merged_arr):
        arr[start + i] = sorted_item



def tim_sort(arr):
    n = len(arr)


    min_run = 32  


    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, n - 1))


    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(start + size - 1, n - 1)
            end = min(start + size * 2 - 1, n - 1)
            if mid < end:
                merge(arr, start, mid, end)
        size *= 2
