def deterministic_quicksort(arr, low, high):
    if low < high:
        # Partition the array using the first element as pivot
        pivot_index = deterministic_partition(arr, low, high)
        
        # Recursively sort elements before and after the partition
        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)

def deterministic_partition(arr, low, high):
    # Use the first element as the pivot
    pivot = arr[low]
    i = low + 1  # Start i just after the pivot

    # Partitioning based on the pivot
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    # Place the pivot in its correct position by swapping it with arr[i - 1]
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1  # Return the index of the pivot
