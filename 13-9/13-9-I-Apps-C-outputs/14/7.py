
import math

def get_flaws_positions(n):
    flaws = []
    for i in range(n):
        flaws.append(list(map(float, input().split())))
    return flaws

def get_diameter(flaws):
    x_coords = [flaw[0] for flaw in flaws]
    y_coords = [flaw[1] for flaw in flaws]
    z_coords = [flaw[2] for flaw in flaws]
    max_distance = max(math.sqrt(x_coords[i]**2 + y_coords[i]**2 + z_coords[i]**2) for i in range(len(flaws)))
    return 2 * max_distance

def main():
    n = int(input())
    flaws = get_flaws_positions(n)
    diameter = get_diameter(flaws)
    print(diameter)

if __name__ == '__main__':
    main()

