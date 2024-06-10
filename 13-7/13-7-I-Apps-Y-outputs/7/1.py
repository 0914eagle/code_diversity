
def get_min_distance(points):
    # Sort the points by their x-coordinate
    points.sort(key=lambda x: x[0])
    
    # Initialize the minimum distance to 0
    min_distance = 0
    
    # Iterate through the points and calculate the distance between them
    for i in range(len(points) - 1):
        min_distance += abs(points[i + 1][0] - points[i][0]) + abs(points[i + 1][1] - points[i][1])
    
    return min_distance

def main():
    n = int(input())
    points = []
    
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    
    print(get_min_distance(points))

if __name__ == '__main__':
    main()

