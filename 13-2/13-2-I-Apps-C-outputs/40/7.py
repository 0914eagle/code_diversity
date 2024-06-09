
def is_valid_solution(grid, n, k):
    # Check if all rows are valid
    for i in range(n):
        row = [grid[i][j] for j in range(n)]
        if len(set(row)) != n:
            return False
    
    # Check if all columns are valid
    for j in range(n):
        col = [grid[i][j] for i in range(n)]
        if len(set(col)) != n:
            return False
    
    # Check if all subgrids are valid
    for i in range(n):
        for j in range(n):
            subgrid = []
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    subgrid.append(grid[row][col])
            if len(set(subgrid)) != n:
                return False
    
    return True

def solve_superdoku(n, k, grid):
    # Check if the given grid is valid
    if not is_valid_solution(grid, n, k):
        return []
    
    # If the grid is valid, return it
    return grid

def main():
    n, k = map(int, input().split())
    grid = []
    for i in range(k):
        grid.append(list(map(int, input().split())))
    solution = solve_superdoku(n, k, grid)
    if solution:
        print("yes")
        for row in solution:
            print(" ".join(map(str, row)))
    else:
        print("no")

if __name__ == "__main__":
    main()

