
def find_min_days(total_mass):
    # Initialize variables
    days = 0
    bacteria = 1
    mass = 1
    
    # Loop until the total mass is reached
    while mass < total_mass:
        # Increment the number of days
        days += 1
        
        # Split the bacteria
        bacteria *= 2
        
        # Increment the mass of each bacterium
        mass += bacteria
    
    # Return the minimum number of days needed
    return days

def find_split_pattern(total_mass):
    # Initialize variables
    days = 0
    bacteria = 1
    mass = 1
    
    # Loop until the total mass is reached
    while mass < total_mass:
        # Increment the number of days
        days += 1
        
        # Split the bacteria
        bacteria *= 2
        
        # Increment the mass of each bacterium
        mass += bacteria
    
    # Return the split pattern
    return [int(bacteria / 2)] * days

if __name__ == '__main__':
    total_mass = int(input())
    print(find_min_days(total_mass))
    print(*find_split_pattern(total_mass), sep=' ')

