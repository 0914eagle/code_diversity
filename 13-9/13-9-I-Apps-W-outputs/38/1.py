
def find_min_chessboard_size(n):
    # Initialize the minimum chessboard size as 1
    m = 1
    # Loop until we find a valid solution or reach the maximum number of pieces
    while m <= n:
        # Check if we can place n pieces on a mxm chessboard
        if can_place_n_pieces(n, m):
            # If we can, return the minimum chessboard size
            return m
        # Increment the minimum chessboard size
        m += 1
    # If we reach the maximum number of pieces and cannot find a solution, return -1
    return -1

def can_place_n_pieces(n, m):
    # Initialize a list to store the coordinates of the pieces
    pieces = []
    # Loop until we have n pieces
    for i in range(n):
        # Generate a random coordinate for the piece
        r, c = random.randint(1, m), random.randint(1, m)
        # Check if the coordinate is already taken
        if (r, c) in pieces:
            # If it is, generate a new coordinate
            continue
        # Add the coordinate to the list of pieces
        pieces.append((r, c))
    # Loop through the pieces and check if the distance between any two pieces is at least as large as their index
    for i in range(n):
        for j in range(i+1, n):
            # Calculate the distance between the two pieces
            dist = abs(pieces[i][0] - pieces[j][0]) + abs(pieces[i][1] - pieces[j][1])
            # Check if the distance is at least as large as their index
            if dist < abs(i - j):
                # If it's not, return False
                return False
    # If we reach this point, return True
    return True

def place_pieces(n, m):
    # Initialize a list to store the coordinates of the pieces
    pieces = []
    # Loop until we have n pieces
    for i in range(n):
        # Generate a random coordinate for the piece
        r, c = random.randint(1, m), random.randint(1, m)
        # Check if the coordinate is already taken
        if (r, c) in pieces:
            # If it is, generate a new coordinate
            continue
        # Add the coordinate to the list of pieces
        pieces.append((r, c))
    # Return the list of pieces
    return pieces

if __name__ == '__main__':
    n = int(input())
    print(find_min_chessboard_size(n))
    print(*place_pieces(n, find_min_chessboard_size(n)), sep='\n')

