
def get_min_time(a, b, n, coordinates, speeds):
    # Calculate the distance between Vasiliy's house and each taxi
    distances = [(abs(a - x) + abs(b - y)) / v for x, y, v in coordinates]
    
    # Return the minimum distance
    return min(distances)

def main():
    a, b = map(int, input().split())
    n = int(input())
    coordinates = []
    speeds = []
    
    for i in range(n):
        x, y, v = map(int, input().split())
        coordinates.append((x, y))
        speeds.append(v)
    
    print(get_min_time(a, b, n, coordinates, speeds))

if __name__ == '__main__':
    main()

