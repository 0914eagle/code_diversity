
def solve(n):
    # Initialize the number of bacteria to 1 and their mass to 1
    num_bacteria = 1
    mass = 1
    
    # Initialize the number of nights to 0
    nights = 0
    
    # Loop until the total mass of the bacteria is equal to n
    while mass != n:
        # Increment the number of nights
        nights += 1
        
        # Double the number of bacteria
        num_bacteria *= 2
        
        # Increment the mass of each bacterium by 1
        mass += num_bacteria
    
    # Return the number of nights and the number of bacteria that should split on each night
    return nights, [int(num_bacteria / 2)] * nights

