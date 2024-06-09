
# Read input
n, s, t, q = map(int, input().split())
hills = []
for _ in range(n):
    x, y, h = map(int, input().split())
    hills.append((x, y, h))
springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

# Function to calculate distance between two points
def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

# Initialize variables
INF = float('inf')
dp = [[INF] * n for _ in range(1 << t)]
for i in range(s):
    dp[1 << (i + t)][springs[i] - 1] = 0

# Dynamic programming to find minimum total length of aqueducts
for mask in range(1, 1 << (t + s)):
    for i in range(n):
        for j in range(n):
            if mask & (1 << j):
                dp[mask][i] = min(dp[mask][i], dp[mask ^ (1 << j)][j] + distance(hills[i], hills[j]))

# Find the minimum total length for supplying each town with fresh water
ans = min(dp[(1 << t) - 1][town - 1] for town in towns)

# Output the result
if ans >= INF:
    print("IMPOSSIBLE")
else:
    print("{:.6f}".format(ans))
