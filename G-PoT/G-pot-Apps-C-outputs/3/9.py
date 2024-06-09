
def count_ways_to_paint(N, M, blue_params):
    total_ways = 1
    for i in range(N):
        total_ways *= (M - blue_params[i] - i)
        total_ways %= 100003
    return total_ways, total_ways % 100003

# Input
N, M = map(int, input().split())
blue_params = list(map(int, input().split()))

# Output
X, Y = count_ways_to_paint(N, M, blue_params)
print(X, Y)
