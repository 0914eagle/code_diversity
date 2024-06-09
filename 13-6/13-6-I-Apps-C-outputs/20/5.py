
def is_connected(grid):
    # Check if all the # are connected
    visited = set()
    queue = [(0, 0)]
    while queue:
        row, col = queue.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if grid[row][col] == '#':
            queue.extend([(row-1, col), (row+1, col), (row, col-1), (row, col+1)])
    return len(visited) == 6

def can_form_cube(grid):
    # Check if the grid can be folded into a cube
    if not is_connected(grid):
        return False
    for row in range(6):
        for col in range(6):
            if grid[row][col] == '#':
                if row == 0 or row == 5 or col == 0 or col == 5:
                    continue
                if grid[row-1][col] == '#' and grid[row+1][col] == '#' and grid[row][col-1] == '#' and grid[row][col+1] == '#':
                    return True
    return False

def main():
    grid = []
    for _ in range(6):
        grid.append(input())
    if can_form_cube(grid):
        print("can fold")
    else:
        print("cannot fold")

if __name__ == '__main__':
    main()

