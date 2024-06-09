
def get_min_operations(arr):
    # Calculate the sum of the array
    sum_arr = sum(arr)
    
    # Initialize the minimum number of operations to 0
    min_operations = 0
    
    # Iterate through the array
    for i in range(len(arr)):
        # Calculate the sum of the current subarray
        sum_subarr = sum(arr[i:])
        
        # If the sum of the current subarray is 0, increment the minimum number of operations
        if sum_subarr == 0:
            min_operations += 1
        
        # If the sum of the current subarray is negative, increment the minimum number of operations
        elif sum_subarr < 0:
            min_operations += abs(sum_subarr)
    
    # Return the minimum number of operations
    return min_operations

