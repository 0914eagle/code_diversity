
def get_toys(n, m, a):
    # Sort the list of toys in ascending order
    a.sort()
    # Initialize variables to keep track of the number of toys and cost
    k = 0
    cost = 0
    # Iterate through the list of toys
    for i in range(n):
        # If the current toy is not already owned and the cost is less than or equal to the budget, add it to the list of toys to buy
        if a[i] not in a[:i] and cost + a[i] <= m:
            k += 1
            cost += a[i]
    # Return the number of toys to buy and the list of toys to buy
    return k, cost

