
def get_perfect_perket(ingredients):
    # Sort the ingredients by their sourness in descending order
    ingredients = sorted(ingredients, key=lambda x: x[0], reverse=True)
    # Initialize the total sourness and bitterness to 0
    total_sourness, total_bitterness = 0, 0
    # Loop through the ingredients and calculate the total sourness and bitterness
    for ingredient in ingredients:
        total_sourness += ingredient[0]
        total_bitterness += ingredient[1]
    # Return the absolute difference between the total sourness and bitterness
    return abs(total_sourness - total_bitterness)

