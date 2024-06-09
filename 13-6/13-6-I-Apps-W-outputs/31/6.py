
def get_max_square_area(grid, r1, c1, r2, c2):
    max_area = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if grid[i][j] == grid[r1][c1]:
                area = (r2-r1+1) * (c2-c1+1)
                if area > max_area:
                    max_area = area
    return max_area

def solve(grid, options):
    result = []
    for option in options:
        r1, c1, r2, c2 = option
        result.append(get_max_square_area(grid, r1, c1, r2, c2))
    return result

if __name__ == '__main__':
    n, m, q = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(input()))
    options = []
    for i in range(q):
        options.append(list(map(int, input().split())))
    result = solve(grid, options)
    for i in result:
        print(i)

