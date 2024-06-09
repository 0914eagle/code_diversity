
def solve(n, a):
    # Sort the array of skills in non-decreasing order
    a.sort()
    # Initialize the total number of problems to 0
    total_problems = 0
    # Loop through the array of skills
    for i in range(n):
        # If the current skill is equal to the previous skill, then no problems need to be solved
        if i > 0 and a[i] == a[i-1]:
            continue
        # Otherwise, calculate the number of problems needed to solve to equal the current skill
        problems = a[i] - a[i-1]
        # Add the number of problems to the total
        total_problems += problems
    # Return the total number of problems
    return total_problems

