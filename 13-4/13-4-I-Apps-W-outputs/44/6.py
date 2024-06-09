
def knight_moves(x, y):
    # Initialize a dictionary to store the number of ways to reach each square
    ways = {(0, 0): 1}

    # Loop through all possible positions of the knight
    for i in range(x + 1):
        for j in range(y + 1):
            # If the current position is not the origin and has not been visited yet, mark it as visited and update the number of ways to reach it
            if (i, j) != (0, 0) and (i, j) not in ways:
                ways[(i, j)] = ways[(i - 1, j + 2)] + ways[(i - 2, j + 1)]

    # Return the number of ways to reach the target position, modulo 10^9 + 7
    return ways[(x, y)] % 1000000007

def main():
    x, y = map(int, input().split())
    print(knight_moves(x, y))

if __name__ == '__main__':
    main()

