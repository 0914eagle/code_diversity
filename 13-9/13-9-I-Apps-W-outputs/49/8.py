
def get_maximum_distinct_numbers(n, cubes):
    # Sort the cubes in non-decreasing order
    cubes.sort()
    # Initialize the first heap with the first n cubes
    first_heap = cubes[:n]
    # Initialize the second heap with the remaining cubes
    second_heap = cubes[n:]
    # Initialize the number of distinct four-digit numbers to 0
    distinct_numbers = 0
    # Loop through each cube in the first heap
    for i in range(n):
        # Get the number on the current cube
        current_number = first_heap[i]
        # Loop through each cube in the second heap
        for j in range(n):
            # Get the number on the current cube
            current_number_2 = second_heap[j]
            # Check if the number is not already present in the first heap
            if current_number_2 not in first_heap:
                # Add the number to the first heap
                first_heap.append(current_number_2)
                # Increment the number of distinct four-digit numbers
                distinct_numbers += 1
                break
    # Return the maximum number of distinct four-digit numbers
    return distinct_numbers

