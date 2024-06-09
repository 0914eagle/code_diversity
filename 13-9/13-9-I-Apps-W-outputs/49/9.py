
def max_distinct_numbers(n, cubes):
    # Sort the cubes in non-decreasing order
    cubes.sort()
    
    # Initialize the maximum number of distinct numbers as 0
    max_num_distinct = 0
    
    # Initialize the current number of distinct numbers as 0
    curr_num_distinct = 0
    
    # Initialize the first and second heaps as empty lists
    heap1 = []
    heap2 = []
    
    # Iterate over the cubes
    for i in range(n):
        # If the current cube is greater than or equal to the previous cube, add it to the first heap
        if i == 0 or cubes[i] >= cubes[i-1]:
            heap1.append(cubes[i])
        # Otherwise, add it to the second heap
        else:
            heap2.append(cubes[i])
        
        # Update the current number of distinct numbers
        curr_num_distinct += 1
        
        # If the current number of distinct numbers is greater than the maximum number of distinct numbers, update the maximum number of distinct numbers
        if curr_num_distinct > max_num_distinct:
            max_num_distinct = curr_num_distinct
    
    # Return the maximum number of distinct numbers and the heaps
    return [max_num_distinct, heap1, heap2]

