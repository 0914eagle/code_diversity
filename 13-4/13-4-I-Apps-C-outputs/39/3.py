
def solve(n, d, frogs):
    # Sort the frogs by their leap capacity in descending order
    frogs.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the maximum number of frogs that can escape as 0
    max_escaped = 0
    
    # Iterate through the frogs
    for i in range(n):
        # Get the current frog's leap capacity, weight, and height
        l, w, h = frogs[i]
        
        # Check if the current frog can escape the pit directly
        if l > d:
            # Increment the maximum number of frogs that can escape
            max_escaped += 1
        
        # Check if the current frog can be carried by other frogs
        else:
            # Initialize a variable to store the maximum number of frogs that can be carried
            max_carried = 0
            
            # Iterate through the remaining frogs
            for j in range(i+1, n):
                # Get the current frog's leap capacity, weight, and height
                l_next, w_next, h_next = frogs[j]
                
                # Check if the current frog can be carried by the next frog
                if w_next + w <= l:
                    # Increment the maximum number of frogs that can be carried
                    max_carried += 1
                
                # Check if the current frog can be carried by the next frog and the next frog's leap capacity is sufficient
                elif w_next + w <= l_next:
                    # Increment the maximum number of frogs that can be carried
                    max_carried += 1
                    break
                
                # Otherwise, break the loop
                else:
                    break
            
            # Increment the maximum number of frogs that can escape by the maximum number of frogs that can be carried
            max_escaped += max_carried + 1
    
    # Return the maximum number of frogs that can escape
    return max_escaped

