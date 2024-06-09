
def f1(n, k, art_installation):
    # Initialize a dictionary to store the shortest distance from tile 1 to each tile
    distances = {1: 0}
    # Initialize a queue to perform BFS
    queue = [1]
    # Loop until the queue is empty
    while queue:
        # Get the current tile from the queue
        current_tile = queue.pop(0)
        # Get the neighbors of the current tile
        neighbors = get_neighbors(current_tile, n, k, art_installation)
        # Loop through the neighbors
        for neighbor in neighbors:
            # If the neighbor is not in the dictionary, add it to the dictionary with the current distance + 1
            if neighbor not in distances:
                distances[neighbor] = distances[current_tile] + 1
                # Add the neighbor to the queue
                queue.append(neighbor)
    # Return the shortest distance from tile 1 to tile k
    return distances[k] if k in distances else -1

def get_neighbors(tile, n, k, art_installation):
    # Get the row and column of the tile
    row, col = tile // n, tile % n
    # Initialize a list to store the neighbors
    neighbors = []
    # Loop through the possible rows and columns
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            # If the neighbor is valid, add it to the list
            if 0 <= i < n and 0 <= j < n and art_installation[i][j] != 0:
                neighbors.append(i*n + j)
    return neighbors

def f2(n, k, art_installation):
    # Initialize a dictionary to store the shortest distance from each tile to tile k
    distances = {}
    # Loop through the tiles
    for tile in range(1, n*n+1):
        # If the tile is not in the dictionary, add it with the shortest distance from tile 1 to tile k
        if tile not in distances:
            distances[tile] = f1(n, k, art_installation)
    # Return the shortest distance from tile 1 to tile k
    return distances[1]

if __name__ == '__main__':
    n, k = map(int, input().split())
    art_installation = []
    for _ in range(n):
        art_installation.append(list(map(int, input().split())))
    print(f2(n, k, art_installation))

