
# Read input
N, M = map(int, input().split())
blue_params = list(map(int, input().split()))

# Calculate the number of ways to create the painting
total_ways = 1
for i in range(N):
    total_ways *= (M - blue_params[i] - i)
    total_ways %= 100003

X = total_ways // 100003
Y_m = total_ways % 100003

# Output the result
print(X, Y_m)
