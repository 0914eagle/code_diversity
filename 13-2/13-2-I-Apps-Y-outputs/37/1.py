
def hopscotch(n, k, art_installation):
    # Initialize a dictionary to store the minimum distance from tile 1 to each tile
    distances = {1: 0}
    # Initialize a queue to perform BFS
    queue = [1]
    # Loop until the queue is empty
    while queue:
        # Dequeue a tile from the queue
        current_tile = queue.pop(0)
        # Get the neighbors of the current tile
        neighbors = get_neighbors(current_tile, n, k, art_installation)
        # Loop through the neighbors
        for neighbor in neighbors:
            # If the neighbor has not been visited before, mark it as visited and add it to the queue
            if neighbor not in distances:
                distances[neighbor] = distances[current_tile] + 1
                queue.append(neighbor)
    # If tile k has been visited, return the minimum distance from tile 1 to tile k
    if k in distances:
        return distances[k]
    # If tile k has not been visited, return -1
    return -1

def get_neighbors(tile, n, k, art_installation):
    # Get the row and column of the tile
    row, col = tile // n, tile % n
    # Initialize a list to store the neighbors
    neighbors = []
    # Loop through the possible moves
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # Get the row and column of the neighbor
        nr, nc = row + dr, col + dc
        # If the neighbor is within the bounds of the art installation, add it to the list of neighbors
        if 0 <= nr < n and 0 <= nc < n:
            neighbor = nr * n + nc
            if art_installation[nr][nc] != 0:
                neighbors.append(neighbor)
    return neighbors

if __name__ == '__main__':
    n, k = map(int, input().split())
    art_installation = []
    for _ in range(n):
        art_installation.append(list(map(int, input().split())))
    print(hopscotch(n, k, art_installation))

