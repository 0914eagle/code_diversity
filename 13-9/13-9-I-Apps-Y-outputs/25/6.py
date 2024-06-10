
def read_grid():
    grid = []
    for _ in range(3):
        grid.append(list(map(int, input().split())))
    return grid

def solve(grid):
    a1, a2, a3, b1, b2, b3 = set(), set(), set(), set(), set(), set()
    for i in range(3):
        for j in range(3):
            a1.add(grid[i][j] - b1[j])
            a2.add(grid[i][j] - b2[i])
            a3.add(grid[i][j] - b3[i])
    return "Yes" if a1 <= a2 and a2 <= a3 and b1 <= b2 and b2 <= b3 else "No"

if __name__ == '__main__':
    grid = read_grid()
    print(solve(grid))

