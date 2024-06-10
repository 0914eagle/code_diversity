
import math

def get_flaws_center(flaws):
    x_coords = [flaw[0] for flaw in flaws]
    y_coords = [flaw[1] for flaw in flaws]
    z_coords = [flaw[2] for flaw in flaws]
    x_center = sum(x_coords) / len(flaws)
    y_center = sum(y_coords) / len(flaws)
    z_center = sum(z_coords) / len(flaws)
    return [x_center, y_center, z_center]

def get_flaws_radius(flaws, center):
    x_coords = [math.fabs(flaw[0] - center[0]) for flaw in flaws]
    y_coords = [math.fabs(flaw[1] - center[1]) for flaw in flaws]
    z_coords = [math.fabs(flaw[2] - center[2]) for flaw in flaws]
    radius = max(x_coords + y_coords + z_coords)
    return radius

def get_diameter(radius):
    return radius * 2

def get_smallest_diameter(flaws):
    center = get_flaws_center(flaws)
    radius = get_flaws_radius(flaws, center)
    diameter = get_diameter(radius)
    return diameter

def main():
    n = int(input())
    flaws = []
    for i in range(n):
        x, y, z = map(float, input().split())
        flaws.append([x, y, z])
    smallest_diameter = get_smallest_diameter(flaws)
    print(smallest_diameter)

if __name__ == '__main__':
    main()

