
def solve(n):
    # Initialize variables
    total_mass = 1
    bacteria_count = 1
    nights = 0
    days = 1
    
    # Loop until the total mass is equal to the given value
    while total_mass != n:
        # Increase the night count
        nights += 1
        
        # Check if the bacteria should split
        if total_mass >= 2:
            # Split the bacteria
            bacteria_count *= 2
            total_mass = bacteria_count
        
        # Increase the day count
        days += 1
    
    # Return the minimum number of nights needed to reach the given total mass
    return nights

