
def is_correct_grid(grid):
    n = len(grid)
    for i in range(n):
        row = grid[i]
        col = [row[j] for row in grid]
        if not is_balanced(row) or not is_balanced(col):
            return False
    return True

def is_balanced(lst):
    n = len(lst)
    count = 0
    for i in range(n):
        if lst[i] == "B":
            count += 1
        else:
            count -= 1
        if count == 3 or count == -3:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    grid = [input() for _ in range(n)]
    print(int(is_correct_grid(grid)))

