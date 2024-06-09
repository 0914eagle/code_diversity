
import itertools

def solve(r, s, m, d, n, brands, dishes):
    # Initialize a set to store the different dinner experiences
    dinner_experiences = set()

    # Iterate over each dish and its ingredients
    for dish in dishes:
        # Get the ingredients for the current dish
        ingredients = dish[1:]

        # Iterate over each ingredient and its brands
        for ingredient, brand in enumerate(ingredients):
            # If the ingredient is not already in the dinner experience, add it
            if ingredient not in dinner_experiences:
                dinner_experiences.add(ingredient)

            # If the ingredient is already in the dinner experience, add the brand
            else:
                dinner_experiences.add((ingredient, brand))

    # Return the number of different dinner experiences
    return len(dinner_experiences)

# Main function
if __name__ == "__main__":
    # Read the input
    r, s, m, d, n = map(int, input().split())
    brands = list(map(int, input().split()))
    dishes = []
    for _ in range(s+m+d):
        dishes.append(list(map(int, input().split())))

    # Solve the problem
    result = solve(r, s, m, d, n, brands, dishes)

    # Print the result
    print(result)

