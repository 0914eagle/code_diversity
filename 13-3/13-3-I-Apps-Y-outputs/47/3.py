
def get_maximum_sum_of_absolute_differences(n, m):
    # Initialize the array with all elements as 0
    arr = [0] * n
    
    # Base case: if the sum is 0, return 0
    if m == 0:
        return 0
    
    # Initialize the maximum sum of absolute differences
    max_sum = 0
    
    # Iterate over the array
    for i in range(n):
        # Calculate the sum of the elements in the array
        current_sum = sum(arr)
        
        # If the current sum is equal to the target sum, return the maximum sum of absolute differences
        if current_sum == m:
            return max_sum
        
        # If the current sum is greater than the target sum, move to the next element
        elif current_sum > m:
            continue
        
        # Calculate the absolute difference between the current element and the target sum
        abs_diff = abs(current_sum - m)
        
        # If the absolute difference is greater than the maximum sum of absolute differences, update the maximum sum of absolute differences
        if abs_diff > max_sum:
            max_sum = abs_diff
        
        # Add the current element to the array
        arr[i] += 1
    
    # Return the maximum sum of absolute differences
    return max_sum

