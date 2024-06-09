
# Read input
r, c = map(int, input().split())
start_bed, fridge = eval(input()), eval(input())
school_map = [input() for _ in range(r)]
p = int(input())
masters_paths = [list(map(eval, input().split())) for _ in range(p)]

# Initialize variables
INF = float('inf')
dp = [[INF] * c for _ in range(r)]
queue = [(start_bed[0]-1, start_bed[1]-1, 0)]
dp[start_bed[0]-1][start_bed[1]-1] = 0

# Perform BFS
while queue:
    x, y, time = queue.pop(0)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and school_map[nx][ny] == '.' and dp[nx][ny] == INF:
            dp[nx][ny] = time + 1
            queue.append((nx, ny, time + 1))

# Check if child can reach the fridge
if dp[fridge[0]-1][fridge[1]-1] == INF:
    print("IMPOSSIBLE")
else:
    print(dp[fridge[0]-1][fridge[1]-1])
