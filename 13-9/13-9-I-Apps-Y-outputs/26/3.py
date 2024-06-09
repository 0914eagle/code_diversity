
def solve(n, a):
    # Sort the skills in ascending order
    a.sort()
    # Initialize the total number of problems to 0
    total_problems = 0
    # Loop through the skills and find the minimum number of problems needed to form each team
    for i in range(0, n, 2):
        # If the two skills are not equal, add the difference to the total number of problems
        if a[i] != a[i+1]:
            total_problems += abs(a[i] - a[i+1])
    return total_problems

