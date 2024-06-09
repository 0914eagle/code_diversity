
def knight_moves(x, y):
    # Initialize a dictionary to store the number of ways to reach each square
    ways = {(0, 0): 1}
    
    # Loop through all possible moves of the knight
    for i in range(x + 1):
        for j in range(y + 1):
            # If the current square is not the starting square and has not been visited before, continue
            if (i, j) != (0, 0) and (i, j) not in ways:
                continue
            
            # If the current square is the starting square, add the number of ways to reach it from the starting square
            if (i, j) == (0, 0):
                ways[(i, j)] = 1
            
            # If the current square is not the starting square, add the number of ways to reach it from the previous square
            else:
                ways[(i, j)] = ways[(i - 1, j + 2)] + ways[(i - 2, j + 1)]
    
    # Return the number of ways to reach the target square
    return ways[(x, y)] % (10**9 + 7)

def main():
    x, y = map(int, input().split())
    print(knight_moves(x, y))

if __name__ == '__main__':
    main()

