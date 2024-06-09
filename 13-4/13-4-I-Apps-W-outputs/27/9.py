
def get_maximum_types(n, m, a, k):
    # Sort the list of already owned toys in ascending order
    a.sort()
    # Initialize variables to keep track of the number of types and cost
    num_types = 0
    cost = 0
    # Iterate through the list of toys and add them to the collection if the cost is less than or equal to m
    for i in range(n):
        if cost + a[i] <= m:
            cost += a[i]
            num_types += 1
        if cost == m:
            break
    # Return the number of types and the list of toys to buy
    return num_types, a[:num_types]

