
def is_correct_grid(grid):
    n = len(grid)
    for i in range(n):
        row = grid[i]
        if row.count("B") != row.count("W"):
            return False
    for j in range(n):
        col = [row[j] for row in grid]
        if col.count("B") != col.count("W"):
            return False
    for i in range(n-2):
        for j in range(n-2):
            if grid[i][j] == grid[i+1][j+1] == grid[i+2][j+2]:
                return False
    return True

def main():
    n = int(input())
    grid = [input() for _ in range(n)]
    print(int(is_correct_grid(grid)))

if __name__ == '__main__':
    main()

