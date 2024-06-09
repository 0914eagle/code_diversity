
def solve(n, a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the total number of problems to 0
    total_problems = 0
    # Loop through the array and find the minimum number of problems needed to form each team
    for i in range(0, n, 2):
        # Calculate the difference between the two students in the team
        diff = abs(a[i] - a[i+1])
        # Add the difference to the total number of problems
        total_problems += diff
    # Return the total number of problems
    return total_problems

