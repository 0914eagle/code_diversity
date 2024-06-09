
def solve(n):
    # Initialize variables
    bacteria = 1
    mass = 1
    days = 0
    nights = 0
    
    # Loop until the total mass is equal to n
    while mass != n:
        # Increment the day count
        days += 1
        
        # Check if the bacteria should split
        if bacteria >= 2:
            # Split the bacteria
            bacteria *= 2
            # Increment the night count
            nights += 1
        
        # Increment the mass
        mass += bacteria
    
    # Return the results
    return days, nights

