
def solve(n, pairs):
    # Initialize a dictionary to store the food types for each pair
    food_types = {}
    
    # Iterate over the pairs and assign food types based on the following rules:
    # 1. Each pair has a different food type
    # 2. No boy has the same food type as his girlfriend
    for i, pair in enumerate(pairs):
        boy, girl = pair
        if i % 2 == 0:
            food_types[pair] = 1, 2
        else:
            food_types[pair] = 2, 1
    
    # Check if the food types satisfy the third rule:
    # Among any three guests sitting on consecutive chairs, there is at least two of them who have different types of food
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if food_types[(i, j)] != food_types[(j, k)] and food_types[(i, j)] != food_types[(k, i)]:
                    break
            else:
                return -1
    
    # If we reach this point, it means that the food types satisfy the rules
    return food_types

