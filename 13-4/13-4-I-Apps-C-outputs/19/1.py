
import math

def get_largest_corn_area(vertices, canal):
    
    # Sort the vertices by their x-coordinate
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Initialize the largest area and the current area
    largest_area = 0
    current_area = 0

    # Iterate through the vertices
    for i in range(len(sorted_vertices)):
        # Calculate the area of the current triangle
        current_area = get_triangle_area(sorted_vertices[i], sorted_vertices[(i+1)%len(sorted_vertices)], canal)

        # Update the largest area if necessary
        if current_area > largest_area:
            largest_area = current_area

    return largest_area

def get_triangle_area(vertex1, vertex2, canal):
    
    # Calculate the length of the sides of the triangle
    side1 = math.sqrt((vertex1[0] - vertex2[0])**2 + (vertex1[1] - vertex2[1])**2)
    side2 = math.sqrt((canal[0] - vertex1[0])**2 + (canal[1] - vertex1[1])**2)
    side3 = math.sqrt((canal[0] - vertex2[0])**2 + (canal[1] - vertex2[1])**2)

    # Calculate the semi-perimeter of the triangle
    semi_perimeter = (side1 + side2 + side3) / 2

    # Calculate the area of the triangle
    area = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))

    return area

def main():
    # Read the input
    num_vertices = int(input())
    vertices = []
    for i in range(num_vertices):
        x, y = map(int, input().split())
        vertices.append((x, y))
    x1, y1, x2, y2 = map(int, input().split())
    canal = ((x1, y1), (x2, y2))

    # Calculate the largest area of corn fields
    largest_area = get_largest_corn_area(vertices, canal)

    # Print the output
    print(largest_area)

if __name__ == '__main__':
    main()

