
import math

def get_hexagon_circumference(vertices):
    # Calculate the length of each side of the hexagon
    side_lengths = []
    for i in range(6):
        side_lengths.append(math.sqrt((vertices[i][0] - vertices[(i+1)%6][0])**2 + (vertices[i][1] - vertices[(i+1)%6][1])**2))
    
    # Calculate the circumference of the hexagon
    circumference = 0
    for side_length in side_lengths:
        circumference += side_length
    
    return circumference

def get_max_hexagon_circumference(vertices):
    max_circumference = 0
    for i in range(len(vertices)):
        hexagon_circumference = get_hexagon_circumference([vertices[i], vertices[(i+1)%6], vertices[(i+2)%6], vertices[(i+3)%6], vertices[(i+4)%6], vertices[(i+5)%6]])
        if hexagon_circumference > max_circumference:
            max_circumference = hexagon_circumference
    
    return max_circumference

n = int(input())
vertices = []
for i in range(n):
    x, y = map(int, input().split())
    vertices.append((x, y))

for i in range(n):
    print(get_max_hexagon_circumference([vertices[i], vertices[(i+1)%n], vertices[(i+2)%n], vertices[(i+3)%n], vertices[(i+4)%n], vertices[(i+5)%n]]))


