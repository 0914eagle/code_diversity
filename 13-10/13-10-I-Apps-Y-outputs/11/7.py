
def get_minimum_distance(n, p, distances):
    # Sort the distances in ascending order
    sorted_distances = sorted(distances)

    # Initialize the minimum distance to the car directly in front
    min_distance = 0

    # Iterate through the distances and calculate the minimum distance required
    for i in range(n):
        min_distance += sorted_distances[i] + p * (i + 1)

    return min_distance

def main():
    n, p = map(int, input().split())
    distances = list(map(int, input().split()))
    print(get_minimum_distance(n, p, distances))

if __name__ == '__main__':
    main()

