
def max_unique_identification(n, m, a):
    # Initialize a list to store the number of burgers ordered on each day
    burgers = [0] * m

    # Set the number of burgers ordered on the first day
    burgers[0] = a[0]

    # Initialize a variable to store the maximum number of unique identifications
    max_unique = 0

    # Iterate over the remaining days
    for i in range(1, m):
        # Set the number of burgers ordered on the current day
        burgers[i] = a[i]

        # Iterate over the previous days
        for j in range(i):
            # If the number of burgers ordered on the current day is equal to the number of burgers ordered on the previous day
            if burgers[i] == burgers[j]:
                # Increment the maximum number of unique identifications
                max_unique += 1

    # Return the maximum number of unique identifications
    return max_unique

