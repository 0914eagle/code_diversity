
def calculate_min_max_stops(n, k, a, b):
    min_stops = min(a, b) * n
    max_stops = min(n * k - max(a, b), n * k - min(a, b)) + 1
    return min_stops, max_stops

if __name__ == "__main__":
    n, k = map(int, input().split())
    a, b = map(int, input().split())
    x, y = calculate_min_max_stops(n, k, a, b)
    print(x, y)
