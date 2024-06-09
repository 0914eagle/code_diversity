
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
    
    # Calculate the maximum circumference by summing the distances of the 6 longest edges
    max_circumference = 0
    for i in range(6):
        max_circumference += distances[i]
    
    return max_circumference

n = int(input())
vertices = []
for i in range(n):
    x, y = map(int, input().split())
    vertices.append((x, y))

for i in range(n):
    print(get_max_circumference(vertices[i:i+1] + vertices[:i] + vertices[i+1:]))

