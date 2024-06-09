
def solve(n, a):
    # Initialize the number of bribed citizens to 0
    bribed = 0
    # Sort the list of votes in descending order
    a.sort(reverse=True)
    # Loop through the list of votes
    for i in range(n):
        # If the current vote is 0, break the loop
        if a[i] == 0:
            break
        # Otherwise, bribe one citizen and decrease the current vote by 1
        bribed += 1
        a[i] -= 1
    # Return the number of bribed citizens
    return bribed

