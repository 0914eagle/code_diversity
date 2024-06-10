
def get_penalty(matrix, k, n, m):
    # Initialize the penalty to 0
    penalty = 0
    
    # Initialize a list to store the paths
    paths = []
    
    # Loop through each candy
    for i in range(k):
        # Find the shortest path for the candy
        path = find_shortest_path(matrix, n, m)
        
        # Add the path to the list of paths
        paths.append(path)
        
        # Update the matrix with the candy
        matrix[path[0][0]][path[0][1]] = i + 1
        
        # Update the penalty
        penalty += len(path)
    
    # Return the penalty and the list of paths
    return penalty, paths

def find_shortest_path(matrix, n, m):
    # Initialize a list to store the shortest path
    shortest_path = []
    
    # Loop through each cell in the matrix
    for i in range(n):
        for j in range(m):
            # If the cell is empty, find the shortest path to it
            if matrix[i][j] == 0:
                path = find_path(matrix, n, m, i, j)
                
                # If the path is shorter than the current shortest path, update the shortest path
                if len(path) < len(shortest_path) or len(shortest_path) == 0:
                    shortest_path = path
    
    # Return the shortest path
    return shortest_path

def find_path(matrix, n, m, i, j):
    # Initialize a list to store the path
    path = []
    
    # Loop through each cell in the matrix
    for x in range(n):
        for y in range(m):
            # If the cell is empty and is adjacent to the current cell, add it to the path
            if matrix[x][y] == 0 and (abs(x - i) + abs(y - j)) == 1:
                path.append((x, y))
    
    # Return the path
    return path

if __name__ == '__main__':
    # Get the input
    n, m, k = map(int, input().split())
    
    # Initialize the matrix
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    
    # Get the penalty and the paths
    penalty, paths = get_penalty(matrix, k, n, m)
    
    # Print the penalty
    print(penalty)
    
    # Print the paths
    for path in paths:
        print(' '.join(map(str, path)))

