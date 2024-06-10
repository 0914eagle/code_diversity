
def is_correct(grid):
    a_set = set()
    b_set = set()
    for i in range(3):
        for j in range(3):
            a_set.add(grid[i][0] - grid[i][j])
            b_set.add(grid[i][j] - grid[i][0])
    return len(a_set) == 6 and len(b_set) == 6

def main():
    grid = []
    for i in range(3):
        grid.append(list(map(int, input().split())))
    print("Yes" if is_correct(grid) else "No")

if __name__ == '__main__':
    main()

