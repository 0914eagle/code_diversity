
def f1(n, k, matrix):
    # Initialize a dictionary to store the shortest distance from tile 1 to each other tile
    distances = {1: 0}
    # Initialize a set to keep track of the tiles that have been visited
    visited = set()
    # Initialize a queue to perform BFS
    queue = [1]
    # Loop until the queue is empty
    while queue:
        # Dequeue a tile from the queue
        current_tile = queue.pop(0)
        # If the current tile is the destination tile, return the shortest distance
        if current_tile == k:
            return distances[current_tile]
        # If the current tile has not been visited, mark it as visited and add its neighbors to the queue
        if current_tile not in visited:
            visited.add(current_tile)
            # Get the neighbors of the current tile
            neighbors = get_neighbors(current_tile, matrix)
            # Loop through the neighbors
            for neighbor in neighbors:
                # If the neighbor has not been visited, add it to the queue and update the shortest distance
                if neighbor not in visited:
                    queue.append(neighbor)
                    distances[neighbor] = distances[current_tile] + 1
    # If the destination tile has not been reached, return -1
    return -1

def get_neighbors(tile, matrix):
    # Get the row and column of the tile
    row, col = tile // n, tile % n
    # Initialize a list to store the neighbors
    neighbors = []
    # Loop through the possible neighbors
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            # If the neighbor is valid, add it to the list
            if 0 <= i < n and 0 <= j < n and (i != row or j != col):
                neighbors.append(i * n + j)
    return neighbors

def f2(n, k, matrix):
    # Initialize the shortest distance to infinity
    shortest_distance = float('inf')
    # Loop through the possible starting tiles
    for i in range(1, n*n+1):
        # If the starting tile is valid, calculate the shortest distance and compare it to the current shortest distance
        if i in matrix:
            distance = f1(n, k, matrix)
            if distance != -1 and distance < shortest_distance:
                shortest_distance = distance
    # Return the shortest distance
    return shortest_distance

if __name__ == '__main__':
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(f2(n, k, matrix))

