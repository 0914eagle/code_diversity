
def get_min_time(a, b, n, taxi_coordinates):
    # Calculate the distance between Vasiliy's home and each taxi location
    distances = [(x - a) ** 2 + (y - b) ** 2 for x, y in taxi_coordinates]
    
    # Find the minimum distance and return the time it will take for the corresponding taxi to arrive
    return min(distances) ** 0.5 / max(v for x, y, v in taxi_coordinates)

def main():
    a, b = map(int, input().split())
    n = int(input())
    taxi_coordinates = [(int(x), int(y), int(v)) for _ in range(n) for x, y, v in [input().split()]]
    print(get_min_time(a, b, n, taxi_coordinates))

if __name__ == '__main__':
    main()

