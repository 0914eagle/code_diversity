
def calculate_stops(n, k, a, b):
    min_stops = max(1, (a + b + k - 1) // k)
    max_stops = min(n, (a + b + k - 1) // k + (a + b) // k)
    return min_stops, max_stops

if __name__ == "__main__":
    n, k = map(int, input().split())
    a, b = map(int, input().split())
    x, y = calculate_stops(n, k, a, b)
    print(x, y)
