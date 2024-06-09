
def solve(n, pairs):
    # Initialize a dictionary to store the food types for each pair
    food_types = {}
    
    # Iterate over the pairs and assign food types
    for pair in pairs:
        # If the boy in the pair has not been assigned a food type, assign Kooft
        if pair[0] not in food_types:
            food_types[pair[0]] = 1
        # If the girl in the pair has not been assigned a food type, assign Zahre-mar
        if pair[1] not in food_types:
            food_types[pair[1]] = 2
        # If both the boy and girl in the pair have been assigned food types, check if they are the same
        if pair[0] in food_types and pair[1] in food_types and food_types[pair[0]] == food_types[pair[1]]:
            return -1
    
    # If all pairs have been assigned food types, return the dictionary of food types
    return food_types

