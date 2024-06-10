
def calculate_stops(n, k, a, b):
    min_stops = min(a // k, b // k)
    max_stops = min(n - a // k, n - b // k) + n * (k - max(a, b)) // k
    return min_stops + 1, max_stops + 1

if __name__ == "__main__":
    n, k = map(int, input().split())
    a, b = map(int, input().split())
    x, y = calculate_stops(n, k, a, b)
    print(x, y)
