
def get_max_days(n, m, a):
    # Initialize variables
    days = 0
    types = set()
    packages = {}

    # Iterate over the food packages
    for i in range(m):
        # Check if the current package type is already in the list of types
        if a[i] not in types:
            # If not, add it to the list of types and create a new key in the packages dictionary
            types.add(a[i])
            packages[a[i]] = 1
        else:
            # If it is already in the list of types, increment the number of packages of that type
            packages[a[i]] += 1

    # Iterate over the participants
    for i in range(n):
        # Check if there are any packages of the current participant's type
        if packages[i % len(types) + 1]:
            # If there are, decrement the number of packages of that type and increment the number of days
            packages[i % len(types) + 1] -= 1
            days += 1
        else:
            # If there are no packages of the current participant's type, the expedition cannot last for more than the current day
            return days

    # Return the maximum number of days the expedition can last
    return days

