
def get_input():
    return [list(map(int, input().split())) for _ in range(3)]

def check_if_correct(grid):
    a_set = set()
    b_set = set()
    for i in range(3):
        for j in range(3):
            a_set.add(grid[i][j] - grid[i][0])
            b_set.add(grid[0][j] - grid[i][j])
    return len(a_set) == 3 and len(b_set) == 3

def main():
    grid = get_input()
    if check_if_correct(grid):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

