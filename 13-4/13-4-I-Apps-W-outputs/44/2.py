
def knight_moves(x, y):
    # Initialize a dictionary to store the number of ways to reach each square
    ways = {(0, 0): 1}
    
    # Loop through all possible positions of the knight
    for i in range(x + 1):
        for j in range(y + 1):
            # If the current position is not the starting position, check if it can be reached from the previous position
            if (i, j) != (0, 0):
                # If the current position is reachable from the previous position, add the number of ways to reach the previous position to the current position
                if (i - 2, j + 1) in ways or (i - 1, j + 2) in ways:
                    ways[(i, j)] = (ways.get((i - 2, j + 1), 0) + ways.get((i - 1, j + 2), 0)) % (10**9 + 7)
    
    # Return the number of ways to reach the target position
    return ways.get((x, y), 0)

def main():
    x, y = map(int, input().split())
    print(knight_moves(x, y))

if __name__ == '__main__':
    main()

