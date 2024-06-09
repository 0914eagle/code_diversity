
def solve(n, c, t):
    if c == t:
        return "Yes"
    
    # Initialize the charges of the stones
    charges = c
    
    # Iterate through the stones and synchronize them with their neighbors
    for i in range(1, n):
        # Calculate the new charge of the current stone
        new_charge = charges[i-1] + charges[i+1] - charges[i]
        
        # Update the charge of the current stone
        charges[i] = new_charge
    
    # Check if the charges of the stones match the required charges
    if charges == t:
        return "Yes"
    else:
        return "No"

