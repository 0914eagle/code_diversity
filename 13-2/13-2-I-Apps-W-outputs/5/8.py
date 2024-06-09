
def solve(n, a):
    # Sort the ratings in descending order
    a.sort(reverse=True)
    
    # Initialize the optimal distribution
    b = [0] * n
    
    # Loop through the ratings and assign them to the users
    for i in range(n):
        # Find the user with the highest rating who has not yet received a rating
        for j in range(n):
            if b[j] == 0:
                b[j] = a[i]
                break
    
    return b

