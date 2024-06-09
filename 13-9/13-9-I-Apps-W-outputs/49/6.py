
def get_max_distinct_numbers(n, cubes):
    # Sort the cubes in non-decreasing order
    cubes.sort()
    # Initialize the first heap with the first n cubes
    heap1 = cubes[:n]
    # Initialize the second heap with the remaining cubes
    heap2 = cubes[n:]
    # Initialize the number of distinct four-digit numbers as 0
    distinct_numbers = 0
    # Loop through each cube in the first heap
    for cube1 in heap1:
        # Get the first two digits of the cube
        first_two_digits = int(str(cube1)[:2])
        # Loop through each cube in the second heap
        for cube2 in heap2:
            # Get the second two digits of the cube
            second_two_digits = int(str(cube2)[2:])
            # Check if the first two digits and the second two digits are different
            if first_two_digits != second_two_digits:
                # Increment the number of distinct four-digit numbers
                distinct_numbers += 1
    # Return the maximum number of distinct four-digit numbers
    return distinct_numbers

