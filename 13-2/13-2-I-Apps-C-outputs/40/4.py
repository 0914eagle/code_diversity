
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

def solve_superdoku(grid, n, k):
    # Check if the given grid is valid
    if not is_valid_solution(grid, n, k):
        return False
    
    # Check if all rows and columns are filled
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                return False
    
    return True

def main():
    n, k = map(int, input().split())
    grid = []
    for i in range(k):
        grid.append(list(map(int, input().split())))
    
    if solve_superdoku(grid, n, k):
        print("yes")
        for i in range(n):
            print(" ".join(map(str, grid[i])))
    else:
        print("no")

if __name__ == "__main__":
    main()

