
def is_correct_grid(grid):
    n = len(grid)
    if n % 2 == 1 or n > 24:
        return 0
    
    for i in range(n):
        row = grid[i]
        if len(row) != n:
            return 0
        for j in range(n):
            if row[j] not in ["B", "W"]:
                return 0
    
    for i in range(n):
        count_b = 0
        count_w = 0
        for j in range(n):
            if grid[j][i] == "B":
                count_b += 1
            else:
                count_w += 1
        if count_b != count_w:
            return 0
    
    for i in range(n):
        count_b = 0
        count_w = 0
        for j in range(n):
            if grid[i][j] == "B":
                count_b += 1
            else:
                count_w += 1
        if count_b != count_w:
            return 0
    
    for i in range(n):
        for j in range(n-2):
            if grid[i][j] == grid[i][j+1] == grid[i][j+2]:
                return 0
        for j in range(n-2):
            if grid[j][i] == grid[j+1][i] == grid[j+2][i]:
                return 0
    
    return 1

def main():
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(input())
    print(is_correct_grid(grid))

if __name__ == '__main__':
    main()

