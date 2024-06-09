
def f1(board1, board2):
    # Initialize a list to store the positions of the bishwocks
    bishwocks = []
    # Loop through the rows of the board
    for i in range(len(board1)):
        # Loop through the columns of the board
        for j in range(len(board1[0])):
            # Check if the current position is empty
            if board1[i][j] == "0" and board2[i][j] == "0":
                # Add the current position to the list of bishwocks
                bishwocks.append((i, j))
    # Return the length of the list of bishwocks
    return len(bishwocks)

