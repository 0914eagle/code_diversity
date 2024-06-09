
def f1(n, k, matrix):
    # Initialize a dictionary to store the distances from tile 1 to each other tile
    distances = {1: 0}
    
    # Loop through each tile in the matrix
    for i in range(n):
        for j in range(n):
            # If the current tile is not tile 1, check if it is reachable from tile 1
            if matrix[i][j] != 1:
                # Check if the current tile is reachable from any of the already visited tiles
                for visited_tile in distances:
                    # If the current tile is reachable from the visited tile, update the distance
                    if matrix[i][j] == visited_tile + 1:
                        distances[matrix[i][j]] = distances[visited_tile] + 1
                        break
    
    # Check if tile k is reachable from tile 1
    if k not in distances:
        return -1
    
    # Return the shortest distance from tile 1 to tile k
    return distances[k]

def f2(...):
    ...

if __name__ == '__main__':
    n, k = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    print(f1(n, k, matrix))

