
def get_rating(grid):
    # Initialize variables
    rating = 0
    moves = []

    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current character is '$', add the current move to the moves list
            if grid[i][j] == '$':
                moves.append((i, j))
    # Iterate through the moves list
    for i in range(len(moves) - 1):
        # If the current move is not the last move and the next move is not the last move, check if the current move and the next move are in the same row
        if moves[i] != moves[-1] and moves[i + 1] != moves[-1]:
            if moves[i][0] == moves[i + 1][0]:
                # If the current move and the next move are in the same row, remove the current move from the moves list
                moves.remove(moves[i])
    # Return the length of the moves list as the rating
    return len(moves)

def main():
    # Read the input grid
    grid = []
    for _ in range(int(input())):
        grid.append(input())
    # Call the get_rating function and print the result
    print(get_rating(grid))

if __name__ == '__main__':
    main()

