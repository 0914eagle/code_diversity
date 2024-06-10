
def get_optimal_platform_placement(points, platform_length):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])
    
    # Initialize the optimal solution with 0 points saved
    optimal_solution = 0
    
    # Iterate over the points and check if they can be saved by the current platform placement
    for i in range(len(sorted_points)):
        # Check if the point is within the current platform's range
        if sorted_points[i][0] >= platform_length:
            # If the point is not within the range, move the platform to the next point
            optimal_solution += 1
    
    return optimal_solution

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        print(get_optimal_platform_placement(points, k))

if __name__ == '__main__':
    main()

