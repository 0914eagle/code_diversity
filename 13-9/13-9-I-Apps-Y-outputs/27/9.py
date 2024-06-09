
def solve(n, friends):
    # Initialize a dictionary to map each friend to their gift recipient
    gift_map = {}
    
    # Iterate through the input list of friends
    for i, friend in enumerate(friends):
        # If the friend doesn't know whom they want to give the gift to, set their gift recipient to the next friend in the list
        if friend == 0:
            gift_map[i] = (i + 1) % n
        # Otherwise, set their gift recipient to the specified friend
        else:
            gift_map[i] = friend
    
    # Initialize a list to store the final output
    output = []
    
    # Iterate through the gift map
    for i in range(n):
        # Add the gift recipient for the current friend to the output list
        output.append(gift_map[i])
    
    # Return the output list
    return output

