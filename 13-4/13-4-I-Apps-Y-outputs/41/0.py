
def get_perket_ingredients(ingredients):
    # Sort the ingredients by their sourness in ascending order
    ingredients = sorted(ingredients, key=lambda x: x[0])
    
    # Initialize the minimum difference and the chosen ingredients
    min_diff = float('inf')
    chosen_ingredients = []
    
    # Iterate through all possible combinations of ingredients
    for i in range(len(ingredients)):
        for j in range(i+1, len(ingredients)):
            # Calculate the total sourness and bitterness of the current combination
            total_sourness = ingredients[i][0] * ingredients[j][0]
            total_bitterness = ingredients[i][1] + ingredients[j][1]
            
            # Calculate the absolute difference between sourness and bitterness
            diff = abs(total_sourness - total_bitterness)
            
            # If the current difference is smaller than the minimum difference, update the minimum difference and the chosen ingredients
            if diff < min_diff:
                min_diff = diff
                chosen_ingredients = [ingredients[i], ingredients[j]]
    
    return chosen_ingredients

