
def shortest_path(n, k, art_installation):
    # Initialize a dictionary to store the shortest distance from tile 1 to each tile
    distances = {1: 0}
    # Initialize a dictionary to store the previous tile for each tile
    previous = {1: None}
    # Initialize a queue to perform BFS
    queue = [1]
    # Loop until the queue is empty
    while queue:
        # Get the current tile from the queue
        current_tile = queue.pop(0)
        # If the current tile is the destination tile, return the shortest distance
        if current_tile == k:
            return distances[current_tile]
        # Get the neighbors of the current tile
        neighbors = get_neighbors(current_tile, n, k, art_installation)
        # Loop through the neighbors
        for neighbor in neighbors:
            # If the neighbor has not been visited before, add it to the queue and dictionary
            if neighbor not in distances:
                queue.append(neighbor)
                distances[neighbor] = distances[current_tile] + 1
                previous[neighbor] = current_tile
    # If the destination tile has not been reached, return -1
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
        # If the neighbor is within the bounds of the art installation, add it to the list
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
    print(shortest_path(n, k, art_installation))

