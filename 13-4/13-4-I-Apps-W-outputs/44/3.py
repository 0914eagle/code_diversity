
def knight_moves(x, y):
    # Initialize a dictionary to store the number of ways to reach each square
    ways = {(0, 0): 1}
    
    # Loop through all possible moves for the knight
    for i in range(x):
        for j in range(y):
            # If the current square is not already in the dictionary, add it and its possible moves
            if (i, j) not in ways:
                ways[(i, j)] = ways.get((i-1, j+2), 0) + ways.get((i+1, j+2), 0) + ways.get((i-2, j+1), 0) + ways.get((i+2, j+1), 0)
    
    # Return the number of ways to reach the target square, modulo 10^9 + 7
    return ways[(x, y)] % 1000000007

def main():
    x, y = map(int, input().split())
    print(knight_moves(x, y))

if __name__ == '__main__':
    main()

