
def solve(n):
    # Initialize variables
    days = 0
    bacteria = 1
    total_mass = 1
    
    # Loop until the total mass is equal to n
    while total_mass != n:
        # Increment the number of days
        days += 1
        
        # Check if the bacteria can split
        if bacteria >= 2:
            # Split the bacteria
            bacteria *= 2
        
        # Increment the total mass
        total_mass += bacteria
    
    # Return the number of days and the number of bacteria that should split on each day
    return days, [1 for _ in range(days)]

