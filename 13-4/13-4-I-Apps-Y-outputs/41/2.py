
def perket(ingredients):
    # Sort the ingredients by their sourness in descending order
    ingredients.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the minimum difference and the chosen ingredients
    min_diff = 1000000000
    chosen_ingredients = []
    
    # Iterate over all possible combinations of ingredients
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
    
    # Return the minimum difference and the chosen ingredients
    return (min_diff, chosen_ingredients)

