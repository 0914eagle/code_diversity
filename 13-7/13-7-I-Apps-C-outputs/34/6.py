
def arcaea_partners(n, k, partners):
    # Sort the partners in descending order of their Frag value
    partners = sorted(partners, key=lambda x: x[0], reverse=True)
    
    # Initialize the maximum diversity as 0
    max_diversity = 0
    
    # Iterate over the partners
    for i in range(n):
        # Check if the partner can be awakened
        if partners[i][3] != 0:
            # Increment the maximum diversity
            max_diversity += 1
            
            # Update the Frag and Step values of the partner
            partners[i] = (partners[i][3], partners[i][4])
            
            # Check if the maximum diversity has reached the limit
            if max_diversity == k:
                break
    
    # Return the maximum diversity
    return max_diversity

