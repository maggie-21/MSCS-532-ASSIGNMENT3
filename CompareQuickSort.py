from RandomizedQuickSort import randomized_quicksort
from DeterministicQuickSort import deterministic_quicksort

import time
import random
import sys

# Increase recursion limit
sys.setrecursionlimit(20000)  # Adjust this value as needed based on array size

# Define functions to measure execution time of each quicksort
def measure_randomized_quicksort_time(arr):
    start_time = time.time()
    randomized_quicksort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

def measure_deterministic_quicksort_time(arr):
    start_time = time.time()
    deterministic_quicksort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

# Test arrays with different cases
array_sizes = [1000, 5000, 10000]  # Testing with different input sizes

# 1. Empty array test
empty_array = []
time_empty_random = measure_randomized_quicksort_time(empty_array)
time_empty_deterministic = measure_deterministic_quicksort_time(empty_array)
print(f"Empty array sorted in (Randomized): {time_empty_random:.6f} seconds")
print(f"Empty array sorted in (Deterministic): {time_empty_deterministic:.6f} seconds")
print("-" * 40)

# Loop through other test arrays with increasing sizes
for size in array_sizes:
    # 2. Randomly generated array
    random_array = [random.randint(1, 10000) for _ in range(size)]
    time_random_randomized = measure_randomized_quicksort_time(random_array[:])
    time_random_deterministic = measure_deterministic_quicksort_time(random_array[:])
    print(f"Random array of size {size} sorted in (Randomized): {time_random_randomized:.6f} seconds")
    print(f"Random array of size {size} sorted in (Deterministic): {time_random_deterministic:.6f} seconds")

    # 3. Already sorted array
    sorted_array = list(range(1, size + 1))
    time_sorted_randomized = measure_randomized_quicksort_time(sorted_array[:])
    time_sorted_deterministic = measure_deterministic_quicksort_time(sorted_array[:])
    print(f"Sorted array of size {size} sorted in (Randomized): {time_sorted_randomized:.6f} seconds")
    print(f"Sorted array of size {size} sorted in (Deterministic): {time_sorted_deterministic:.6f} seconds")

    # 4. Reverse-sorted array
    reverse_sorted_array = list(range(size, 0, -1))
    time_reverse_randomized = measure_randomized_quicksort_time(reverse_sorted_array[:])
    time_reverse_deterministic = measure_deterministic_quicksort_time(reverse_sorted_array[:])
    print(f"Reverse sorted array of size {size} sorted in (Randomized): {time_reverse_randomized:.6f} seconds")
    print(f"Reverse sorted array of size {size} sorted in (Deterministic): {time_reverse_deterministic:.6f} seconds")

    # 5. Array with repeated elements
    repeated_elements_array = [random.choice([1, 2, 3, 4, 5]) for _ in range(size)]
    time_repeated_randomized = measure_randomized_quicksort_time(repeated_elements_array[:])
    time_repeated_deterministic = measure_deterministic_quicksort_time(repeated_elements_array[:])
    print(f"Array with repeated elements of size {size} sorted in (Randomized): {time_repeated_randomized:.6f} seconds")
    print(f"Array with repeated elements of size {size} sorted in (Deterministic): {time_repeated_deterministic:.6f} seconds")

    print("-" * 40)
