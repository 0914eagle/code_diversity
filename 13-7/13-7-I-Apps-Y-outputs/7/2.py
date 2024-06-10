
def get_min_distance(key_points):
    # Sort the key points by their x-coordinate
    sorted_key_points = sorted(key_points, key=lambda x: x[0])

    # Initialize the minimum distance to 0
    min_distance = 0

    # Loop through the key points and calculate the distance to the next point
    for i in range(len(sorted_key_points) - 1):
        current_point = sorted_key_points[i]
        next_point = sorted_key_points[i + 1]
        distance = abs(current_point[0] - next_point[0]) + abs(current_point[1] - next_point[1])
        min_distance += distance

    return min_distance

def main():
    n = int(input())
    key_points = []
    for i in range(n):
        x, y = map(int, input().split())
        key_points.append((x, y))
    print(get_min_distance(key_points))

if __name__ == '__main__':
    main()

