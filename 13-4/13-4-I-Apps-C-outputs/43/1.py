
import itertools

def solve(r, s, m, d, n, brands, dishes):
    # Initialize a set to store the different dinner experiences
    dinner_experiences = set()

    # Iterate over each starter, main, and dessert dish
    for dish in dishes:
        # Get the ingredients of the current dish
        ingredients = dish[1:]

        # Get the brands of the ingredients
        brand_list = [brands[i-1] for i in ingredients]

        # Get the number of different brands
        num_brands = len(set(brand_list))

        # If the number of brands is greater than 1, add the current dish to the dinner experiences
        if num_brands > 1:
            dinner_experiences.add(tuple(ingredients))

    # If the number of dinner experiences is at most 10^18, return the number of dinner experiences
    if len(dinner_experiences) <= 10**18:
        return len(dinner_experiences)
    else:
        return "too many"

# Test the function with the sample inputs
r = 6
s = 1
m = 1
d = 1
n = 0
brands = [2, 3, 1, 5, 3, 2]
dishes = [(2, 1, 2), (3, 3, 4, 5), (1, 6)]
print(solve(r, s, m, d, n, brands, dishes))

r = 3
s = 2
m = 2
d = 1
n = 1
brands = [3, 2, 2]
dishes = [(1, 1), (1, 2), (1, 2), (1, 3), (1, 1), (2, 3)]
print(solve(r, s, m, d, n, brands, dishes))

r = 3
s = 1
m = 1
d = 1
n = 1
brands = [5, 5, 5]
dishes = [(3, 1, 2, 3), (3, 1, 2, 3), (3, 1, 2, 3), (2, 1), (1, 1)]
print(solve(r, s, m, d, n, brands, dishes))

