
def max_unique_identification(n, m, a):
    # Initialize a list to store the number of burgers ordered on each day
    burgers = [0] * m

    # Loop through the number of days
    for i in range(m):
        # If the number of burgers ordered is greater than the number of colleagues, return 0
        if a[i] > n:
            return 0

        # If the number of burgers ordered is equal to the number of colleagues, return the number of colleagues
        if a[i] == n:
            return n

        # If the number of burgers ordered is less than the number of colleagues, update the list of burgers ordered
        else:
            burgers[i] = a[i]

    # Initialize a variable to store the maximum number of unique identifications
    max_identifications = 0

    # Loop through the number of days
    for i in range(m):
        # If the number of burgers ordered is greater than the number of colleagues, return 0
        if burgers[i] > n:
            return 0

        # If the number of burgers ordered is equal to the number of colleagues, return the number of colleagues
        if burgers[i] == n:
            return n

        # If the number of burgers ordered is less than the number of colleagues, update the maximum number of unique identifications
        else:
            max_identifications = max(max_identifications, burgers[i])

    # Return the maximum number of unique identifications
    return max_identifications

