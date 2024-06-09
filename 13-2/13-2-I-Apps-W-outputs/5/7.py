
def solve(n, a):
    # Sort the ratings in descending order
    a.sort(reverse=True)
    
    # Initialize the optimal distribution
    b = [0] * n
    
    # Loop through the users and assign them the highest possible rating
    for i in range(n):
        b[i] = a[i]
    
    # Return the optimal distribution
    return b

