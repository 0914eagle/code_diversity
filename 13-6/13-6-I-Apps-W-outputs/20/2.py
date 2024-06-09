
def solve(T, n, a):
    # Initialize an empty list to store the required seals
    required_seals = []
    
    # Iterate over the doors
    for i in range(T):
        # Initialize a list to store the possible seals
        possible_seals = []
        
        # Iterate over the seals of the current door
        for j in range(n):
            # Calculate the energy of the current seal
            energy = a[j]
            
            # Check if the energy is nonzero and does not exceed 100 in absolute value
            if energy != 0 and abs(energy) <= 100:
                # Add the current seal to the possible seals list
                possible_seals.append(energy)
        
        # Initialize a list to store the required seals for the current door
        required_seals_current_door = []
        
        # Iterate over the possible seals
        for seal in possible_seals:
            # Calculate the product of the current seal and all the other seals
            product = 1
            for other_seal in possible_seals:
                if other_seal != seal:
                    product *= other_seal
            
            # Check if the product is equal to zero
            if product == 0:
                # Add the current seal to the required seals list
                required_seals_current_door.append(seal)
        
        # Add the required seals for the current door to the overall required seals list
        required_seals.append(required_seals_current_door)
    
    # Return the required seals list
    return required_seals

