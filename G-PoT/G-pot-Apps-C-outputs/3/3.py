
# Read input
N, M = map(int, input().split())
blue_params = list(map(int, input().split()))

# Calculate the number of ways to create the painting
total_ways = 1
for i in range(N):
    total_ways *= (M - blue_params[i] - i - 1) % 100003

X = total_ways // 100003
Y = total_ways % 100003

print(X, Y)
