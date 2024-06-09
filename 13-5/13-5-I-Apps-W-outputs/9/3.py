
def get_max_square(grid, r1, c1, r2, c2):
    max_area = 0
    for i in range(r1, r2):
        for j in range(c1, c2):
            if grid[i][j] == grid[r1][c1]:
                area = 1
                for ii in range(i, r2):
                    for jj in range(j, c2):
                        if grid[ii][jj] != grid[r1][c1]:
                            break
                        area += 1
                    else:
                        continue
                    break
                max_area = max(max_area, area)
    return max_area

def solve(grid, options):
    result = []
    for option in options:
        r1, c1, r2, c2 = option
        result.append(get_max_square(grid, r1, c1, r2, c2))
    return result

