
def solve(n, a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the minimum number of problems to solve as 0
    min_problems = 0
    # Loop through the array and find the median
    for i in range(n//2):
        # Find the difference between the current element and the median
        diff = a[i] - a[n//2]
        # Add the difference to the minimum number of problems to solve
        min_problems += diff
    return min_problems

