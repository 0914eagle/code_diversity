
def extract_diagonal(grid):
    diagonal_letters = [grid[i][i] for i in range(3)]
    return ''.join(diagonal_letters)

if __name__ == '__main__':
    grid = [input() for _ in range(3)]
    result = extract_diagonal(grid)
    print(result)
