
import sys

def get_min_diff(ingredients):
    # Sort the ingredients by sourness in ascending order
    ingredients.sort(key=lambda x: x[0])
    # Initialize the minimum difference and the chosen ingredients
    min_diff = sys.maxsize
    chosen_ingredients = []
    # Iterate over the ingredients
    for ingredient in ingredients:
        # If the ingredient is not already chosen, add it to the chosen ingredients
        if ingredient not in chosen_ingredients:
            chosen_ingredients.append(ingredient)
            # Calculate the total sourness and bitterness of the chosen ingredients
            total_sourness = sum([ingredient[0] for ingredient in chosen_ingredients])
            total_bitterness = sum([ingredient[1] for ingredient in chosen_ingredients])
            # Calculate the difference between the total sourness and bitterness
            diff = abs(total_sourness - total_bitterness)
            # If the difference is smaller than the current minimum, update the minimum difference and the chosen ingredients
            if diff < min_diff:
                min_diff = diff
                chosen_ingredients = chosen_ingredients.copy()
    return min_diff

n = int(input())
ingredients = []
for i in range(n):
    s, b = map(int, input().split())
    ingredients.append((s, b))

print(get_min_diff(ingredients))

