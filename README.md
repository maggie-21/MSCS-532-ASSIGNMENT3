# MSCS-532-ASSIGNMENT3

## Overview
This assignment explores and compares two fundamental algorithms: **Randomized Quicksort** and **Hashing with Chaining**. The objective is to analyze their efficiency, scalability, and performance across different input types, as well as to implement and test each algorithm.

- **Randomized Quicksort**: A sorting algorithm that uses a random pivot selection to maintain average-case \(O(n \log n)\) performance, even on challenging inputs like sorted or reverse-sorted arrays.
- **Hashing with Chaining**: A hash table implementation that uses chaining to handle collisions, maintaining efficient insert, search, and delete operations even with a high load factor.

## Project Structure
- `RandomizedQuickSort.py`: Contains the `randomized_quicksort` function, which implements Randomized Quicksort using random pivot selection.
- `DeterministicQuickSort.py`: Contains the `deterministic_quicksort` function, which implements Deterministic Quicksort using the first element as the pivot.
- `HashingWithChaining.py`: Contains the `HashTable` class, implementing a hash table with chaining to handle collisions.
- `CompareQuickSort.py`: Script to run and compare Randomized and Deterministic Quicksort on different input types.
- `TestRandomizedQuickSort.py`: Script with test cases for Randomized Quicksort.
- `TestHashTableWithChaining.py`: Script with test cases for the hash table with chaining.



## Requirements
- **Python 3.x** is required to run the scripts.
- No additional libraries are needed as this implementation uses standard Python libraries.

## Usage

### 1. Randomized Quicksort
To test the **Randomized Quicksort** implementation, you can run the `TestRandomizedQuickSort.py` script:

```bash
python3 TestRandomizedQuickSort.py
```
This script:

- Tests the performance of Randomized Quicksort on various input types (empty array, random array, sorted array, reverse-sorted array, and array with repeated elements).
- Compares execution times across different input sizes, verifying the \(O(n \log n)\) average-case complexity.

### 2. Compare Randomized Quicksort and Deterministic Quicksort
To compare **Deterministic Quicksort** with **Randomized Quicksort**, you can run the `CompareQuickSort.py` script:

```bash
python3 CompareQuickSort.py
```
This script:

- Compares execution times of Randomized and Deterministic Quicksort on the same input types and sizes.
- Demonstrates the effect of pivot selection on performance, particularly for sorted and reverse-sorted arrays.

### 3. Hashing with Chaining
To test the **Hashing with Chaining** implementation, you can run the `TestHashTableWithChaining.py` script:

```bash
python3 TestHashTableWithChaining.py
```
This script:

- Tests the functionality of the hash table with chaining, including insert, search, and delete operations.
- Verifies collision handling by inserting multiple keys that hash to the same index.
- Demonstrates performance under various load factors.



### Conclusion
This project provides a comprehensive analysis of **Randomized Quicksort** and **Hashing with Chaining**, exploring their strengths, limitations, and best use cases. The test scripts allow users to observe the efficiency and robustness of each algorithm under different input scenarios.
