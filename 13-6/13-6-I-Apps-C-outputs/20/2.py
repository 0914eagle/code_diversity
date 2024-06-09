
def f1(grid):
    # Check if the input grid is valid
    if len(grid) != 6 or len(grid[0]) != 6:
        return "Invalid input"
    
    # Check if the grid is connected
    if not is_connected(grid):
        return "Cannot fold"
    
    # Check if the grid can be folded into a cube
    if can_fold(grid):
        return "Can fold"
    else:
        return "Cannot fold"

def is_connected(grid):
    # Check if the grid is connected by searching for a path from the top-left corner to the bottom-right corner
    queue = [(0, 0)]
    visited = set()
    while queue:
        row, col = queue.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if grid[row][col] == "#":
            queue.extend([(row-1, col), (row+1, col), (row, col-1), (row, col+1)])
        if row == 5 and col == 5:
            return True
    return False

def can_fold(grid):
    # Check if the grid can be folded into a cube by checking if the number of # is equal to 6
    count = 0
    for row in grid:
        for cell in row:
            if cell == "#":
                count += 1
    return count == 6

if __name__ == '__main__':
    grid = [
        [".", ".", ".", ".", ".", "."],
        [".", "#", ".", ".", ".", "."],
        ["#", "#", "#", ".", ".", "."],
        [".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "."]
    ]
    print(f1(grid))

