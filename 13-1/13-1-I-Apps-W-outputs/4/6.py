
def get_max_days(n, m, a):
    # Initialize variables
    days = 0
    types = set()
    packages = {}

    # Iterate over the food packages
    for i in range(m):
        # Check if the current package type is already in the set of types
        if a[i] not in types:
            # If not, add it to the set and create a new key in the packages dictionary with value 1
            types.add(a[i])
            packages[a[i]] = 1
        else:
            # If it is already in the set, increment the value of the current package type in the packages dictionary
            packages[a[i]] += 1

    # Iterate over the participants
    for i in range(n):
        # Check if there is at least one package of each type
        if len(packages) == types:
            # If so, increment the number of days and remove the current package type from the set
            days += 1
            types.remove(a[i])
        else:
            # If not, break the loop and return 0
            return 0

    # Return the number of days
    return days

