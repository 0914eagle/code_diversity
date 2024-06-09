
def is_loop_possible(points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Create a dictionary to keep track of the points that have been visited
    visited = {}

    # Initialize the current point to be the first point in the list
    current_point = sorted_points[0]

    # Loop through the points and check if they can be connected to form a loop
    for i in range(1, len(sorted_points)):
        # Get the next point in the list
        next_point = sorted_points[i]

        # Check if the next point is already visited
        if next_point in visited:
            # If it is visited, return False
            return False

        # Check if the next point is aligned with the current point
        if current_point[0] == next_point[0] or current_point[1] == next_point[1]:
            # If it is aligned, mark it as visited and set it as the current point
            visited[next_point] = True
            current_point = next_point
        else:
            # If it is not aligned, return False
            return False

    # If all points have been visited and we have formed a loop, return True
    return True

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Loop through the test cases
    for test_case in range(num_test_cases):
        # Read the number of points
        num_points = int(input())

        # Initialize a list to store the points
        points = []

        # Loop through the points and read their coordinates
        for i in range(num_points):
            x, y = map(int, input().split())
            points.append((x, y))

        # Check if it is possible to form a loop with the given points
        if is_loop_possible(points):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()

