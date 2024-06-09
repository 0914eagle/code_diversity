
def n_queens(n, m, board):
    # Initialize variables
    max_queens = 0
    num_ways = 0

    # Loop through each row of the board
    for i in range(n):
        # Loop through each column of the board
        for j in range(m):
            # If the current cell is not broken and is not already occupied by a queen
            if board[i][j] == '.' and (i, j) not in queens:
                # Add the current cell to the list of queens
                queens.append((i, j))
                # Recursively call the function to place the remaining queens
                place_queens(n, m, board, queens)
                # Remove the current cell from the list of queens
                queens.pop()

def place_queens(n, m, board, queens):
    # If all queens have been placed
    if len(queens) == n:
        # Increment the number of ways to place the queens
        num_ways += 1
        # Check if this is the maximum number of queens placed so far
        if len(queens) > max_queens:
            max_queens = len(queens)
        return

    # Loop through each row of the board
    for i in range(n):
        # Loop through each column of the board
        for j in range(m):
            # If the current cell is not broken and is not already occupied by a queen
            if board[i][j] == '.' and (i, j) not in queens:
                # Add the current cell to the list of queens
                queens.append((i, j))
                # Recursively call the function to place the remaining queens
                place_queens(n, m, board, queens)
                # Remove the current cell from the list of queens
                queens.pop()

def main():
    # Read the input
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(input()))

    # Initialize the list of queens
    queens = []

    # Call the function to place the queens
    place_queens(n, m, board, queens)

    # Print the maximum number of queens and the number of ways to place them
    print(max_queens, num_ways)

if __name__ == "__main__":
    main()

