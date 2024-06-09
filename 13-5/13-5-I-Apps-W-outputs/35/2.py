
def f1(n, m, S_x, S_y):
    # Initialize the visited matrix
    visited = [[False for _ in range(m)] for _ in range(n)]
    # Mark the starting cell as visited
    visited[S_x - 1][S_y - 1] = True
    # Initialize the queue with the starting cell
    queue = [(S_x, S_y)]
    # Loop through the queue
    while queue:
        # Get the current cell
        x, y = queue.pop(0)
        # If we have visited all cells, return the solution
        if all(all(row) for row in visited):
            return visited
        # If we have not visited all cells, find the next cell to visit
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 1 <= i <= n and 1 <= j <= m and not visited[i - 1][j - 1]:
                    visited[i - 1][j - 1] = True
                    queue.append((i, j))
    # If there is no solution, return an empty matrix
    return visited

def f2(n, m, S_x, S_y):
    # Initialize the visited matrix
    visited = [[False for _ in range(m)] for _ in range(n)]
    # Mark the starting cell as visited
    visited[S_x - 1][S_y - 1] = True
    # Initialize the queue with the starting cell
    queue = [(S_x, S_y)]
    # Loop through the queue
    while queue:
        # Get the current cell
        x, y = queue.pop(0)
        # If we have visited all cells, return the solution
        if all(all(row) for row in visited):
            return visited
        # If we have not visited all cells, find the next cell to visit
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 1 <= i <= n and 1 <= j <= m and not visited[i - 1][j - 1]:
                    visited[i - 1][j - 1] = True
                    queue.append((i, j))
    # If there is no solution, return an empty matrix
    return visited

if __name__ == '__main__':
    n, m, S_x, S_y = map(int, input().split())
    visited = f1(n, m, S_x, S_y)
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                print(i + 1, j + 1)

