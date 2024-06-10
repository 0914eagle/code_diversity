
def count_rooks(n, k):
    # Initialize a 2D array to store the number of rooks in each cell
    board = [[0] * n for _ in range(n)]
    
    # Initialize a set to store the pairs of rooks that attack each other
    pairs = set()
    
    # Iterate over each row
    for i in range(n):
        # Iterate over each column
        for j in range(n):
            # If the current cell is empty, place a rook in it
            if board[i][j] == 0:
                board[i][j] = 1
                # Check if the current cell is under attack by any other rook
                attacks = 0
                for r in range(n):
                    if r != i and board[r][j] == 1:
                        attacks += 1
                    if r != j and board[i][r] == 1:
                        attacks += 1
                # If the current cell is under attack, add it to the pairs set
                if attacks == k:
                    pairs.add((i, j))
    
    # Initialize a variable to store the total number of ways to place the rooks
    total = 0
    
    # Iterate over each pair of rooks that attack each other
    for pair in pairs:
        # Get the row and column indices of the current pair
        i, j = pair
        # Initialize a variable to store the number of ways to place the rooks in the current pair
        ways = 1
        # Iterate over each row
        for r in range(n):
            # If the current row is not the same as the row of the current pair,
            # check if there are any rooks in the same column as the current pair
            if r != i:
                # If there are no rooks in the same column as the current pair,
                # add the number of ways to place rooks in the current pair
                if board[r][j] == 0:
                    ways *= n - 1
            # If the current row is the same as the row of the current pair,
            # check if there are any rooks in the same row as the current pair
            else:
                # If there are no rooks in the same row as the current pair,
                # add the number of ways to place rooks in the current pair
                if board[r][j] == 0:
                    ways *= n - 1
        # Add the number of ways to place rooks in the current pair to the total
        total += ways
    
    # Return the total number of ways to place rooks modulo 998244353
    return total % 998244353

def input_manager():
    # Read a line of input from stdin and split it into tokens
    n, k = map(int, input().split())
    
    # Return the input as a tuple
    return n, k

if __name__ == '__main__':
    # Get the input from the user
    n, k = input_manager()
    
    # Call the count_rooks function and print the result
    print(count_rooks(n, k))

