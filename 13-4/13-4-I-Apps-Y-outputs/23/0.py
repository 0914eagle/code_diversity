
def get_max_groups(n):
    # Initialize a list to store the number of groups of three or more students
    groups = []

    # Iterate from 3 to n, which are the possible sizes of groups
    for i in range(3, n + 1):
        # Calculate the number of groups of size i that can be formed
        num_groups = n // i

        # If the number of groups is greater than 0, add it to the list
        if num_groups > 0:
            groups.append(num_groups)

    # Return the maximum number of groups that can be formed
    return max(groups)

