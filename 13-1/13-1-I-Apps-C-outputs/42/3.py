
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

    # Check if the number of dinner experiences is less than 10^18
    if num_dinner_experiences <= 10**18:
        return num_dinner_experiences
    else:
        return "too many"

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    r, s, m, d, n = map(int, input().split())
    print(f1(r, s, m, d, n))

