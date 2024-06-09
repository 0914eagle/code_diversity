
def get_wrongness_sum(grid, D):
    
    # Initialize the minimum sum to infinity
    min_sum = float('inf')

    # Loop through all possible colors
    for color in range(1, len(D) + 1):
        # Calculate the wrongness sum for the current color
        wrongness_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != color:
                    wrongness_sum += D[grid[i][j] - 1][color - 1]

        # Update the minimum sum if the current sum is smaller
        if wrongness_sum < min_sum:
            min_sum = wrongness_sum

    return min_sum

def solve(grid, D):
    
    return get_wrongness_sum(grid, D)

if __name__ == '__main__':
    grid = [[1, 2, 3], [4, 5, 6]]
    D = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    print(solve(grid, D))

