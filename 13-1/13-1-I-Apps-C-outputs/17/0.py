
def solve(n, pairs):
    # Initialize a dictionary to store the food types for each pair
    food_types = {}
    
    # Iterate over the pairs and assign food types
    for i, pair in enumerate(pairs):
        # If the boy has Kooft, assign Zahre-mar to the girl
        if pair[0] % 2 == 0:
            food_types[i] = (1, 2)
        # If the boy has Zahre-mar, assign Kooft to the girl
        else:
            food_types[i] = (2, 1)
    
    # Check if the conditions are met
    for i in range(n):
        # If the boy and girl have the same food type, return -1
        if food_types[i][0] == food_types[i][1]:
            return -1
        # If the boy and girl are sitting on consecutive chairs, return -1
        if (i + 1) % n == 0 and food_types[i][0] == food_types[(i + 1) % n][1]:
            return -1
    
    # If all conditions are met, return the food types
    return [food_types[i] for i in range(n)]

