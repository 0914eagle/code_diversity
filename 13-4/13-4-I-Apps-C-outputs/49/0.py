
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
    
    # Calculate the maximum circumference of the hexagon
    max_circumference = 0
    for i in range(len(distances)):
        for j in range(i+1, len(distances)):
            for k in range(j+1, len(distances)):
                circumference = distances[i] + distances[j] + distances[k]
                if circumference > max_circumference:
                    max_circumference = circumference
    
    return max_circumference

n = int(input())
vertices = []
for i in range(n):
    x, y = map(int, input().split())
    vertices.append((x, y))

print(get_max_circumference(vertices))

