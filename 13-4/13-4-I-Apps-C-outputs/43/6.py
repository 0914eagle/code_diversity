
import itertools

def solve(r, s, m, d, n, b, dishes):
    # Initialize a set to store the different dinner experiences
    dinner_experiences = set()

    # Iterate over each dish and its ingredients
    for dish in dishes:
        # Get the ingredients for the current dish
        ingredients = dish[1:]

        # Initialize a set to store the different brands of ingredients
        ingredient_brands = set()

        # Iterate over each ingredient in the current dish
        for ingredient in ingredients:
            # Get the brand of the current ingredient
            brand = b[ingredient - 1]

            # Add the brand of the current ingredient to the set of ingredient brands
            ingredient_brands.add(brand)

        # Add the set of ingredient brands to the set of dinner experiences
        dinner_experiences.add(frozenset(ingredient_brands))

    # Get the number of different dinner experiences
    num_dinner_experiences = len(dinner_experiences)

    # Check if the number of different dinner experiences is at most 10^18
    if num_dinner_experiences <= 10**18:
        return num_dinner_experiences
    else:
        return "too many"

def main():
    # Read the input
    r, s, m, d, n = map(int, input().split())
    b = list(map(int, input().split()))
    dishes = []
    for _ in range(s + m + d):
        dishes.append(list(map(int, input().split())))
    incompatible_dishes = []
    for _ in range(n):
        incompatible_dishes.append(list(map(int, input().split())))

    # Solve the problem
    result = solve(r, s, m, d, n, b, dishes)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()

