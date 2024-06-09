
def count_bishwocks(pawns_positions, bishwocks_positions):
    # Initialize a set to store the positions of the bishwocks
    bishwocks = set()
    # Loop through the positions of the pawns
    for pawn_position in pawns_positions:
        # Check if the current position is already occupied by a bishwock
        if pawn_position in bishwocks:
            # If it is, remove it from the set of bishwocks
            bishwocks.remove(pawn_position)
    # Loop through the positions of the bishwocks
    for bishwock_position in bishwocks_positions:
        # Check if the current position is already occupied by a pawn
        if bishwock_position in pawns_positions:
            # If it is, remove it from the set of bishwocks
            bishwocks.remove(bishwock_position)
    # Return the number of bishwocks that can be placed on the board
    return len(bishwocks)

def main():
    # Read the input data
    pawns_positions = input()
    bishwocks_positions = input()
    # Call the count_bishwocks function and print the result
    print(count_bishwocks(pawns_positions, bishwocks_positions))

if __name__ == '__main__':
    main()

