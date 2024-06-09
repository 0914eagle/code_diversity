
def solve(arr):
    # Calculate the sum of the array
    sum_arr = sum(arr)
    
    # Initialize a variable to store the minimum number of elements to insert
    min_elements = 0
    
    # Iterate through the array
    for i in range(len(arr)):
        # Calculate the sum of the current subarray
        sum_subarr = sum(arr[:i+1])
        
        # If the sum of the current subarray is 0, we need to insert elements
        if sum_subarr == 0:
            # Calculate the number of elements to insert
            num_elements = abs(sum_arr) - abs(sum_subarr)
            
            # Update the minimum number of elements to insert
            min_elements = max(min_elements, num_elements)
    
    return min_elements

