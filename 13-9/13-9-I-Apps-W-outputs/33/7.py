
def get_shortest_time(map):
    # Initialize variables
    rows, cols = len(map), len(map[0])
    start_row, start_col = None, None
    end_row, end_col = None, None
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = []
    time = 0

    # Find the start and end positions
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == "S":
                start_row, start_col = i, j
            elif map[i][j] == "D":
                end_row, end_col = i, j

    # Add the start position to the queue
    queue.append((start_row, start_col, time))
    visited[start_row][start_col] = True

    # Breadth-first search
    while queue:
        row, col, time = queue.pop(0)

        # Check if we have reached the end
        if row == end_row and col == end_col:
            return time

        # Check if we can move to any of the four neighbors
        for i, j in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= i < rows and 0 <= j < cols and map[i][j] != "X" and not visited[i][j]:
                queue.append((i, j, time+1))
                visited[i][j] = True

    # If we reach this point, it means we could not find a path to the end
    return "KAKTUS"

def solve(map):
    return get_shortest_time(map)

if __name__ == '__main__':
    map = [
        [".", ".", "."],
        [".", "D", "."],
        [".", ".", "S"]
    ]
    print(solve(map))

