
def solve(n, pairs):
    # Initialize a dictionary to store the food types for each pair
    food_types = {}
    
    # Iterate over the pairs and assign food types
    for i, pair in enumerate(pairs):
        # If the boy and girl are sitting on consecutive chairs, they cannot have the same food type
        if pair[0] == pair[1] + 1 or pair[0] == n + 1:
            food_types[i] = (1, 2)
        else:
            food_types[i] = (2, 1)
    
    # Check if the conditions are met
    for i in range(n):
        # If the boy and girl are sitting on consecutive chairs, they cannot have the same food type
        if pairs[i][0] == pairs[i][1] + 1 or pairs[i][0] == n + 1:
            if food_types[i][0] == food_types[i][1]:
                return -1
    
    # If all conditions are met, return the food types
    return [food_types[i] for i in range(n)]

