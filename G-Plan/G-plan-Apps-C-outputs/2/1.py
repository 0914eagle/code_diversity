
def calculate_stops(n, k, a, b):
    x = min(a // k, b // k)
    y = min(n - x, (a + k - 1) // k + (b + k - 1) // k)
    return x, n * y

if __name__ == "__main__":
    n, k = map(int, input().split())
    a, b = map(int, input().split())
    x, y = calculate_stops(n, k, a, b)
    print(x, y)
