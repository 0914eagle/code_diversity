
import math

def get_hexagonal_wall(vertices):
    # Sort the vertices in clockwise order
    sorted_vertices = sorted(vertices, key=lambda x: math.atan2(x[1], x[0]))

    # Initialize the maximum circumference and the vertices of the hexagonal wall
    max_circumference = 0
    hexagonal_wall = []

    # Iterate over all possible combinations of 6 vertices
    for i in range(len(sorted_vertices)):
        for j in range(i+1, len(sorted_vertices)):
            for k in range(j+1, len(sorted_vertices)):
                for l in range(k+1, len(sorted_vertices)):
                    for m in range(l+1, len(sorted_vertices)):
                        for n in range(m+1, len(sorted_vertices)):
                            # Calculate the circumference of the hexagonal wall
                            circumference = get_circumference(sorted_vertices[i], sorted_vertices[j], sorted_vertices[k], sorted_vertices[l], sorted_vertices[m], sorted_vertices[n])

                            # Update the maximum circumference and the vertices of the hexagonal wall
                            if circumference > max_circumference:
                                max_circumference = circumference
                                hexagonal_wall = [sorted_vertices[i], sorted_vertices[j], sorted_vertices[k], sorted_vertices[l], sorted_vertices[m], sorted_vertices[n]]

    return hexagonal_wall

def get_circumference(v1, v2, v3, v4, v5, v6):
    # Calculate the side lengths of the hexagonal wall
    a = math.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)
    b = math.sqrt((v2[0] - v3[0]) ** 2 + (v2[1] - v3[1]) ** 2)
    c = math.sqrt((v3[0] - v4[0]) ** 2 + (v3[1] - v4[1]) ** 2)
    d = math.sqrt((v4[0] - v5[0]) ** 2 + (v4[1] - v5[1]) ** 2)
    e = math.sqrt((v5[0] - v6[0]) ** 2 + (v5[1] - v6[1]) ** 2)
    f = math.sqrt((v6[0] - v1[0]) ** 2 + (v6[1] - v1[1]) ** 2)

    # Calculate the circumference of the hexagonal wall
    circumference = a + b + c + d + e + f

    return circumference

def main():
    # Read the input
    n = int(input())
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))

    # Find the maximum circumference and the vertices of the hexagonal wall
    hexagonal_wall = get_hexagonal_wall(vertices)

    # Print the maximum circumference for each vertex
    for i in range(n):
        print(get_circumference(vertices[i], hexagonal_wall[0], hexagonal_wall[1], hexagonal_wall[2], hexagonal_wall[3], hexagonal_wall[4]))

if __name__ == "__main__":
    main()

