
def solve(n, m, s):
    # Initialize the variables
    k = 0
    rows, cols = n, m
    start, end = (0, 0), (n-1, m-1)
    visited = set()
    queue = [(start, 0)]

    # Loop through the queue
    while queue:
        current, distance = queue.pop(0)
        visited.add(current)
        if current == end:
            return distance
        for neighbor in get_neighbors(current, rows, cols):
            if neighbor not in visited and s[neighbor[0]-1][neighbor[1]-1] != "#":
                queue.append((neighbor, distance+1))
                k = max(k, distance+1)

    return k

def get_neighbors(cell, rows, cols):
    (i, j) = cell
    neighbors = []
    if i < rows-1:
        neighbors.append((i+1, j))
    if j < cols-1:
        neighbors.append((i, j+1))
    return neighbors

