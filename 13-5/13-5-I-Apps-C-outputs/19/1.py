
def solve(n, m, a):
    # Initialize a list to store the number of burgers ordered on each day
    burgers = [0] * m

    # Loop through each day and update the number of burgers ordered
    for i in range(m):
        burgers[i] = a[i]

    # Initialize a set to store the names of the colleagues who have been identified
    identified = set()

    # Loop through each day and identify the colleagues who have been identified
    for i in range(m):
        # If the number of burgers ordered is greater than 0, identify the colleague who ordered a burger
        if burgers[i] > 0:
            identified.add(i)

    # Return the maximum number of colleagues who can be uniquely identified
    return len(identified)

