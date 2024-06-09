
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
    # Get the current cell
    x, y = queue.pop(0)
    
    # If the current cell is the destination, return the distance
    if x == n and y == n:
        return distance[x][y]
    
    # If the current cell is not a volcano, add its neighbors to the queue
    if (x, y) not in volcanoes:
        # Down neighbor
        if x + 1 <= n:
            queue.append((x + 1, y))
            distance[x + 1][y] = distance[x][y] + 1
        
        # Right neighbor
        if y + 1 <= n:
            queue.append((x, y + 1))
            distance[x][y + 1] = distance[x][y] + 1

# If the destination is not reachable, return -1
print(-1)

