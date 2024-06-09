
import math

def count_ways_to_paint(N, M, blue_params):
    total_ways = 1
    
    for i in range(N):
        total_ways *= (M - blue_params[i] - i)
    
    X = total_ways // 100003
    Y = total_ways % 100003
    
    return X, Y

# Read input
N, M = map(int, input().split())
blue_params = list(map(int, input().split()))

# Calculate and output result
X, Y = count_ways_to_paint(N, M, blue_params)
print(X, Y)
