
def max_frogs_can_escape(n, d, frogs):
    # Sort the frogs by their leap capacity in descending order
    frogs.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the maximum number of frogs that can escape as 0
    max_escaped = 0
    
    # Loop through the frogs and try to form piles
    for i in range(n):
        # Check if the current frog can escape the pit
        if frogs[i][0] > d:
            # If the current frog can escape, add it to the maximum number of escaped frogs
            max_escaped += 1
        else:
            # If the current frog cannot escape, try to form a pile with the next frogs
            for j in range(i+1, n):
                # Check if the current frog and the next frog can form a pile
                if frogs[i][1] + frogs[j][1] <= frogs[i][0]:
                    # If they can form a pile, add the next frog to the current frog and break
                    frogs[i][1] += frogs[j][1]
                    break
    
    return max_escaped

