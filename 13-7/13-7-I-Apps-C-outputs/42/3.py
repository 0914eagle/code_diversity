
def max_flowers(field, initial_position):
    # Initialize variables
    rows, cols = len(field), len(field[0])
    visited = set()
    queue = [initial_position]
    visited.add(initial_position)
    count = 0

    # Breadth-first search
    while queue:
        row, col = queue.pop(0)
        count += 1
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and field[r][c] > field[row][col]:
                queue.append((r, c))
                visited.add((r, c))

    return count

