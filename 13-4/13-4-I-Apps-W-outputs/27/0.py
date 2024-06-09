
def solve(n, m, a):
    # Sort the list of toys that Tanya already has
    a.sort()
    
    # Initialize variables to keep track of the number of different types of toys and the total cost
    k = 0
    cost = 0
    
    # Iterate through the list of toys that Tanya already has
    for i in range(n):
        # If the current toy is not already in Tanya's collection, add it to the list of toys to buy
        if a[i] not in a[:i]:
            k += 1
            cost += a[i]
        
        # If the total cost exceeds the maximum amount that Tanya's mom is willing to spend, break the loop
        if cost > m:
            break
    
    # Return the number of different types of toys and the list of toys to buy
    return k, a[:k]

