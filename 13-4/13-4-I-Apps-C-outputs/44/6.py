
def solve(n, pairs):
    # Initialize the food types for each pair
    food_types = [[0, 0] for _ in range(n)]
    
    # Iterate over the pairs and assign food types
    for i in range(n):
        # If the boy and girl are sitting on consecutive chairs, they cannot have the same food type
        if abs(pairs[i][0] - pairs[i][1]) == 1:
            food_types[i][0] = 1
            food_types[i][1] = 2
        # If the boy and girl are not sitting on consecutive chairs, they can have the same food type
        else:
            food_types[i][0] = 1
            food_types[i][1] = 1
    
    # Check if the food types satisfy the conditions
    for i in range(n):
        # If the boy and girl have the same food type, it's not possible to satisfy the conditions
        if food_types[i][0] == food_types[i][1]:
            return [-1]
    
    return food_types

