
def solve(n, pairs):
    # Initialize a dictionary to store the food types for each pair
    food_types = {}
    
    # Iterate over the pairs and assign food types
    for pair in pairs:
        # If the boy and girl are sitting on consecutive chairs, they cannot have the same food type
        if pair[0] == pair[1] - 1 or pair[0] == pair[1] + 1:
            return -1
        
        # If the boy and girl have already been assigned food types, they cannot have the same type
        if pair[0] in food_types and food_types[pair[0]] == pair[1]:
            return -1
        if pair[1] in food_types and food_types[pair[1]] == pair[0]:
            return -1
        
        # Assign food types to the pair
        food_types[pair[0]] = 1 if pair[0] % 2 == 0 else 2
        food_types[pair[1]] = 2 if pair[1] % 2 == 0 else 1
    
    # Return the food types for each pair
    return [food_types[pair[0]], food_types[pair[1]] for pair in pairs]

