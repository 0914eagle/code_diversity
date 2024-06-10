
def get_minimum_distance(n, p, distances):
    # Sort the distances in ascending order
    distances.sort()
    
    # Initialize the minimum distance to the car in front
    min_distance = distances[0]
    
    # Iterate through the distances and calculate the minimum distance needed to not use breaks
    for i in range(1, n):
        min_distance = max(min_distance, distances[i] - p * (i + 1))
    
    return min_distance

def main():
    n, p = map(int, input().split())
    distances = list(map(int, input().split()))
    print(get_minimum_distance(n, p, distances))

if __name__ == '__main__':
    main()

