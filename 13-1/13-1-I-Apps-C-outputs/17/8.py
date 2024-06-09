
def solve(n, pairs):
    # Initialize a dictionary to store the food types for each pair
    food_types = {}
    
    # Iterate over the pairs and assign food types
    for pair in pairs:
        # If the boy has Kooft, assign Zahre-mar to the girl
        if pair[0] % 2 == 0:
            food_types[pair] = (1, 2)
        # If the boy has Zahre-mar, assign Kooft to the girl
        else:
            food_types[pair] = (2, 1)
    
    # Check if the conditions are met
    for i in range(n):
        # If the boy and girl have the same food type, return -1
        if food_types[pairs[i]][0] == food_types[pairs[(i+1)%n]][0]:
            return -1
        # If the boy and girl have the same food type, return -1
        if food_types[pairs[i]][1] == food_types[pairs[(i+1)%n]][1]:
            return -1
    
    # If all conditions are met, return the food types
    return [food_types[pair] for pair in pairs]

