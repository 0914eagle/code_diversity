
def solve(n, arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Initialize a variable to store the number of ways
    ways = 0
    
    # Loop through the array and check if the current element is greater than or equal to the previous element
    for i in range(n-1):
        if arr[i] >= arr[i+1]:
            ways += 1
    
    return ways

