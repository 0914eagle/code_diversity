
def get_rating(grid):
    # Initialize variables
    rating = 0
    moves = []

    # Loop through each row of the grid
    for row in grid:
        # Check if the current row is a move
        if row.count('$') > 0:
            # Add the current row to the list of moves
            moves.append(row)

    # Loop through each move and count the number of moves
    for move in moves:
        # Check if the current move is a single blank column
        if move.count('_') == len(move) - 1:
            # Increment the rating
            rating += 1

    return rating

def main():
    # Read the input grid
    grid = []
    for _ in range(int(input())):
        grid.append(input())

    # Get the rating of the grid
    rating = get_rating(grid)

    # Print the rating
    print(rating)

if __name__ == '__main__':
    main()

