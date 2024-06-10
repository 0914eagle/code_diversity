
from math import comb

def count_sets(n, points):
    y_counts = {}
    for x, y in points:
        if y in y_counts:
            y_counts[y] += 1
        else:
            y_counts[y] = 1
    
    total_sets = 1
    for count in y_counts.values():
        total_sets *= comb(n, count)
        n -= count
    
    return total_sets

if __name__ == "__main__":
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    result = count_sets(n, points)
    print(result)
