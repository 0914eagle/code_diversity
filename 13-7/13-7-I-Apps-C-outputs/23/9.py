
import math

def get_max_circumference(vertices):
    # Sort the vertices in counterclockwise order
    sorted_vertices = sorted(vertices, key=lambda v: math.atan2(v[1], v[0]))

    # Initialize the maximum circumference and the current vertex
    max_circumference = 0
    current_vertex = sorted_vertices[0]

    # Iterate through the vertices and calculate the circumference of the hexagon
    for vertex in sorted_vertices[1:]:
        # Calculate the length of the side of the hexagon
        side_length = math.sqrt((vertex[0] - current_vertex[0]) ** 2 + (vertex[1] - current_vertex[1]) ** 2)

        # Calculate the circumference of the hexagon
        circumference = 6 * side_length

        # Update the maximum circumference if necessary
        if circumference > max_circumference:
            max_circumference = circumference

        # Update the current vertex
        current_vertex = vertex

    return max_circumference

def main():
    n = int(input())
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))
    print(get_max_circumference(vertices))

if __name__ == "__main__":
    main()

