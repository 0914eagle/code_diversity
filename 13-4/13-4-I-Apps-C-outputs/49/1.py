
import math

def get_max_circumference(vertices):
    # Sort the vertices by their x-coordinate
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Initialize the maximum circumference and the corresponding hexagon
    max_circumference = 0
    hexagon = []

    # Iterate over the sorted vertices
    for i in range(len(sorted_vertices)):
        # Get the current vertex and its coordinates
        vertex = sorted_vertices[i]
        x, y = vertex[0], vertex[1]

        # Find the two vertices that form the diameter of the circle passing through the current vertex and the previous vertex
        prev_vertex = sorted_vertices[(i - 1) % len(sorted_vertices)]
        prev_x, prev_y = prev_vertex[0], prev_vertex[1]
        dx, dy = x - prev_x, y - prev_y
        a, b = -(dx + dy), dx - dy
        c = dx * dx + dy * dy

        # Find the coordinates of the two vertices that form the diameter
        root = math.sqrt(a * a - 4 * b * c)
        x1 = (a + root) / (2 * b)
        y1 = (-a - root) / (2 * b)
        x2 = (a - root) / (2 * b)
        y2 = (-a + root) / (2 * b)

        # Find the distance between the current vertex and the two vertices that form the diameter
        d1 = math.sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1))
        d2 = math.sqrt((x - x2) * (x - x2) + (y - y2) * (y - y2))

        # Find the circumference of the hexagon
        circumference = d1 + d2 + 2 * math.sqrt(2) * math.sin(math.acos((d1 * d1 + d2 * d2 - 2 * d1 * d2 * math.cos(math.acos(a / c))) / (2 * d1 * d2)))

        # Update the maximum circumference and the corresponding hexagon
        if circumference > max_circumference:
            max_circumference = circumference
            hexagon = [vertex, prev_vertex, (x1, y1), (x2, y2), (x2, y1), (x1, y2)]

    return max_circumference, hexagon

def main():
    n = int(input())
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))
    max_circumference, hexagon = get_max_circumference(vertices)
    print(max_circumference)

if __name__ == "__main__":
    main()

