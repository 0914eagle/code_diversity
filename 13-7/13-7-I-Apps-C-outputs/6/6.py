
import math

def get_distance_to_target(contour_lines):
    # Initialize the minimum distance to the target as a large value
    min_distance = 1000000
    # Loop through each contour line
    for contour in contour_lines:
        # Get the number of vertices in the contour
        num_vertices = len(contour) // 2
        # Loop through each vertex in the contour
        for i in range(num_vertices):
            # Get the coordinates of the current vertex
            x1, y1 = contour[2*i]
            x2, y2 = contour[2*i+1]
            # Calculate the distance from the current vertex to the target
            distance = math.sqrt((x1-0)**2 + (y1-0)**2)
            # Update the minimum distance if necessary
            if distance < min_distance:
                min_distance = distance
    # Return the minimum distance to the target
    return min_distance

def get_closest_slanted_distance(contour_lines):
    # Initialize the minimum slanted distance to the target as a large value
    min_slanted_distance = 1000000
    # Loop through each contour line
    for contour in contour_lines:
        # Get the number of vertices in the contour
        num_vertices = len(contour) // 2
        # Loop through each vertex in the contour
        for i in range(num_vertices):
            # Get the coordinates of the current vertex
            x1, y1 = contour[2*i]
            x2, y2 = contour[2*i+1]
            # Calculate the slanted distance from the current vertex to the target
            slanted_distance = math.sqrt((x1-0)**2 + (y1-0)**2) / math.sqrt((x2-x1)**2 + (y2-y1)**2)
            # Update the minimum slanted distance if necessary
            if slanted_distance < min_slanted_distance:
                min_slanted_distance = slanted_distance
    # Return the minimum slanted distance to the target
    return min_slanted_distance

def main():
    # Read the number of contour lines
    num_contour_lines = int(input())
    # Read the contour lines
    contour_lines = []
    for i in range(num_contour_lines):
        contour_line = input().split()
        contour_lines.append([int(x) for x in contour_line])
    # Get the distance to the target
    distance_to_target = get_distance_to_target(contour_lines)
    # Get the closest slanted distance to the target
    closest_slanted_distance = get_closest_slanted_distance(contour_lines)
    # Print the closest slanted distance to the target
    print(closest_slanted_distance)

if __name__ == '__main__':
    main()

