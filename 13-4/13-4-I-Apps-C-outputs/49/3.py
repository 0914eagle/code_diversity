
import math

def get_max_circumference(vertices):
    # Calculate the distance between each pair of vertices
    distances = []
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            dx = vertices[i][0] - vertices[j][0]
            dy = vertices[i][1] - vertices[j][1]
            distances.append(math.sqrt(dx**2 + dy**2))
    
    # Sort the distances in descending order
    distances.sort(reverse=True)
    
    # Calculate the maximum circumference
    circumference = 0
    for i in range(6):
        circumference += distances[i]
    
    return circumference

def main():
    n = int(input())
    vertices = []
    for i in range(n):
        x, y = map(int, input().split())
        vertices.append((x, y))
    
    max_circumference = 0
    for i in range(n):
        vertex = vertices[i]
        vertices_copy = vertices[:i] + vertices[i+1:]
        circumference = get_max_circumference(vertices_copy + [vertex])
        if circumference > max_circumference:
            max_circumference = circumference
    
    print(max_circumference)

if __name__ == "__main__":
    main()

