
def get_shortest_time(map):
    # Initialize variables
    rows, cols = len(map), len(map[0])
    start_row, start_col = 0, 0
    end_row, end_col = 0, 0
    time = 0
    queue = []

    # Find the start and end positions
    for row in range(rows):
        for col in range(cols):
            if map[row][col] == "S":
                start_row, start_col = row, col
            elif map[row][col] == "D":
                end_row, end_col = row, col

    # Breadth-first search
    queue.append((start_row, start_col, time))
    visited = set()
    while queue:
        row, col, time = queue.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if (row, col) == (end_row, end_col):
            return time
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < cols and map[r][c] != "X" and (r, c) not in visited:
                queue.append((r, c, time+1))
    return "KAKTUS"

def main():
    map = []
    for _ in range(int(input())):
        map.append(input())
    print(get_shortest_time(map))

if __name__ == '__main__':
    main()

