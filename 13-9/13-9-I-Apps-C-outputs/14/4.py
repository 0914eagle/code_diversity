
import math

def get_flaws_diameter(flaws):
    
    x_coords, y_coords, z_coords = zip(*flaws)
    x_max, x_min = max(x_coords), min(x_coords)
    y_max, y_min = max(y_coords), min(y_coords)
    z_max, z_min = max(z_coords), min(z_coords)
    diameter = max(x_max-x_min, y_max-y_min, z_max-z_min)
    return diameter

def get_flaws_center(flaws):
    
    x_coords, y_coords, z_coords = zip(*flaws)
    x_center = sum(x_coords) / len(flaws)
    y_center = sum(y_coords) / len(flaws)
    z_center = sum(z_coords) / len(flaws)
    return (x_center, y_center, z_center)

def get_flaws_distance(flaws, center):
    
    x_center, y_center, z_center = center
    distances = []
    for flaw in flaws:
        x, y, z = flaw
        distance = math.sqrt((x-x_center)**2 + (y-y_center)**2 + (z-z_center)**2)
        distances.append(distance)
    return max(distances)

def get_min_drill_diameter(flaws):
    
    center = get_flaws_center(flaws)
    distance = get_flaws_distance(flaws, center)
    return 2 * distance

def main():
    num_flaws = int(input())
    flaws = []
    for _ in range(num_flaws):
        flaws.append(tuple(map(float, input().split())))
    print(get_min_drill_diameter(flaws))

if __name__ == '__main__':
    main()

