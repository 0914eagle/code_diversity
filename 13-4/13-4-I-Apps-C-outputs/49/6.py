
import math

def get_hexagon_circumference(vertices):
    # Calculate the circumference of the hexagon
    circumference = 0
    for i in range(len(vertices)):
        vertex1 = vertices[i]
        vertex2 = vertices[(i + 1) % len(vertices)]
        circumference += math.sqrt((vertex1[0] - vertex2[0]) ** 2 + (vertex1[1] - vertex2[1]) ** 2)
    return circumference

def get_max_hexagon_circumference(vertices):
    # Find the vertex with the maximum circumference
    max_circumference = 0
    max_vertex = 0
    for i in range(len(vertices)):
        vertex = vertices[i]
        circumference = get_hexagon_circumference([vertex] + vertices[(i + 1) % len(vertices):] + vertices[:i])
        if circumference > max_circumference:
            max_circumference = circumference
            max_vertex = i
    return max_circumference, max_vertex

def solve(n, vertices):
    # Find the vertex with the maximum circumference
    max_circumference, max_vertex = get_max_hexagon_circumference(vertices)
    
    # Print the maximum circumference for each vertex
    for i in range(n):
        if i == max_vertex:
            print(f"{max_circumference:.9f}")
        else:
            print(f"{get_hexagon_circumference([vertices[i]] + vertices[(i + 1) % n:] + vertices[:i]):.9f}")

if __name__ == "__main__":
    n = int(input())
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))
    solve(n, vertices)

