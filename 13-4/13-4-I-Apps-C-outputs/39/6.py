
def solve(n, d, frogs):
    # Sort the frogs in descending order of their leap capacity
    frogs.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the maximum number of frogs that can escape as 0
    max_escaped = 0
    
    # Loop through the frogs and try to form piles
    for i in range(n):
        # Check if the current frog has a leap capacity greater than the depth of the pit
        if frogs[i][0] > d:
            # If so, add it to the maximum number of escaped frogs
            max_escaped += 1
        else:
            # If not, try to form a pile with the current frog and the previous frogs
            for j in range(i):
                # Check if the current frog and the previous frog have a combined leap capacity greater than the depth of the pit
                if frogs[i][0] + frogs[j][0] > d:
                    # If so, add the current frog to the maximum number of escaped frogs
                    max_escaped += 1
                    # And break out of the loop
                    break
    
    # Return the maximum number of escaped frogs
    return max_escaped

