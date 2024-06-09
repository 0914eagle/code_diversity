
def solve(n, a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the total number of problems to 0
    total_problems = 0
    # Loop through the array and find the pairs of students with equal skills
    for i in range(0, n-1, 2):
        # If the skills of the current student and the next student are equal, then they can form a team
        if a[i] == a[i+1]:
            # Increment the total number of problems by 1 for each pair of students with equal skills
            total_problems += 1
    # Return the total number of problems
    return total_problems

