
import sys

n = int(input())
ingredients = []

for i in range(n):
    s, b = map(int, input().split())
    ingredients.append((s, b))

# Sort the ingredients by their sourness in descending order
ingredients.sort(key=lambda x: x[0], reverse=True)

# Initialize the minimum difference and the chosen ingredients
min_diff = 1000000000
chosen_ingredients = []

# Iterate through all possible combinations of ingredients
for i in range(1, n+1):
    for combination in itertools.combinations(ingredients, i):
        # Calculate the total sourness and bitterness of the current combination
        total_sourness = 1
        total_bitterness = 0
        for ingredient in combination:
            total_sourness *= ingredient[0]
            total_bitterness += ingredient[1]
        
        # Calculate the difference between the total sourness and bitterness
        diff = abs(total_sourness - total_bitterness)
        
        # If the difference is smaller than the current minimum, update the minimum and the chosen ingredients
        if diff < min_diff:
            min_diff = diff
            chosen_ingredients = combination

print(min_diff)

