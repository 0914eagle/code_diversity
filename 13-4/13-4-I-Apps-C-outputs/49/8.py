
import math

def get_hexagon_circumference(vertices):
    # Calculate the distance between each pair of vertices
    distances = []
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            dx = vertices[i][0] - vertices[j][0]
            dy = vertices[i][1] - vertices[j][1]
            distances.append(math.sqrt(dx**2 + dy**2))
    
    # Sort the distances in descending order
    distances.sort(reverse=True)
    
    # Calculate the circumference of the hexagon
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
    
    circumferences = []
    for i in range(n):
        vertex = vertices[i]
        vertices_copy = vertices[:i] + vertices[i+1:]
        circumferences.append(get_hexagon_circumference(vertices_copy + [vertex]))
    
    for circumference in circumferences:
        print(circumference)

if __name__ == '__main__':
    main()

