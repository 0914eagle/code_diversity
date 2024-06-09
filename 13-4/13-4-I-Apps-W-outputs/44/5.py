
def knight_moves(x, y):
    # Initialize a dictionary to store the number of ways to reach each square
    ways = {(0, 0): 1}
    
    # Loop through all possible positions of the knight
    for i in range(x+1):
        for j in range(y+1):
            # If the current position is not the starting position and there is no way to reach it, skip it
            if (i, j) != (0, 0) and (i, j) not in ways:
                continue
            # If the current position is the destination, return the number of ways to reach it
            if (i, j) == (x, y):
                return ways[(x, y)]
            # Otherwise, update the number of ways to reach the neighboring positions
            for move in [(i+1, j+2), (i+2, j+1)]:
                if move in ways:
                    ways[move] = (ways[move] + ways[(i, j)]) % 1000000007
                else:
                    ways[move] = ways[(i, j)]
    
    # If the destination is not reachable, return 0
    return 0

def main():
    x, y = map(int, input().split())
    print(knight_moves(x, y))

if __name__ == '__main__':
    main()

