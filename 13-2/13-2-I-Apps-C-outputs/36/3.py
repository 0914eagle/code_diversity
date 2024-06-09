
import math

def get_water_height(vertices, depth, liters):
    # Calculate the area of the polygon
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i+1)%len(vertices)]
        area += x1*y2 - x2*y1
    area = abs(area) / 2

    # Calculate the volume of the tank
    volume = area * depth

    # Calculate the height of the water
    height = (liters * 1000) / volume

    return height

vertices = [(20, 0), (100, 0), (100, 40), (20, 40)]
depth = 30
liters = 50

print(f"{get_water_height(vertices, depth, liters):.2f}")

