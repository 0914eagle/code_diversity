
def f1(board1, board2):
    # Initialize a list to store the positions of pawns
    pawns = []

    # Iterate through the strings and append the positions of pawns to the list
    for i in range(len(board1)):
        for j in range(len(board2)):
            if board1[i] == "X" or board2[j] == "X":
                pawns.append((i, j))

    # Initialize a set to store the positions of bishwocks
    bishwocks = set()

    # Iterate through the possible positions of bishwocks
    for i in range(len(board1)):
        for j in range(len(board2)):
            # Check if the current position is not occupied by a pawn and not already occupied by a bishwock
            if (i, j) not in pawns and (i, j) not in bishwocks:
                # Add the current position to the set of bishwocks
                bishwocks.add((i, j))

    # Return the maximum amount of bishwocks that can be placed on the board
    return len(bishwocks)

