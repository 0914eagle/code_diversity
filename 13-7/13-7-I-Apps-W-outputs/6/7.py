
def solve(n):
    # Initialize variables
    days = 0
    bacteria = 1
    splits = []
    
    # Loop until the total mass of the bacteria is equal to n
    while bacteria < n:
        # Check if the bacteria can split
        if bacteria >= 2:
            # Split the bacteria
            bacteria //= 2
            splits.append(1)
        # Increment the day
        days += 1
        
        # Increment the mass of the bacteria
        bacteria += 1
    
    # Check if the total mass of the bacteria is equal to n
    if bacteria == n:
        return [days, *splits]
    else:
        return [-1]

