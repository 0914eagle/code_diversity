
def get_grid_size(grid):
    return len(grid), len(grid[0])

def get_subrectangles(grid):
    subrectangles = []
    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            subrectangles.append(grid[i:i+3, j:j+3])
    return subrectangles

def count_black_cells(subrectangle):
    return np.count_nonzero(subrectangle == 1)

def count_subrectangles(grid, num_black_cells):
    subrectangles = get_subrectangles(grid)
    return len([subrectangle for subrectangle in subrectangles if count_black_cells(subrectangle) == num_black_cells])

def main():
    grid_size = get_grid_size(grid)
    num_subrectangles = [count_subrectangles(grid, num_black_cells) for num_black_cells in range(10)]
    for num_black_cells in num_subrectangles:
        print(num_black_cells)

if __name__ == '__main__':
    grid = [[0] * 5 for _ in range(4)]
    main()

