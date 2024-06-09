
def get_maximum_distinct_numbers(n, cubes):
    # Sort the cubes in ascending order
    cubes.sort()
    
    # Initialize the maximum number of distinct numbers and the corresponding heap assignments
    max_distinct_numbers = 0
    heap_assignments = [0] * n
    
    # Iterate over the cubes and check if they can be placed in the first or second heap
    for i in range(n):
        if cubes[i] // 10 == cubes[i % n] % 10:
            # If the cube can be placed in the first heap, assign it to the first heap and update the maximum number of distinct numbers
            heap_assignments[i] = 1
            max_distinct_numbers += 1
        else:
            # If the cube cannot be placed in the first heap, assign it to the second heap
            heap_assignments[i] = 2
    
    # Return the maximum number of distinct numbers and the heap assignments
    return max_distinct_numbers, heap_assignments

