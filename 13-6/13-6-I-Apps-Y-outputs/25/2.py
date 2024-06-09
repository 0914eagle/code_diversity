
def get_rating(grid):
    # Initialize variables
    rating = 0
    current_move = 0
    previous_move = 0

    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the current position is a '$'
            if grid[i][j] == '$':
                # Check if the previous position was a '$'
                if previous_move == 1:
                    # Increment the current move
                    current_move += 1
                # Set the previous move to 1
                previous_move = 1
            else:
                # Set the previous move to 0
                previous_move = 0

    # Return the rating
    return current_move

def main():
    # Read the grid from stdin
    grid = []
    for _ in range(int(input())):
        grid.append(input())

    # Get the rating of the grid
    rating = get_rating(grid)

    # Print the rating
    print(rating)

if __name__ == '__main__':
    main()

