
def get_max_four_digit_numbers(n, cubes):
    # Sort the cubes in ascending order
    cubes.sort()
    # Initialize the maximum number of distinct four-digit numbers
    max_distinct_numbers = 0
    # Initialize the heap assignments
    heap_assignments = [0] * n
    # Iterate over the possible heap assignments
    for i in range(n):
        # Initialize the current number of distinct four-digit numbers
        distinct_numbers = 0
        # Initialize the current heap assignments
        current_heap_assignments = [0] * n
        # Iterate over the cubes
        for j in range(n):
            # Calculate the current four-digit number
            current_number = cubes[j] * 100 + cubes[(j + i) % n]
            # Check if the current number is distinct
            if current_number not in cubes[0:j] + cubes[(j + 1) % n:]:
                # Increment the current number of distinct four-digit numbers
                distinct_numbers += 1
            # Assign the current cube to the current heap
            current_heap_assignments[j] = (j + i) % n + 1
        # Check if the current number of distinct four-digit numbers is greater than the maximum
        if distinct_numbers > max_distinct_numbers:
            # Update the maximum number of distinct four-digit numbers
            max_distinct_numbers = distinct_numbers
            # Update the heap assignments
            heap_assignments = current_heap_assignments
    # Return the maximum number of distinct four-digit numbers and the heap assignments
    return max_distinct_numbers, heap_assignments

