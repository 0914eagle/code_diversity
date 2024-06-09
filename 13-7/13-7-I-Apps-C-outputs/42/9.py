
def get_max_flowers(field, initial_position):
    rows = len(field)
    cols = len(field[0])
    visited = set()
    queue = [(initial_position[0], initial_position[1], 0)]
    while queue:
        row, col, count = queue.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        count += 1
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < cols and field[r][c] > field[row][col]:
                queue.append((r, c, count))
    return count

