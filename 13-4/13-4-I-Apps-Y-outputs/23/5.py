
def get_max_groups(n):
    # Initialize a list to store the number of groups for each number of students
    num_groups = [0] * (n + 1)
    # Initialize the maximum number of groups to 0
    max_groups = 0
    # Loop through each number of students
    for i in range(2, n + 1):
        # Calculate the number of groups for the current number of students
        num_groups[i] = n // i
        # If the number of groups is greater than the maximum, update the maximum
        if num_groups[i] > max_groups:
            max_groups = num_groups[i]
    # Return the maximum number of groups
    return max_groups

