
def get_maximum_types(n, m, a, k):
    # Sort the list of already owned toys in ascending order
    a.sort()
    # Initialize variables to keep track of the current cost and number of types
    cost = 0
    types = set()
    # Iterate through the list of toys and add them to the gift if they are not already owned and the cost does not exceed the budget
    for i in range(n):
        if a[i] not in types and cost + i <= m:
            types.add(a[i])
            cost += i
    # Return the number of types and the list of types as a set
    return len(types), types

