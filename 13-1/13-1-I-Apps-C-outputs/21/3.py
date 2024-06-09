
import sys
input = sys.stdin.read()
n, m = map(int, input.split())

volcanoes = set()
for i in range(m):
    x, y = map(int, input.split())
    volcanoes.add((x, y))

# Initialize the distance matrix with -1
distance = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

# Initialize the queue with the starting point
queue = [(1, 1)]

# Initialize the distance of the starting point to 0
distance[1][1] = 0

# Loop until the queue is empty
while queue:
    # Get the current cell from the queue
    x, y = queue.pop(0)
    
    # If the current cell is the destination, return the distance
    if x == n and y == n:
        return distance[x][y]
    
    # If the current cell is not a volcano, add its neighbors to the queue
    if (x, y) not in volcanoes:
        for dx, dy in [(0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= n and 1 <= ny <= n and distance[nx][ny] == -1:
                queue.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1

# If no path is found, return -1
return -1

