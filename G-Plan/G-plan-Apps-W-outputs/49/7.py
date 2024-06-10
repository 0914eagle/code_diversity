gn_floors(n, limits):
    result = [0] * n
    for i in range(n):
        result[i] = min(limits[i], limits[i-1] if i > 0 else float('inf'), limits[i+1] if i < n-1 else float('inf'))
    return result

if __name__ == '__main__':
    n = int(input())
    limits = list(map(int, input().split()))
    result = assign_floors(n, limits)
    print(*result