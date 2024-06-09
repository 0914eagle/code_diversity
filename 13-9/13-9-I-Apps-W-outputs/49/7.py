
def max_four_digit_numbers(n, cubes):
    # Sort the cubes in ascending order
    cubes.sort()
    # Initialize the maximum number of distinct four-digit numbers as 0
    max_numbers = 0
    # Initialize the heap assignments as empty lists
    heap1 = []
    heap2 = []
    # Iterate over the cubes
    for i in range(n):
        # If the current cube is less than or equal to 99, add it to the first heap
        if cubes[i] <= 99:
            heap1.append(cubes[i])
        # Otherwise, add it to the second heap
        else:
            heap2.append(cubes[i])
        # Get the current number of distinct four-digit numbers
        numbers = get_four_digit_numbers(heap1, heap2)
        # If the current number of distinct four-digit numbers is greater than the maximum, update the maximum and the heap assignments
        if numbers > max_numbers:
            max_numbers = numbers
            heap1_assignment = heap1.copy()
            heap2_assignment = heap2.copy()
    # Return the maximum number of distinct four-digit numbers and the heap assignments
    return max_numbers, heap1_assignment, heap2_assignment

# Function to get the number of distinct four-digit numbers that can be obtained from the heaps
def get_four_digit_numbers(heap1, heap2):
    # Initialize the number of distinct four-digit numbers as 0
    numbers = 0
    # Iterate over the cubes in the first heap
    for i in range(len(heap1)):
        # Get the current cube from the first heap
        cube1 = heap1[i]
        # Iterate over the cubes in the second heap
        for j in range(len(heap2)):
            # Get the current cube from the second heap
            cube2 = heap2[j]
            # If the current cube from the first heap is less than or equal to the current cube from the second heap, skip this combination
            if cube1 <= cube2:
                continue
            # Otherwise, get the four-digit number by concatenating the two digits of the current cube from the first heap with the two digits of the current cube from the second heap
            number = str(cube1) + str(cube2)
            # If the four-digit number has not already been counted, increment the number of distinct four-digit numbers
            if number not in ["1000", "0100", "0010", "0001"]:
                numbers += 1
    # Return the number of distinct four-digit numbers
    return numbers

