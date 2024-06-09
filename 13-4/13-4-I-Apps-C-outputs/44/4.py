
def solve(n, pairs):
    # Initialize a dictionary to store the food types for each pair
    food_types = {}
    
    # Iterate over the pairs and assign food types
    for pair in pairs:
        # If the boy has not been assigned a food type, assign Kooft
        if pair[0] not in food_types:
            food_types[pair[0]] = 1
        # If the girl has not been assigned a food type, assign Zahre-mar
        if pair[1] not in food_types:
            food_types[pair[1]] = 2
        # If both the boy and girl have been assigned food types, check if they are the same
        elif food_types[pair[0]] == food_types[pair[1]]:
            # If they are the same, return -1 as there is no solution
            return -1
    
    # If we reach this point, it means that all pairs have been assigned food types
    # Return the food types for each pair
    return [food_types[pair[0]] for pair in pairs]

