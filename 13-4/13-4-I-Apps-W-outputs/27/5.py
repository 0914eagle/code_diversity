
def get_maximum_types(n, m, a):
    # Sort the list of toys in ascending order
    a.sort()
    # Initialize variables to keep track of the number of types and cost
    types = 0
    cost = 0
    # Iterate through the list of toys
    for i in range(n):
        # If the current toy is not already in Tanya's collection
        if a[i] not in a[:i]:
            # Increment the number of types and add the cost of the current toy
            types += 1
            cost += a[i]
            # If the total cost exceeds the given limit, return the current number of types
            if cost > m:
                return types
    # If all toys have been considered and the total cost has not exceeded the limit, return the total number of types
    return types

