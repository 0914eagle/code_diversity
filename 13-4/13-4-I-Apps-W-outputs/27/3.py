
def solve(n, m, a):
    # Sort the list of toys that Tanya already has
    a.sort()
    
    # Initialize variables to keep track of the number of distinct toys and the total cost
    k = 0
    cost = 0
    
    # Iterate through the list of toys and add them to the collection if they are not already there and the total cost does not exceed m
    for i in range(n):
        if a[i] not in a[:i] and cost + a[i] <= m:
            k += 1
            cost += a[i]
    
    # Return the number of distinct toys and the list of toys to buy
    return [k, a[:k]]

