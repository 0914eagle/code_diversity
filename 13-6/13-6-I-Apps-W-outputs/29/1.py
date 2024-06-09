
def get_wrongness(grid, colors, D):
    # Initialize the wrongness of all the squares to 0
    wrongness = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Loop through each square and calculate its wrongness
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the square is not the same color as the neighboring squares, calculate its wrongness
            if grid[i][j] != grid[i-1][j] or grid[i][j] != grid[i][j-1]:
                wrongness[i][j] = D[grid[i][j]-1][grid[i-1][j]-1] + D[grid[i][j]-1][grid[i][j-1]-1]

    # Return the sum of the wrongness of all the squares
    return sum(sum(wrongness, []))

def solve(grid, colors, D):
    # Initialize the minimum possible sum of wrongness to infinity
    min_wrongness = float('inf')
    # Loop through each possible color for the first square
    for i in range(1, len(colors)+1):
        # Loop through each possible color for the second square
        for j in range(1, len(colors)+1):
            # If the colors are the same, skip this combination
            if i == j:
                continue
            # Create a new grid with the first two squares painted with the current colors
            new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
            new_grid[0][0] = i
            new_grid[0][1] = j
            # Calculate the wrongness of the new grid
            wrongness = get_wrongness(new_grid, colors, D)
            # If the wrongness is less than the minimum possible wrongness, update the minimum possible wrongness
            if wrongness < min_wrongness:
                min_wrongness = wrongness

    # Return the minimum possible sum of wrongness
    return min_wrongness

if __name__ == '__main__':
    grid = [[0 for _ in range(500)] for _ in range(500)]
    colors = [i for i in range(1, 31)]
    D = [[0 for _ in range(30)] for _ in range(30)]
    for i in range(1, 31):
        for j in range(1, 31):
            D[i-1][j-1] = int(input())
    print(solve(grid, colors, D))

