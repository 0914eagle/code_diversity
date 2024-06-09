
def f1(n, m, s):
    # Initialize variables
    witch_cells = set()
    treasure_cell = (n, m)
    current_cell = (1, 1)
    visited_cells = set([current_cell])
    queue = [(current_cell, 0)]

    # Breadth-first search
    while queue:
        current_cell, distance = queue.pop(0)
        if current_cell == treasure_cell:
            return distance
        for neighbor in get_neighbors(current_cell, n, m, s):
            if neighbor not in visited_cells:
                visited_cells.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1

def f2(n, m, s):
    # Initialize variables
    witch_cells = set()
    treasure_cell = (n, m)
    current_cell = (1, 1)
    visited_cells = set([current_cell])
    queue = [(current_cell, 0)]

    # Breadth-first search
    while queue:
        current_cell, distance = queue.pop(0)
        if current_cell == treasure_cell:
            return distance
        for neighbor in get_neighbors(current_cell, n, m, s):
            if neighbor not in visited_cells:
                visited_cells.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1

def get_neighbors(cell, n, m, s):
    neighbors = []
    for dr, dc in [(0, 1), (1, 0)]:
        r, c = cell
        nr, nc = r + dr, c + dc
        if 1 <= nr <= n and 1 <= nc <= m and s[nr - 1][nc - 1] != '#':
            neighbors.append((nr, nc))
    return neighbors

if __name__ == '__main__':
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    print(f1(n, m, s))
    print(f2(n, m, s))

