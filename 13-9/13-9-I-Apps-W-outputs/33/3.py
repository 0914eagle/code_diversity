
def get_shortest_time(map):
    # Initialize variables
    rows, cols = len(map), len(map[0])
    painter_row, painter_col = None, None
    hedgehogs_row, hedgehogs_col = None, None
    den_row, den_col = None, None
    time = 0
    visited = set()

    # Find the position of the painter, the hedgehogs, and the den
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == 'S':
                hedgehogs_row, hedgehogs_col = i, j
            elif map[i][j] == 'D':
                den_row, den_col = i, j
            elif map[i][j] == 'P':
                painter_row, painter_col = i, j

    # Breadth-first search to find the shortest path from the painter to the den
    queue = [(painter_row, painter_col)]
    while queue:
        row, col = queue.pop(0)
        if (row, col) == (den_row, den_col):
            return time
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < cols and map[r][c] != '*' and (r, c) not in visited:
                queue.append((r, c))
                visited.add((r, c))
        time += 1

    return "KAKTUS"

def main():
    map = []
    for _ in range(int(input())):
        map.append(input())
    print(get_shortest_time(map))

if __name__ == '__main__':
    main()

