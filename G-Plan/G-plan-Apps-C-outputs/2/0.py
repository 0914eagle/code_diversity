
def calculate_stops(n, k, a, b):
    min_stops = min(a // k, b // k)
    max_stops = min(n - min_stops, (k - a + k - b - 1) // k + min_stops)
    return min_stops + 1, max_stops * n + min_stops

if __name__ == "__main__":
    n, k = map(int, input().split())
    a, b = map(int, input().split())
    x, y = calculate_stops(n, k, a, b)
    print(x, y)
