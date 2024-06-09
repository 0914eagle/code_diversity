
def f1(n, m, S_x, S_y):
    # Initialize the visited matrix
    visited = [[False for _ in range(m)] for _ in range(n)]
    # Mark the starting cell as visited
    visited[S_x-1][S_y-1] = True
    # Initialize the queue with the starting cell
    queue = [(S_x, S_y)]
    # Loop through the queue
    while queue:
        # Get the current cell
        x, y = queue.pop(0)
        # If we have visited all cells, return the solution
        if all(all(row) for row in visited):
            return [[(i+1, j+1) for j, visited in enumerate(row) if visited] for i, row in enumerate(visited)]
        # Add the unvisited neighbors to the queue
        for i, j in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
            if 1 <= i <= n and 1 <= j <= m and not visited[i-1][j-1]:
                visited[i-1][j-1] = True
                queue.append((i, j))
    # If there is no solution, return an empty list
    return []

def f2(n, m, S_x, S_y):
    # Initialize the visited matrix
    visited = [[False for _ in range(m)] for _ in range(n)]
    # Mark the starting cell as visited
    visited[S_x-1][S_y-1] = True
    # Initialize the queue with the starting cell
    queue = [(S_x, S_y)]
    # Loop through the queue
    while queue:
        # Get the current cell
        x, y = queue.pop(0)
        # If we have visited all cells, return the solution
        if all(all(row) for row in visited):
            return [[(i+1, j+1) for j, visited in enumerate(row) if visited] for i, row in enumerate(visited)]
        # Add the unvisited neighbors to the queue
        for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 1 <= i <= n and 1 <= j <= m and not visited[i-1][j-1]:
                visited[i-1][j-1] = True
                queue.append((i, j))
    # If there is no solution, return an empty list
    return []

if __name__ == '__main__':
    n, m, S_x, S_y = map(int, input().split())
    print(f1(n, m, S_x, S_y))
    print(f2(n, m, S_x, S_y))

