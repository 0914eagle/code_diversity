
def get_max_groups(n):
    # Initialize variables
    count = 0
    groups = 0

    # Loop through each possible group size
    for i in range(3, n + 1):
        # Calculate the number of groups for this group size
        count += n // i
        # If the number of groups is greater than the maximum, update the maximum
        if count > groups:
            groups = count

    # Return the maximum number of groups
    return groups

