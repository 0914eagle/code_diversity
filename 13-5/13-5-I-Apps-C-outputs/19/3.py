
def solve(n, m, a):
    # Initialize a list to store the number of burgers ordered on each day
    burgers = [0] * m

    # Initialize a set to store the names of the colleagues who have been identified
    identified = set()

    # Loop through each day
    for i in range(m):
        # If the number of burgers ordered is greater than the number of identified colleagues
        if a[i] > len(identified):
            # Identify the next colleague who has not been identified
            identified.add(i % n)

    # Return the maximum number of identified colleagues
    return len(identified)

