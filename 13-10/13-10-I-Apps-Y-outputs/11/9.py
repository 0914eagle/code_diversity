
def get_minimum_distance(p, distances):
    # Sort the distances in ascending order
    distances.sort()
    
    # Initialize the minimum distance to the car directly in front
    min_distance = distances[0]
    
    # Loop through the distances and calculate the minimum distance needed to maintain constant speed
    for i in range(1, len(distances)):
        min_distance = max(min_distance, distances[i] - p * (i + 1))
    
    return min_distance

def main():
    n, p = map(int, input().split())
    distances = list(map(int, input().split()))
    print(get_minimum_distance(p, distances))

if __name__ == '__main__':
    main()

