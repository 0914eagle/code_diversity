
def solve(n, k, arr):
    # Sort the array to identify the duplicates
    arr.sort()
    
    # Initialize the minimum number of balls to rewrite
    min_balls = 0
    
    # Iterate over the array
    for i in range(n-1):
        # Check if the current element is equal to the next element
        if arr[i] == arr[i+1]:
            # Increment the minimum number of balls to rewrite
            min_balls += 1
        # Check if the current element is not equal to the next element and the difference between the current element and the next element is greater than or equal to k
        elif arr[i] + k <= arr[i+1]:
            # Increment the minimum number of balls to rewrite
            min_balls += 1
    
    # Return the minimum number of balls to rewrite
    return min_balls

