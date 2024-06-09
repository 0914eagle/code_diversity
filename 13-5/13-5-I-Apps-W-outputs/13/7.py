
def get_grid_size(grid_str):
    return tuple(map(int, grid_str.split()))

def get_painted_cells(painted_cells_str):
    return [tuple(map(int, cell.split())) for cell in painted_cells_str.split()]

def count_subrectangles(grid_size, painted_cells):
    grid = [[0] * grid_size[1] for _ in range(grid_size[0])]
    for row, col in painted_cells:
        grid[row-1][col-1] = 1
    
    count = [0] * 10
    for i in range(grid_size[0]-2):
        for j in range(grid_size[1]-2):
            count[sum(grid[i][j:j+3]) + sum(grid[i+1][j:j+3]) + sum(grid[i+2][j:j+3])] += 1
    
    return count

def main():
    grid_size = get_grid_size(input())
    painted_cells = get_painted_cells(input())
    count = count_subrectangles(grid_size, painted_cells)
    for i in range(10):
        print(count[i])

if __name__ == '__main__':
    main()

