
def f1(x, y):
    # Base case: if the knight is already at the destination, return 1
    if x == 0 and y == 0:
        return 1
    
    # Initialize the number of ways to 0
    ways = 0
    
    # Iterate over all possible moves of the knight
    for i in range(max(0, x-2), min(x+2, 10**6)+1):
        for j in range(max(0, y-2), min(y+2, 10**6)+1):
            # If the move is valid, add the number of ways to reach (i, j) from (x, y)
            if i != x and j != y:
                ways += f1(i, j)
    
    # Return the total number of ways modulo 10^9 + 7
    return ways % 1000000007

def f2(x, y):
    # Base case: if the knight is already at the destination, return 1
    if x == 0 and y == 0:
        return 1
    
    # Initialize the number of ways to 0
    ways = 0
    
    # Iterate over all possible moves of the knight
    for i in range(max(0, x-1), min(x+2, 10**6)+1):
        for j in range(max(0, y-1), min(y+2, 10**6)+1):
            # If the move is valid, add the number of ways to reach (i, j) from (x, y)
            if i != x and j != y:
                ways += f2(i, j)
    
    # Return the total number of ways modulo 10^9 + 7
    return ways % 1000000007

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(f1(x, y))

