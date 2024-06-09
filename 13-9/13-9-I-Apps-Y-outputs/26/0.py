
def solve(n, a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the minimum number of problems to solve as 0
    min_problems = 0
    # Loop through the array and find the pairs of students with equal skills
    for i in range(n//2):
        # If the current student and the next student have equal skills, increment the minimum number of problems to solve
        if a[i] == a[i+1]:
            min_problems += 1
        # If the current student and the next student have unequal skills, break the loop
        else:
            break
    return min_problems

