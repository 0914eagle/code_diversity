
def solve(arr):
    # Calculate the sum of the array
    sum_arr = sum(arr)
    
    # Initialize a variable to store the minimum number of elements to insert
    min_elements = 0
    
    # Iterate through the array
    for i in range(len(arr)):
        # Calculate the sum of the current subarray
        sum_subarr = sum(arr[:i+1])
        
        # If the sum of the current subarray is equal to the sum of the original array,
        # it means that there is a subarray with sum 0, so we need to insert an element
        if sum_subarr == sum_arr:
            min_elements += 1
    
    return min_elements

