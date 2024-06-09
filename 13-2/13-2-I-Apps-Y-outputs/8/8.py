
def is_correct_grid(grid):
    n = len(grid)
    for i in range(n):
        row = grid[i]
        col = [row[j] for row in grid]
        if not is_balanced(row) or not is_balanced(col):
            return False
    return True

def is_balanced(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] == 'B':
            count += 1
        elif lst[i] == 'W':
            count -= 1
        if count < 0:
            return False
    return count == 0

if __name__ == '__main__':
    n = int(input())
    grid = [input() for _ in range(n)]
    print(int(is_correct_grid(grid)))

