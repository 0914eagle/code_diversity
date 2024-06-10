
import math

def get_flaws_position(flaws):
    x_coords = [flaw[0] for flaw in flaws]
    y_coords = [flaw[1] for flaw in flaws]
    z_coords = [flaw[2] for flaw in flaws]
    return x_coords, y_coords, z_coords

def get_flaws_diameter(flaws):
    x_coords, y_coords, z_coords = get_flaws_position(flaws)
    diameters = []
    for flaw in flaws:
        diameter = math.sqrt(flaw[0]**2 + flaw[1]**2 + flaw[2]**2)
        diameters.append(diameter)
    return max(diameters)

def get_smallest_diameter_drill_bit(flaws):
    diameters = get_flaws_diameter(flaws)
    return diameters / 2

def main():
    num_flaws = int(input())
    flaws = []
    for _ in range(num_flaws):
        flaw = list(map(float, input().split()))
        flaws.append(flaw)
    print(get_smallest_diameter_drill_bit(flaws))

if __name__ == '__main__':
    main()

