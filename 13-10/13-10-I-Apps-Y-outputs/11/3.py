
def get_minimum_distance(p, distances):
    # Sort the distances in non-decreasing order
    distances.sort()
    
    # Initialize the minimum distance to the car in front
    min_distance = 0
    
    # Iterate through the distances and calculate the minimum distance needed
    for i in range(len(distances)):
        min_distance += (p * (i + 1))
        min_distance = max(min_distance, distances[i])
    
    return min_distance

def main():
    n, p = map(int, input().split())
    distances = list(map(int, input().split()))
    print(get_minimum_distance(p, distances))

if __name__ == '__main__':
    main()

