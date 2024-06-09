
def solve(n, a):
    # Sort the array in ascending order
    a.sort()
    
    # Initialize the minimum number of problems to solve as 0
    min_problems = 0
    
    # Loop through the array and find the maximum difference between two adjacent elements
    for i in range(n-1):
        max_diff = max(max_diff, a[i+1] - a[i])
    
    # Return the minimum number of problems to solve as the maximum difference plus 1
    return max_diff + 1

