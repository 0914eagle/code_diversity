
def get_number_of_bridges(a, b, c):
    # Initialize a 2D array to store the number of bridges between each pair of islands
    num_bridges = [[0] * (a + b + c) for _ in range(a + b + c)]

    # Fill in the number of bridges between islands of the same color
    for i in range(a):
        for j in range(i + 1, a):
            num_bridges[i][j] = 1
    for i in range(a, a + b):
        for j in range(i + 1, a + b):
            num_bridges[i][j] = 1
    for i in range(a + b, a + b + c):
        for j in range(i + 1, a + b + c):
            num_bridges[i][j] = 1

    # Fill in the number of bridges between islands of different colors
    for i in range(a):
        for j in range(a + b, a + b + c):
            num_bridges[i][j] = 1
    for i in range(a, a + b):
        for j in range(a + b, a + b + c):
            num_bridges[i][j] = 1

    # Fill in the number of bridges between islands of the same color, but with a minimum distance of 3
    for i in range(a):
        for j in range(i + 3, a):
            num_bridges[i][j] = 1
    for i in range(a, a + b):
        for j in range(i + 3, a + b):
            num_bridges[i][j] = 1
    for i in range(a + b, a + b + c):
        for j in range(i + 3, a + b + c):
            num_bridges[i][j] = 1

    # Calculate the total number of bridges
    total_bridges = 0
    for i in range(a + b + c):
        for j in range(i + 1, a + b + c):
            total_bridges += num_bridges[i][j]

    return total_bridges % 998244353

def main():
    a, b, c = map(int, input().split())
    print(get_number_of_bridges(a, b, c))

if __name__ == '__main__':
    main()

