
def solve(n, pairs):
    # Initialize a dictionary to store the food types for each pair
    food_types = {}
    
    # Iterate over the pairs and assign food types
    for i, pair in enumerate(pairs):
        # If the boy and girl are sitting on consecutive chairs, they cannot have the same food type
        if pair[0] == pair[1] - 1 or pair[0] == pair[1] + 1:
            return -1
        
        # If the boy has already been assigned a food type, assign the opposite type to the girl
        if pair[0] in food_types:
            food_types[pair[1]] = 3 - food_types[pair[0]]
        # If the girl has already been assigned a food type, assign the same type to the boy
        elif pair[1] in food_types:
            food_types[pair[0]] = food_types[pair[1]]
        # If neither the boy nor the girl has been assigned a food type, assign Kooft to the boy and Zahre-mar to the girl
        else:
            food_types[pair[0]] = 1
            food_types[pair[1]] = 2
    
    # Return the food types for each pair
    return [food_types[pair[0]], food_types[pair[1]] for pair in pairs]

