
def get_max_distinct_numbers(n, cubes):
    # Sort the cubes in non-decreasing order
    cubes.sort()
    # Initialize the maximum number of distinct numbers as 0
    max_distinct_numbers = 0
    # Initialize the heaps as empty lists
    heap1 = []
    heap2 = []
    # Iterate over the cubes
    for i in range(n):
        # If the current cube is less than or equal to the sum of the two largest numbers in the first heap, add it to the first heap
        if cubes[i] <= heap1[0] + heap1[1]:
            heap1.append(cubes[i])
        # Otherwise, add it to the second heap
        else:
            heap2.append(cubes[i])
        # Get the maximum number of distinct numbers by counting the number of unique numbers in the first heap and the number of unique numbers in the second heap
        max_distinct_numbers = max(max_distinct_numbers, len(set(heap1)) * len(set(heap2)))
    # Return the maximum number of distinct numbers and the heaps
    return max_distinct_numbers, heap1, heap2

