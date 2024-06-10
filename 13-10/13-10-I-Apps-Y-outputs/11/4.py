
def get_minimum_distance(n, p, distances):
    # Initialize a list to store the minimum distance for each car
    min_distances = [float('inf')] * (n + 1)
    # Set the minimum distance for the car directly in front to 0
    min_distances[1] = 0
    
    # Iterate through the distances and calculate the minimum distance for each car
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j != i:
                min_distances[i] = min(min_distances[i], min_distances[j] + p * (distances[j] - distances[i]))
    
    # Return the minimum distance for the car directly in front
    return min_distances[1]

def main():
    n, p = map(int, input().split())
    distances = list(map(int, input().split()))
    print(get_minimum_distance(n, p, distances))

if __name__ == '__main__':
    main()

