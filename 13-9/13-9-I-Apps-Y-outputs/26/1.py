
def solve(n, a):
    # Sort the array in ascending order
    a.sort()
    
    # Initialize the minimum number of problems to solve as 0
    min_problems = 0
    
    # Iterate through the array and find the minimum number of problems to solve for each pair of students
    for i in range(n//2):
        min_problems += a[i] - a[n//2+i]
    
    return min_problems

