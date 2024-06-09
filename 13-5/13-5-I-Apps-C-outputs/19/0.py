
def max_unique_identification(n, m, a):
    # Initialize a list to store the number of burgers ordered on each day
    burgers = [0] * m

    # Loop through the days
    for i in range(m):
        # If the number of burgers ordered is greater than the number of salads,
        # then the number of burgers ordered is the number of unique identifications
        if a[i] > (n - a[i]):
            burgers[i] = a[i]
        # Otherwise, the number of salads ordered is the number of unique identifications
        else:
            burgers[i] = n - a[i]

    # Return the maximum number of unique identifications
    return max(burgers)

