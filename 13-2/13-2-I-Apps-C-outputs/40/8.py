
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
    if k == n:
        if is_valid_solution(grid, n, k):
            return grid
        else:
            return None
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                for num in range(1, n + 1):
                    grid[i][j] = num
                    if solve_superdoku(grid, n, k + 1) is not None:
                        return grid
                grid[i][j] = 0
    return None

def main():
    n, k = map(int, input().split())
    grid = [[0] * n for _ in range(n)]
    for i in range(k):
        grid[i] = list(map(int, input().split()))
    solution = solve_superdoku(grid, n, k)
    if solution is not None:
        print("yes")
        for row in solution:
            print(" ".join(map(str, row)))
    else:
        print("no")

if __name__ == "__main__":
    main()

