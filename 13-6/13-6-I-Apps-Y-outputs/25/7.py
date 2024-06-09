
def get_rating(grid):
    # Initialize variables
    rating = 0
    moves = 0

    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the current position is a '$'
            if grid[i][j] == '$':
                # Increment the moves counter
                moves += 1
                # Check if the current position is the last column of a move
                if j == len(grid[0]) - 1:
                    # Increment the rating
                    rating += 1

    # Return the rating
    return rating

def main():
    # Read the input
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(input())

    # Get the rating
    rating = get_rating(grid)

    # Print the output
    print(rating)

if __name__ == '__main__':
    main()

