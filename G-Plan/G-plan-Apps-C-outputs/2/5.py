
def calculate_stops(n, k, a, b):
    min_stops = min(a // k, b // k)
    max_stops = min(n - min(a, b) // k, n)
    return min_stops + 1, max_stops * 2

if __name__ == "__main__":
    n, k = map(int, input().split())
    a, b = map(int, input().split())
    x, y = calculate_stops(n, k, a, b)
    print(x, y)
