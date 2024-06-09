
import math

def count_ways_to_paint(N, M, c):
    total_ways = 1
    for i in range(N):
        total_ways *= (M - c[i] - i)
        total_ways %= 100003
    return total_ways

# Input
N, M = map(int, input().split())
c = list(map(int, input().split()))

# Calculate the number of ways to paint the picture
result = count_ways_to_paint(N, M, c)

# Output
X = 0
Y = result
Y_m = Y % 100003
print(X, Y_m)
