
def solve():
    N, K = map(int, input().split())
    heights = sorted([int(input()) for _ in range(N)])
    min_diff = float('inf')
    for i in range(N-K+1):
        max_height = heights[i+K-1]
        min_height = heights[i]
        diff = max_height - min_height
        min_diff = min(min_diff, diff)
    return min_diff

