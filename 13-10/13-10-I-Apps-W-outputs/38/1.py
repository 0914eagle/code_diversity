
def get_input():
    n, k = map(int, input().split())
    return n, k

def count_rooks(n, k):
    # Initialize a 2D array to store the number of rooks in each cell
    rooks = [[0] * n for _ in range(n)]
    
    # Initialize a set to store the pairs of rooks that attack each other
    pairs = set()
    
    # Loop through each cell and count the number of rooks that attack it
    for i in range(n):
        for j in range(n):
            # Count the number of rooks in the same row and column
            row_count = sum(rooks[i])
            col_count = sum(rooks[j][k] for k in range(n))
            
            # If the cell is not under attack, place a rook in it
            if row_count + col_count < k:
                rooks[i][j] = 1
                
                # If the cell is on the diagonal, add it to the pairs set
                if i == j:
                    pairs.add((i, j))
    
    # Initialize a variable to store the number of ways to place the rooks
    ways = 0
    
    # Loop through each cell and count the number of ways to place rooks in it
    for i in range(n):
        for j in range(n):
            # If the cell is not under attack, add the number of ways to place a rook in it
            if rooks[i][j] == 0:
                ways += 1
    
    # Return the number of ways to place the rooks, modulo 998244353
    return ways % 998244353

def main():
    n, k = get_input()
    print(count_rooks(n, k))

if __name__ == '__main__':
    main()

