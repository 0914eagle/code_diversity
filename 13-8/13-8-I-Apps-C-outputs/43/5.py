
import sys

def solve(N, P, bad_pairs):
    # Initialize a set to store the used ingredients
    used_ingredients = set()
    # Initialize a list to store the drinks
    drinks = []
    # Iterate through the bad pairs of ingredients
    for a, b in bad_pairs:
        # If both ingredients are already used, skip this pair
        if a in used_ingredients and b in used_ingredients:
            continue
        # If either ingredient is already used, add the other ingredient to the used set
        elif a in used_ingredients:
            used_ingredients.add(b)
        elif b in used_ingredients:
            used_ingredients.add(a)
        # If neither ingredient is used, add both to the used set
        else:
            used_ingredients.update([a, b])
    # Iterate through the remaining ingredients
    for i in range(1, N + 1):
        # If the ingredient is not used, add it to the drink
        if i not in used_ingredients:
            drinks.append(i)
    # Return the number of drinks made
    return len(drinks)

if __name__ == '__main__':
    N, P = map(int, input().split())
    bad_pairs = []
    for _ in range(P):
        a, b = map(int, input().split())
        bad_pairs.append((a, b))
    print(solve(N, P, bad_pairs))

