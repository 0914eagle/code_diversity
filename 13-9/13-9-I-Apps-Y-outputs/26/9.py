
def solve(n, a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the minimum number of problems to solve as 0
    min_problems = 0
    # Loop through the array and find the pair with the minimum difference
    for i in range(n//2):
        min_problems += a[i] - a[n-i-1]
    return min_problems

