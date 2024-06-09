
def solve(n, a):
    # Sort the ratings in descending order
    a.sort(reverse=True)
    
    # Initialize the optimal distribution as an array of zeros
    b = [0] * n
    
    # Loop through the ratings and assign them to the users
    for i in range(n):
        # Find the first user who has not received any rating yet
        for j in range(n):
            if b[j] == 0:
                # Assign the current rating to the user
                b[j] = a[i]
                break
    
    return b

