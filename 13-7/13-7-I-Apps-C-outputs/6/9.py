
import math

def get_distance_to_target(contour_lines):
    # Initialize the closest distance to a large value
    closest_distance = 1000000
    # Loop through each contour line
    for contour in contour_lines:
        # Get the coordinates of the contour line
        x_coords, y_coords = zip(*contour)
        # Calculate the length of the contour line
        contour_length = get_line_length(x_coords, y_coords)
        # Calculate the distance from the contour line to the target
        distance_to_target = get_distance_to_line(x_coords, y_coords, 0, 0)
        # Check if the distance to the target is closer than the current closest distance
        if distance_to_target < closest_distance:
            closest_distance = distance_to_target
    return closest_distance

def get_line_length(x_coords, y_coords):
    # Calculate the length of the line segment between the first and last point
    line_length = math.sqrt((x_coords[0] - x_coords[-1]) ** 2 + (y_coords[0] - y_coords[-1]) ** 2)
    return line_length

def get_distance_to_line(x_coords, y_coords, x, y):
    # Calculate the distance from the point (x, y) to the line defined by the contour line
    distance = abs((y - y_coords[0]) * (x_coords[-1] - x_coords[0]) - (x - x_coords[0]) * (y_coords[-1] - y_coords[0])) / get_line_length(x_coords, y_coords)
    return distance

def main():
    # Read the number of contour lines
    num_contour_lines = int(input())
    # Read the contour lines
    contour_lines = []
    for _ in range(num_contour_lines):
        contour_line = []
        height, num_vertices = map(int, input().split())
        for _ in range(num_vertices):
            x, y = map(int, input().split())
            contour_line.append((x, y))
        contour_lines.append(contour_line)
    # Calculate the closest distance to the target
    closest_distance = get_distance_to_target(contour_lines)
    # Print the result
    print(closest_distance)

if __name__ == '__main__':
    main()

