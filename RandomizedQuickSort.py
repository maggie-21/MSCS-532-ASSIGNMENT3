import random

def randomized_quicksort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = randomized_partition(arr, low, high)
        
        # Recursively sort elements before and after the partition
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

def randomized_partition(arr, low, high):
    # Step 1: Choose a random pivot and swap it with the last element
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    
    # Step 2: Standard partitioning around the pivot
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
