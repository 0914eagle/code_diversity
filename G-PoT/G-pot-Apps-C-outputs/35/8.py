
# Read input
R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]

# Find Joe's initial position
for i in range(R):
    for j in range(C):
        if maze[i][j] == 'J':
            joe_pos = (i, j)
            break

# Initialize variables
queue = [(joe_pos[0], joe_pos[1], 0)]
visited = set()
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# BFS to find the earliest time Joe can safely exit the maze
while queue:
    i, j, time = queue.pop(0)
    if (i == 0 or i == R-1 or j == 0 or j == C-1):
        print(time)
        break
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C and maze[ni][nj] != '#' and (ni, nj) not in visited:
            visited.add((ni, nj))
            queue.append((ni, nj, time + 1))

else:
    print("IMPOSSIBLE")
