
def get_min_distance(distances, p):
    # Sort the distances in non-decreasing order
    sorted_distances = sorted(distances)

    # Initialize the minimum distance to the car in front
    min_distance = 0

    # Iterate through the distances and calculate the minimum distance needed to keep
    for i in range(len(sorted_distances)):
        distance = sorted_distances[i]
        min_distance = max(min_distance, distance + (i + 1) * p)

    return min_distance

def main():
    n, p = map(int, input().split())
    distances = list(map(int, input().split()))
    print(get_min_distance(distances, p))

if __name__ == '__main__':
    main()

