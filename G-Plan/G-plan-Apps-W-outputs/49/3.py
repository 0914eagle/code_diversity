_optimal_heights(n, limits):
    heights = [0] * n
    for i in range(n):
        heights[i] = min(limits[i], limits[i - 1] if i > 0 else float('inf'), limits[i + 1] if i < n - 1 else float('inf'))
    return heights

if __name__ == '__main__':
    n = int(input())
    limits = list(map(int, input().split()))
    result = find_optimal_heights(n, limits)
    print(*result