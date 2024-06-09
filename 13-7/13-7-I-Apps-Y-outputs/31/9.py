
def solve(arr):
    # Calculate the sum of the array
    sum_arr = sum(arr)
    
    # Initialize a variable to store the minimum number of elements to insert
    min_elements = 0
    
    # Iterate over the array
    for i in range(len(arr)):
        # Calculate the sum of the current subarray
        sum_subarr = sum(arr[:i+1])
        
        # If the sum of the current subarray is equal to the sum of the original array,
        # it means that we have found a subarray with sum zero
        if sum_subarr == sum_arr:
            # Increment the minimum number of elements to insert
            min_elements += 1
    
    return min_elements

