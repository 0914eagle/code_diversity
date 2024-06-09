
def solve(n, m):
    # Initialize the array with all elements as 0
    arr = [0] * n
    
    # Initialize the sum of the array as 0
    sum = 0
    
    # Loop through the array and assign values to it
    for i in range(n):
        # Calculate the value of the current element
        val = (m - sum) // (n - i)
        
        # Update the sum of the array
        sum += val
        
        # Assign the value to the current element
        arr[i] = val
    
    # Return the maximum possible value of the sum of absolute differences between adjacent elements
    return max([abs(arr[i] - arr[i+1]) for i in range(n-1)])

