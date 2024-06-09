
def f1(n, m, S_x, S_y):
    # Initialize the visited matrix
    visited = [[False for _ in range(m)] for _ in range(n)]
    # Mark the starting cell as visited
    visited[S_x-1][S_y-1] = True
    # Initialize the queue with the starting cell
    queue = [(S_x, S_y)]
    # Loop through the queue
    while queue:
        # Get the current cell from the queue
        x, y = queue.pop(0)
        # If we have visited all cells, return the solution
        if all(all(row) for row in visited):
            return visited
        # Get the neighbors of the current cell
        neighbors = get_neighbors(n, m, x, y)
        # Add the unvisited neighbors to the queue
        for neighbor in neighbors:
            if not visited[neighbor[0]-1][neighbor[1]-1]:
                visited[neighbor[0]-1][neighbor[1]-1] = True
                queue.append(neighbor)
    # If we reach this point, it means that there is no solution
    return []

def get_neighbors(n, m, x, y):
    # Get the neighbors of the current cell
    neighbors = [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
    # Filter the neighbors that are out of bounds
    neighbors = [neighbor for neighbor in neighbors if 1 <= neighbor[0] <= n and 1 <= neighbor[1] <= m]
    return neighbors

def f2(n, m, S_x, S_y):
    # Initialize the visited matrix
    visited = [[False for _ in range(m)] for _ in range(n)]
    # Mark the starting cell as visited
    visited[S_x-1][S_y-1] = True
    # Initialize the queue with the starting cell
    queue = [(S_x, S_y)]
    # Loop through the queue
    while queue:
        # Get the current cell from the queue
        x, y = queue.pop(0)
        # If we have visited all cells, return the solution
        if all(all(row) for row in visited):
            return visited
        # Get the neighbors of the current cell
        neighbors = get_neighbors(n, m, x, y)
        # Add the unvisited neighbors to the queue
        for neighbor in neighbors:
            if not visited[neighbor[0]-1][neighbor[1]-1]:
                visited[neighbor[0]-1][neighbor[1]-1] = True
                queue.append(neighbor)
    # If we reach this point, it means that there is no solution
    return []

if __name__ == '__main__':
    n, m, S_x, S_y = map(int, input().split())
    visited = f1(n, m, S_x, S_y)
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                print(i+1, j+1)

