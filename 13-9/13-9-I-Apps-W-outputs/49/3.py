
def get_max_distinct_numbers(n, cubes):
    # Sort the cubes in ascending order
    cubes.sort()
    # Initialize the first heap with the first n cubes
    first_heap = cubes[:n]
    # Initialize the second heap with the remaining cubes
    second_heap = cubes[n:]
    # Initialize the number of distinct four-digit numbers as 0
    distinct_numbers = 0
    # Loop through each cube in the first heap
    for i in range(n):
        # Get the first two digits of the current cube
        first_two_digits = str(first_heap[i])[:2]
        # Loop through each cube in the second heap
        for j in range(len(second_heap)):
            # Get the second two digits of the current cube
            second_two_digits = str(second_heap[j])[-2:]
            # Check if the first two digits and the second two digits are equal
            if first_two_digits == second_two_digits:
                # Increment the number of distinct four-digit numbers
                distinct_numbers += 1
                # Break out of the inner loop
                break
    # Return the number of distinct four-digit numbers
    return distinct_numbers

