
def assign_integers(n, m):
    # Initialize a list to store the integers
    integers = list(range(1, n + 1))
    # Initialize a list to store the assignments
    assignments = []
    # Loop through each playing field
    for i in range(m):
        # Choose two distinct integers for the playing field
        a, b = choose_integers(integers)
        # Add the integers to the assignments
        assignments.append((a, b))
        # Remove the integers from the list of integers
        integers.remove(a)
        integers.remove(b)
    return assignments

def choose_integers(integers):
    # Choose the first integer at random
    a = integers[random.randint(0, len(integers) - 1)]
    # Choose the second integer at random, ensuring it is different from the first integer
    b = integers[random.randint(0, len(integers) - 1)]
    while b == a:
        b = integers[random.randint(0, len(integers) - 1)]
    return a, b

if __name__ == '__main__':
    n, m = map(int, input().split())
    assignments = assign_integers(n, m)
    for assignment in assignments:
        print(*assignment)

