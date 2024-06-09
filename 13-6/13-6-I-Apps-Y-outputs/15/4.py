
def solve(n, m, *foods):
    # Initialize a set to store the common foods
    common_foods = set(range(1, m + 1))
    # Iterate over the input foods
    for food in foods:
        # Intersect the current food with the common foods set
        common_foods &= set(food)
    # Return the size of the common foods set
    return len(common_foods)

