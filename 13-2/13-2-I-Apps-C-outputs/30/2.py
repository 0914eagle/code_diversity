
import sys

def solve(N, P, bad_pairs):
    # Initialize a set to store the used ingredients
    used_ingredients = set()
    # Initialize a list to store the drinks
    drinks = []
    # Initialize a variable to store the number of nights
    nights = 0

    while len(drinks) < N:
        # Choose a new set of ingredients
        ingredients = set(range(1, N + 1)) - used_ingredients
        # Check if the new set of ingredients contains any bad pairs
        for a, b in bad_pairs:
            if a in ingredients and b in ingredients:
                break
        else:
            # If the new set of ingredients does not contain any bad pairs, add it to the list of drinks
            drinks.append(ingredients)
            # Add the used ingredients to the set of used ingredients
            used_ingredients |= ingredients
            # Increment the number of nights
            nights += 1

    return nights % (10**9 + 7)

if __name__ == '__main__':
    N, P = map(int, input().split())
    bad_pairs = []
    for _ in range(P):
        a, b = map(int, input().split())
        bad_pairs.append((a, b))
    print(solve(N, P, bad_pairs))

