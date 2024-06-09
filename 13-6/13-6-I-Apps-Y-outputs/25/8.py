
def get_rating(grid):
    # Initialize variables
    rating = 0
    current_move = 0
    previous_column = None

    # Iterate through the grid
    for row in grid:
        for column in row:
            # Check if the current column is blank
            if column == "_":
                # Check if the previous column was blank
                if previous_column == "_":
                    # Increment the current move
                    current_move += 1
            # Update the previous column
            previous_column = column

    # Return the rating
    return current_move

def main():
    # Read the input
    N, M = map(int, input().split())
    grid = [input() for _ in range(N)]

    # Get the rating
    rating = get_rating(grid)

    # Print the output
    print(rating)

if __name__ == '__main__':
    main()

