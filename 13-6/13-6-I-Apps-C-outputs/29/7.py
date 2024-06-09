
def f1(R, C, maze):
    # Initialize variables
    joe_row, joe_col = 0, 0
    fire_row, fire_col = 0, 0
    time = 0
    visited = set()
    queue = [(joe_row, joe_col)]

    # Find Joe's position in the maze
    for i in range(R):
        for j in range(C):
            if maze[i][j] == "J":
                joe_row, joe_col = i, j
                break

    # Breadth-first search to find the shortest path to the edge of the maze
    while queue:
        row, col = queue.pop(0)
        visited.add((row, col))
        if (row, col) in [(0, c), (R-1, c), (r, 0), (r, C-1)]:
            return time
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < R and 0 <= c < C and maze[r][c] == "." and (r, c) not in visited:
                queue.append((r, c))
                time += 1

    return -1

def f2(R, C, maze):
    # Initialize variables
    joe_row, joe_col = 0, 0
    fire_row, fire_col = 0, 0
    time = 0
    visited = set()
    queue = [(joe_row, joe_col)]

    # Find Joe's position in the maze
    for i in range(R):
        for j in range(C):
            if maze[i][j] == "J":
                joe_row, joe_col = i, j
                break

    # Breadth-first search to find the shortest path to the edge of the maze
    while queue:
        row, col = queue.pop(0)
        visited.add((row, col))
        if (row, col) in [(0, c), (R-1, c), (r, 0), (r, C-1)]:
            return time
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < R and 0 <= c < C and maze[r][c] == "." and (r, c) not in visited:
                queue.append((r, c))
                time += 1

    return -1

if __name__ == '__main__':
    R, C = map(int, input().split())
    maze = [input() for _ in range(R)]
    print(f2(R, C, maze))

