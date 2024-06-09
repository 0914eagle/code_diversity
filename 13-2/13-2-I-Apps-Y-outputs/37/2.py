
def f1(n, k, matrix):
    # Initialize a dictionary to store the shortest distance from tile 1 to each other tile
    distances = {1: 0}
    # Initialize a queue to perform BFS
    queue = [1]
    # Loop until the queue is empty
    while queue:
        # Get the current tile from the queue
        current_tile = queue.pop(0)
        # Get the neighbors of the current tile
        neighbors = get_neighbors(current_tile, matrix)
        # Loop through the neighbors
        for neighbor in neighbors:
            # If the neighbor is not in the dictionary, add it to the dictionary with the current distance plus 1
            if neighbor not in distances:
                distances[neighbor] = distances[current_tile] + 1
                # Add the neighbor to the queue
                queue.append(neighbor)
    # Return the shortest distance from tile 1 to tile k
    return distances[k]

def get_neighbors(tile, matrix):
    # Get the row and column of the tile
    row, col = tile // n, tile % n
    # Initialize a list to store the neighbors
    neighbors = []
    # Loop through the possible neighbors
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            # If the neighbor is valid, add it to the list
            if 0 <= i < n and 0 <= j < n and (i != row or j != col) and matrix[i][j] != 0:
                neighbors.append(i * n + j)
    return neighbors

def f2(n, k, matrix):
    # Initialize the shortest distance to infinity
    shortest_distance = float('inf')
    # Loop through all possible starting tiles
    for i in range(n):
        for j in range(n):
            # If the starting tile is not 0, continue
            if matrix[i][j] == 0:
                continue
            # Get the shortest distance from the starting tile to tile k
            distance = f1(n, k, matrix)
            # If the distance is less than the current shortest distance, update the shortest distance
            if distance < shortest_distance:
                shortest_distance = distance
    # Return the shortest distance
    return shortest_distance

if __name__ == '__main__':
    n, k = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    print(f2(n, k, matrix))

