
def solve(N):
    # Initialize a list to store the number of groups of three or more students
    groups = []

    # Loop through the range of numbers from 1 to N
    for i in range(1, N + 1):
        # Check if the current number is a factor of N
        if N % i == 0:
            # If it is, add it to the list of groups
            groups.append(i)

    # Return the length of the list of groups
    return len(groups)

