
def get_min_night(n):
    # Initialize variables
    night = 0
    bacteria = 1
    total_mass = 1
    
    # Loop until the total mass is equal to n
    while total_mass < n:
        # Increment the night
        night += 1
        
        # Double the number of bacteria
        bacteria *= 2
        
        # Increment the total mass by the number of bacteria
        total_mass += bacteria
    
    # If the total mass is equal to n, return the minimum number of nights needed
    if total_mass == n:
        return night
    
    # If the total mass is not equal to n, return -1
    else:
        return -1

def get_bacteria_split(n):
    # Initialize variables
    night = 0
    bacteria = 1
    total_mass = 1
    split_bacteria = []
    
    # Loop until the total mass is equal to n
    while total_mass < n:
        # Increment the night
        night += 1
        
        # Double the number of bacteria
        bacteria *= 2
        
        # Increment the total mass by the number of bacteria
        total_mass += bacteria
        
        # Add the number of bacteria that split to the list of split bacteria
        split_bacteria.append(bacteria)
    
    # If the total mass is equal to n, return the minimum number of nights needed and the list of split bacteria
    if total_mass == n:
        return night, split_bacteria
    
    # If the total mass is not equal to n, return -1 and an empty list
    else:
        return -1, []

if __name__ == '__main__':
    # Test case 1
    n = 9
    night, split_bacteria = get_bacteria_split(n)
    print(night)
    print(" ".join(map(str, split_bacteria)))
    
    # Test case 2
    n = 11
    night, split_bacteria = get_bacteria_split(n)
    print(night)
    print(" ".join(map(str, split_bacteria)))
    
    # Test case 3
    n = 2
    night = get_min_night(n)
    print(night)

