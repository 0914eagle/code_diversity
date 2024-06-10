
def optimize_skyscrapers(n, limits):
    heights = [0] * n
    for i in range(n):
        heights[i] = min(limits[i], max(heights[i-1], heights[i+1] if i < n-1 else 0))
    return heights

if __name__ == '__main__':
    n = int(input())
    limits = list(map(int, input().split()))
    result = optimize_skyscrapers(n, limits)
    print(*result)
