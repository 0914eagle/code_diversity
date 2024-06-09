
import sys

def find_exit(maze):
    # Initialize variables
    rows = len(maze)
    cols = len(maze[0])
    start_row, start_col = None, None
    exit_row, exit_col = None, None
    on_fire = set()

    # Find Joe's starting position and the exit
    for row in range(rows):
        for col in range(cols):
            if maze[row][col] == "J":
                start_row, start_col = row, col
            elif maze[row][col] == "F":
                on_fire.add((row, col))
            elif maze[row][col] == ".":
                exit_row, exit_col = row, col

    # Breadth-first search to find the shortest path to the exit
    queue = [(start_row, start_col, 0)]
    visited = set()
    while queue:
        row, col, time = queue.pop(0)
        if (row, col) == (exit_row, exit_col):
            return time
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] != "#" and (r, c) not in on_fire:
                queue.append((r, c, time+1))
    return -1

def main():
    rows, cols = map(int, input().split())
    maze = [input() for _ in range(rows)]
    print(find_exit(maze))

if __name__ == '__main__':
    main()

