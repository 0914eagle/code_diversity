
def get_max_unique_identifications(n, m, a_list):
    # Initialize a list to store the number of burgers ordered on each day
    burgers_ordered = [0] * (m + 1)

    # Iterate over the list of burgers ordered on each day
    for i in range(m):
        # Increment the number of burgers ordered on the current day
        burgers_ordered[i] += a_list[i]

        # If the current day is not the last day, increment the number of burgers ordered on the next day by the number of burgers ordered on the current day
        if i != m - 1:
            burgers_ordered[i + 1] += burgers_ordered[i]

    # Initialize a variable to store the maximum number of unique identifications
    max_unique_identifications = 0

    # Iterate over the list of burgers ordered on each day
    for i in range(m):
        # Calculate the number of unique identifications on the current day
        unique_identifications = n - burgers_ordered[i]

        # Update the maximum number of unique identifications if necessary
        max_unique_identifications = max(max_unique_identifications, unique_identifications)

    # Return the maximum number of unique identifications
    return max_unique_identifications

