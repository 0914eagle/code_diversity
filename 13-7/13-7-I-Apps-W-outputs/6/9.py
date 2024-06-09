
def solve(n):
    # Initialize the number of bacteria to 1 and the current mass to 1
    num_bacteria, current_mass = 1, 1
    
    # Initialize the number of nights to 0
    nights = 0
    
    # Loop until the total mass is greater than or equal to the target mass
    while current_mass < n:
        # Increment the number of bacteria by the number that will split
        num_bacteria += num_bacteria
        
        # Increment the current mass by the total mass of the bacteria
        current_mass += num_bacteria
        
        # Increment the number of nights
        nights += 1
    
    # If the current mass is equal to the target mass, return the number of nights and the number of bacteria that will split on each night
    if current_mass == n:
        return nights, [num_bacteria // 2] * nights
    
    # Otherwise, return -1
    return -1

