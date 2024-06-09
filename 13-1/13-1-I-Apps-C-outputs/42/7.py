
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

    # Calculate the number of different dinner experiences
    num_dinner_experiences = 1
    for dish in compatible_dishes:
        num_dinner_experiences *= b[dish]

    # Check if the number of dinner experiences is at most 10^18
    if num_dinner_experiences <= 10**18:
        return num_dinner_experiences
    else:
        return "too many"

def f2(r, s, m, d, n):
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

    # Calculate the number of different dinner experiences
    num_dinner_experiences = 1
    for dish in compatible_dishes:
        num_dinner_experiences *= b[dish]

    # Check if the number of dinner experiences is at most 10^18
    if num_dinner_experiences <= 10**18:
        return num_dinner_experiences
    else:
        return "too many"

if __name__ == '__main__':
    r, s, m, d, n = map(int, input().split())
    b = list(map(int, input().split()))
    for i in range(s+m+d):
        k = int(input())
        ingredients = set(map(int, input().split()))
        for j in range(k):
            ingredient = int(input())
            ingredients.add(ingredient)
        compatible_dishes.add(ingredients)
    for i in range(n):
        dish1, dish2 = map(int, input().split())
        compatible_dishes.discard(dish1)
        compatible_dishes.discard(dish2)
    num_dinner_experiences = 1
    for dish in compatible_dishes:
        num_dinner_experiences *= b[dish]
    if num_dinner_experiences <= 10**18:
        print(num_dinner_experiences)
    else:
        print("too many")

