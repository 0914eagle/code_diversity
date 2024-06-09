
def f1(r, s, m, d, n):
    # Initialize a set to store the compatible dishes
    compatible_dishes = set()

    # Iterate over the dishes and add them to the compatible dishes set
    for i in range(s):
        compatible_dishes.add(i)
    for i in range(s, s+m):
        compatible_dishes.add(i)
    for i in range(s+m, s+m+d):
        compatible_dishes.add(i)

    # Iterate over the incompatible dishes and remove them from the compatible dishes set
    for i in range(n):
        dish1, dish2 = map(int, input().split())
        compatible_dishes.discard(dish1)
        compatible_dishes.discard(dish2)

    # Return the number of compatible dishes
    return len(compatible_dishes)

def f2(r, s, m, d, n):
    # Initialize a dictionary to store the number of compatible dishes for each ingredient
    compatible_dishes = {}

    # Iterate over the ingredients and initialize the number of compatible dishes for each ingredient to 0
    for i in range(r):
        compatible_dishes[i] = 0

    # Iterate over the dishes and increment the number of compatible dishes for each ingredient in the dish
    for i in range(s):
        ingredients = map(int, input().split())
        for ingredient in ingredients:
            compatible_dishes[ingredient] += 1
    for i in range(s, s+m):
        ingredients = map(int, input().split())
        for ingredient in ingredients:
            compatible_dishes[ingredient] += 1
    for i in range(s+m, s+m+d):
        ingredients = map(int, input().split())
        for ingredient in ingredients:
            compatible_dishes[ingredient] += 1

    # Iterate over the incompatible dishes and decrement the number of compatible dishes for each ingredient in the dish
    for i in range(n):
        dish1, dish2 = map(int, input().split())
        ingredients1 = map(int, input().split())
        ingredients2 = map(int, input().split())
        for ingredient in ingredients1:
            compatible_dishes[ingredient] -= 1
        for ingredient in ingredients2:
            compatible_dishes[ingredient] -= 1

    # Return the number of compatible dishes for each ingredient
    return compatible_dishes

if __name__ == '__main__':
    r, s, m, d, n = map(int, input().split())
    print(f1(r, s, m, d, n))
    print(f2(r, s, m, d, n))

