
def calculate_stops(n, k, a, b):
    min_stops = 1
    max_stops = n * k
    return min_stops, max_stops

if __name__ == "__main__":
    n, k = map(int, input().split())
    a, b = map(int, input().split())
    
    min_stops, max_stops = calculate_stops(n, k, a, b)
    print(min_stops, max_stops)
