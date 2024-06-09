
def solve(n):
    # Initialize the number of bacteria to 1 and the current mass to 1
    num_bacteria = 1
    current_mass = 1
    
    # Initialize the number of nights to 0
    nights = 0
    
    # Loop until the total mass is equal to n
    while current_mass != n:
        # Increment the number of nights
        nights += 1
        
        # Calculate the number of bacteria that will split
        num_split = num_bacteria // 2
        
        # Update the number of bacteria and current mass
        num_bacteria += num_split
        current_mass += num_split
        
        # Increment the current mass of each bacteria by 1
        current_mass += num_bacteria
    
    # Return the number of nights and the number of bacteria that will split on each night
    return nights, [num_bacteria // 2] * nights

