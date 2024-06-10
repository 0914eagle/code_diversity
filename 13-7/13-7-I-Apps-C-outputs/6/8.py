
import math

def get_closest_distance(contour_lines):
    # Initialize the closest distance to a large value
    closest_distance = 1000000
    
    # Iterate over the contour lines
    for line in contour_lines:
        # Get the coordinates of the line
        x_coords, y_coords = line[0::2], line[1::2]
        
        # Calculate the length of the line
        line_length = math.sqrt((x_coords[0] - x_coords[-1]) ** 2 + (y_coords[0] - y_coords[-1]) ** 2)
        
        # Calculate the distance from the line to the target
        distance = math.sqrt((x_coords[0] - 0) ** 2 + (y_coords[0] - 0) ** 2)
        
        # If the distance is closer than the current closest distance, update the closest distance
        if distance < closest_distance:
            closest_distance = distance
    
    return closest_distance

def get_input():
    # Read the number of contour lines
    n = int(input())
    
    # Initialize an empty list to store the contour lines
    contour_lines = []
    
    # Iterate over the number of contour lines
    for i in range(n):
        # Read the height of the land outside and inside the contour, and the number of vertices
        h0, h1, m = map(int, input().split())
        
        # Initialize an empty list to store the coordinates of the contour
        line = []
        
        # Iterate over the number of vertices
        for j in range(m):
            # Read the x and y coordinates of the vertex
            x, y = map(int, input().split())
            
            # Add the coordinates to the list
            line.append(x)
            line.append(y)
        
        # Add the contour line to the list of contour lines
        contour_lines.append(line)
    
    return contour_lines

if __name__ == '__main__':
    # Get the input
    contour_lines = get_input()
    
    # Calculate the closest distance to the target
    closest_distance = get_closest_distance(contour_lines)
    
    # Print the result
    print(closest_distance)

