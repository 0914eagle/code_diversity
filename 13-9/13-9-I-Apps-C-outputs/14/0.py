
import math

def get_flaws_center(flaws):
    x_coords = [flaw[0] for flaw in flaws]
    y_coords = [flaw[1] for flaw in flaws]
    z_coords = [flaw[2] for flaw in flaws]
    return (sum(x_coords) / len(flaws), sum(y_coords) / len(flaws), sum(z_coords) / len(flaws))

def get_flaws_radius(flaws, center):
    return max([math.sqrt((flaw[0] - center[0]) ** 2 + (flaw[1] - center[1]) ** 2 + (flaw[2] - center[2]) ** 2) for flaw in flaws])

def get_smallest_drill_bit(flaws):
    center = get_flaws_center(flaws)
    radius = get_flaws_radius(flaws, center)
    return 2 * radius

def main():
    num_flaws = int(input())
    flaws = []
    for i in range(num_flaws):
        flaws.append(tuple(map(float, input().split())))
    print(get_smallest_drill_bit(flaws))

if __name__ == '__main__':
    main()

