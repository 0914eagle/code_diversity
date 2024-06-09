
def solve(n, pairs):
    # Initialize the food types for each pair
    food_types = [[0, 0] for _ in range(n)]
    
    # Loop through each pair and assign food types
    for i in range(n):
        # If the boy is sitting on an even-numbered chair, give him Kooft
        if pairs[i][0] % 2 == 0:
            food_types[i][0] = 1
        # If the boy is sitting on an odd-numbered chair, give him Zahre-mar
        else:
            food_types[i][0] = 2
        
        # If the girl is sitting on an even-numbered chair, give her Zahre-mar
        if pairs[i][1] % 2 == 0:
            food_types[i][1] = 2
        # If the girl is sitting on an odd-numbered chair, give her Kooft
        else:
            food_types[i][1] = 1
    
    # Check if the conditions are met
    for i in range(n):
        # If the boy and girl have the same food type, return -1
        if food_types[i][0] == food_types[i][1]:
            return -1
        # If any two guests sitting on consecutive chairs have the same food type, return -1
        if i < n-1 and food_types[i][0] == food_types[i+1][0]:
            return -1
        if i < n-1 and food_types[i][1] == food_types[i+1][1]:
            return -1
    
    # If all conditions are met, return the food types
    return food_types

