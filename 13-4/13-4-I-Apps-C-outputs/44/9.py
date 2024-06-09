
def solve(n, pairs):
    # Initialize the food types for each pair
    food_types = [[0, 0] for _ in range(n)]
    
    # Iterate over each pair
    for i in range(n):
        # Get the current pair
        pair = pairs[i]
        
        # If the boy has already been assigned a food type, skip this pair
        if food_types[i][0] != 0:
            continue
        
        # If the girl has already been assigned a food type, skip this pair
        if food_types[i][1] != 0:
            continue
        
        # If the boy and girl have the same type of food, skip this pair
        if pair[0] == pair[1]:
            continue
        
        # If the boy and girl have different types of food, assign them to the pair
        if pair[0] % 2 == 0 and pair[1] % 2 == 1:
            food_types[i] = [1, 2]
        else:
            food_types[i] = [2, 1]
    
    # Check if all pairs have been assigned a food type
    for pair in food_types:
        if pair[0] == 0 or pair[1] == 0:
            return [-1]
    
    # Return the food types for each pair
    return [food_types[i] for i in range(n)]

