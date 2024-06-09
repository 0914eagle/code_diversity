
def solve(n, m):
    # Initialize the array with all elements as 0
    arr = [0] * n
    
    # Initialize the sum of the array as 0
    sum = 0
    
    # Loop through the array and assign values to it
    for i in range(n):
        # Calculate the difference between the current sum and the target sum
        diff = m - sum
        
        # If the difference is 0, break the loop
        if diff == 0:
            break
        
        # Assign the maximum value possible for the current element
        arr[i] = diff
        
        # Update the sum of the array
        sum += diff
    
    # Return the sum of absolute differences between adjacent elements
    return sum(abs(arr[i] - arr[i+1]) for i in range(n-1))

