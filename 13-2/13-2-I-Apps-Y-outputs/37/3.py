
def f1(n, k, matrix):
    # Initialize a dictionary to store the shortest distance from tile 1 to each other tile
    distances = {1: 0}
    # Initialize a set to keep track of the tiles that have been visited
    visited = set()
    # Initialize a queue to do BFS
    queue = [1]
    # Loop until the queue is empty
    while queue:
        # Get the current tile from the queue
        current_tile = queue.pop(0)
        # If the current tile is the target tile, return the shortest distance
        if current_tile == k:
            return distances[current_tile]
        # Mark the current tile as visited
        visited.add(current_tile)
        # Get the neighbors of the current tile
        neighbors = get_neighbors(current_tile, matrix)
        # Loop through the neighbors
        for neighbor in neighbors:
            # If the neighbor has not been visited, add it to the queue and update the shortest distance
            if neighbor not in visited:
                queue.append(neighbor)
                distances[neighbor] = distances[current_tile] + 1
    # If the target tile has not been reached, return -1
    return -1

def get_neighbors(tile, matrix):
    # Get the row and column of the tile
    row, col = tile // n, tile % n
    # Get the neighbors of the tile
    neighbors = []
    if row > 0:
        neighbors.append(tile - n)
    if row < n - 1:
        neighbors.append(tile + n)
    if col > 0:
        neighbors.append(tile - 1)
    if col < n - 1:
        neighbors.append(tile + 1)
    return neighbors

def f2(n, k, matrix):
    # Initialize the shortest distance to infinity
    shortest_distance = float('inf')
    # Loop through all possible starting tiles
    for i in range(1, k + 1):
        # If the starting tile is not the target tile, find the shortest distance from the starting tile to the target tile
        if i != k:
            distance = f1(n, k, matrix)
            # If the distance is shorter than the current shortest distance, update the shortest distance
            if distance != -1 and distance < shortest_distance:
                shortest_distance = distance
    # Return the shortest distance
    return shortest_distance

if __name__ == '__main__':
    n, k = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    print(f2(n, k, matrix))

