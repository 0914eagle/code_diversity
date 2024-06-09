
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
    for i in range(r):
        num_dinner_experiences *= len(compatible_dishes)

    # Check if the number of dinner experiences is at most 10^18
    if num_dinner_experiences <= 10**18:
        return num_dinner_experiences
    else:
        return "too many"

def f2(r, s, m, d, n):
    # Initialize a dictionary to store the compatible dishes for each ingredient
    compatible_dishes = {i: set() for i in range(1, r+1)}

    # Iterate over the dishes and add them to the compatible dishes dictionary
    for i in range(s):
        compatible_dishes[i].add(i)
    for i in range(s, s+m):
        compatible_dishes[i].add(i)
    for i in range(s+m, s+m+d):
        compatible_dishes[i].add(i)

    # Iterate over the incompatible dishes and remove them from the compatible dishes dictionary
    for i in range(n):
        dish1, dish2 = map(int, input().split())
        compatible_dishes[dish1].discard(dish2)
        compatible_dishes[dish2].discard(dish1)

    # Calculate the number of different dinner experiences
    num_dinner_experiences = 1
    for i in range(r):
        num_dinner_experiences *= len(compatible_dishes[i])

    # Check if the number of dinner experiences is at most 10^18
    if num_dinner_experiences <= 10**18:
        return num_dinner_experiences
    else:
        return "too many"

if __name__ == '__main__':
    r, s, m, d, n = map(int, input().split())
    print(f1(r, s, m, d, n))
    print(f2(r, s, m, d, n))

