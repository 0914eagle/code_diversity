
def max_distinct_numbers(n, cubes):
    # Sort the cubes in non-decreasing order
    cubes.sort()
    
    # Initialize the first and second heaps with the first n cubes
    heap1 = cubes[:n]
    heap2 = cubes[n:]
    
    # Initialize the maximum number of distinct numbers as 0
    max_distinct_nums = 0
    
    # Loop through each cube in the first heap
    for i in range(n):
        # Get the number on the current cube
        num1 = heap1[i]
        
        # Loop through each cube in the second heap
        for j in range(len(heap2)):
            # Get the number on the current cube
            num2 = heap2[j]
            
            # Check if the number can be obtained by combining the two numbers
            if str(num1) in str(num2) and str(num2) not in str(num1):
                # If the number can be obtained, add it to the list of distinct numbers
                distinct_nums.append(num1 * 100 + num2)
                
    # Return the maximum number of distinct numbers
    return max(distinct_nums)

