
def get_max_circumference(vertices):
    # Sort the vertices by their x-coordinate
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Initialize the maximum circumference and the current circumference
    max_circumference = 0
    current_circumference = 0

    # Iterate through the vertices
    for i in range(len(sorted_vertices)):
        # Calculate the distance between the current vertex and the next vertex in the sorted list
        distance = get_distance(sorted_vertices[i], sorted_vertices[(i + 1) % len(sorted_vertices)])

        # Add the distance to the current circumference
        current_circumference += distance

        # If the current circumference is greater than the maximum circumference, update the maximum circumference
        if current_circumference > max_circumference:
            max_circumference = current_circumference

    # Return the maximum circumference
    return max_circumference

def get_distance(vertex1, vertex2):
    # Calculate the distance between the two vertices
    distance = ((vertex1[0] - vertex2[0]) ** 2 + (vertex1[1] - vertex2[1]) ** 2) ** 0.5

    # Return the distance
    return distance

def main():
    # Read the number of vertices
    n = int(input())

    # Read the vertices
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append([x, y])

    # Find the maximum circumference
    max_circumference = get_max_circumference(vertices)

    # Print the maximum circumference
    print(max_circumference)

if __name__ == '__main__':
    main()

