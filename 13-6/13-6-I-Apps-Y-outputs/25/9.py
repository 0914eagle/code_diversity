
def get_rating(grid):
    # Initialize variables
    rating = 0
    moves = []

    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the current position is a '$'
            if grid[i][j] == '$':
                # Check if the current move is already in the moves list
                if moves[-1:] != [i, j]:
                    # Add the current move to the moves list
                    moves.append([i, j])
                    # Increment the rating
                    rating += 1

    # Return the rating
    return rating

def main():
    # Read the grid from stdin
    grid = [input() for _ in range(int(input()))]

    # Get the rating of the dance
    rating = get_rating(grid)

    # Print the rating
    print(rating)

if __name__ == '__main__':
    main()

