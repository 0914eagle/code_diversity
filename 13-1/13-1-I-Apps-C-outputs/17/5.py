
def solve(n, pairs):
    # Initialize a dictionary to store the food types for each pair
    food_types = {}
    
    # Iterate over the pairs and assign food types
    for i, pair in enumerate(pairs):
        # If the boy and girl are sitting on consecutive chairs, they cannot have the same food type
        if pair[0] == pair[1] + 1 or pair[0] == n + 1:
            food_types[i] = (1, 2)
        # If the boy and girl are not sitting on consecutive chairs, they can have the same food type
        else:
            food_types[i] = (1, 1)
    
    # Check if the conditions are met
    for i in range(n):
        # If the boy and girl have the same food type, return -1
        if food_types[i][0] == food_types[i][1]:
            return -1
        # If any three guests sitting on consecutive chairs have the same food type, return -1
        if food_types[i][0] == food_types[(i+1)%n][0] and food_types[i][0] == food_types[(i+2)%n][0]:
            return -1
    
    # If the conditions are met, return the food types for each pair
    return [food_types[i] for i in range(n)]

