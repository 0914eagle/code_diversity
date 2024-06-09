
import math

def get_max_circumference(vertices):
    # Sort the vertices by their x-coordinates
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Initialize the maximum circumference and the corresponding hexagon
    max_circumference = 0
    hexagon = []

    # Iterate over the sorted vertices
    for i in range(len(sorted_vertices)):
        # Get the current vertex and its coordinates
        vertex = sorted_vertices[i]
        x, y = vertex[0], vertex[1]

        # Find the two vertices that form the line of the hexagon
        line_vertices = []
        for j in range(i - 1, -1, -1):
            line_vertex = sorted_vertices[j]
            line_vertices.append(line_vertex)
            if line_vertex[1] <= y:
                break

        for j in range(i + 1, len(sorted_vertices)):
            line_vertex = sorted_vertices[j]
            line_vertices.append(line_vertex)
            if line_vertex[1] <= y:
                break

        # Find the two vertices that form the hexagon
        hexagon_vertices = []
        for j in range(len(line_vertices)):
            line_vertex = line_vertices[j]
            if line_vertex[0] > x:
                hexagon_vertices.append(line_vertex)
                break
            hexagon_vertices.append(line_vertex)

        # Calculate the circumference of the hexagon
        circumference = 0
        for j in range(len(hexagon_vertices)):
            vertex1 = hexagon_vertices[j]
            vertex2 = hexagon_vertices[(j + 1) % len(hexagon_vertices)]
            dx = vertex2[0] - vertex1[0]
            dy = vertex2[1] - vertex1[1]
            distance = math.sqrt(dx**2 + dy**2)
            circumference += distance

        # Update the maximum circumference and the corresponding hexagon
        if circumference > max_circumference:
            max_circumference = circumference
            hexagon = hexagon_vertices

    return max_circumference, hexagon

def main():
    n = int(input())
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append([x, y])
    max_circumference, hexagon = get_max_circumference(vertices)
    print(max_circumference)

if __name__ == '__main__':
    main()

