
def max_frogs_can_escape(n, d, frogs):
    # Sort the frogs in descending order of their leap capacity
    frogs.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the maximum number of frogs that can escape as 0
    max_escaping_frogs = 0
    
    # Iterate through the frogs and try to form piles
    for i in range(n):
        # Check if the current frog can escape the pit
        if frogs[i][0] > d:
            # If the current frog can escape the pit, add it to the maximum number of escaping frogs
            max_escaping_frogs += 1
        else:
            # If the current frog cannot escape the pit, try to form a pile with other frogs
            for j in range(i+1, n):
                # Check if the current frog and the next frog can form a pile
                if frogs[i][1] + frogs[j][1] <= frogs[i][0]:
                    # If the current frog and the next frog can form a pile, add them to the maximum number of escaping frogs
                    max_escaping_frogs += 2
                    break
    
    return max_escaping_frogs

