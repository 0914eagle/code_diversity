
def get_input():
    grid = []
    for _ in range(3):
        grid.append(list(map(int, input().split())))
    return grid

def is_takahashi_correct(grid):
    a_set = set()
    b_set = set()
    for i in range(3):
        for j in range(3):
            a_set.add(grid[i][j] - grid[i][j-1])
            b_set.add(grid[i][j] - grid[i-1][j])
    a_set.discard(0)
    b_set.discard(0)
    return len(a_set) == 3 and len(b_set) == 3

def main():
    grid = get_input()
    if is_takahashi_correct(grid):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

