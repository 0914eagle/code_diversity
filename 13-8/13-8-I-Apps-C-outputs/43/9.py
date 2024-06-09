
import sys

def solve(N, P, bad_pairs):
    # Initialize a set to store the used ingredients
    used_ingredients = set()
    # Initialize a set to store the used pairs of ingredients
    used_pairs = set()
    # Initialize a counter to keep track of the number of nights
    nights = 0
    
    while True:
        # Choose a random ingredient from the unused ingredients
        ingredient = random.randint(1, N)
        # If the ingredient has not been used before, use it
        if ingredient not in used_ingredients:
            used_ingredients.add(ingredient)
        # If all ingredients have been used, break the loop
        if len(used_ingredients) == N:
            break
    
    # For each bad pair of ingredients
    for a, b in bad_pairs:
        # If the pair has not been used before, use it
        if (a, b) not in used_pairs:
            used_pairs.add((a, b))
        # If all bad pairs have been used, break the loop
        if len(used_pairs) == P:
            break
    
    # Increment the number of nights
    nights += 1

# Return the number of nights modulo 10^9 + 7
return nights % (10**9 + 7)

