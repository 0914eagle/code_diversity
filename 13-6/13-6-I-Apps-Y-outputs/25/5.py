
def get_rating(grid):
    # Initialize variables
    rating = 0
    moves = []

    # Loop through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current character is '$', add the current move to the list of moves
            if grid[i][j] == '$':
                moves.append((i, j))
    # Loop through the list of moves
    for i in range(len(moves) - 1):
        # If the current move is not the last move and the next move is not in the same column, increment the rating
        if moves[i] != moves[-1] and moves[i + 1][1] != moves[i][1]:
            rating += 1

    return rating

def main():
    # Read the input grid
    grid = []
    for _ in range(int(input())):
        grid.append(input())

    # Get the rating of the dance
    rating = get_rating(grid)

    # Print the rating
    print(rating)

if __name__ == '__main__':
    main()

