
def get_flaw_locations(n_flaws):
    flaws = []
    for _ in range(n_flaws):
        x, y, z = map(float, input().split())
        flaws.append((x, y, z))
    return flaws

def get_diameter(flaws):
    x_coords, y_coords, z_coords = zip(*flaws)
    x_max, x_min = max(x_coords), min(x_coords)
    y_max, y_min = max(y_coords), min(y_coords)
    z_max, z_min = max(z_coords), min(z_coords)
    diameter = max(x_max-x_min, y_max-y_min, z_max-z_min)
    return diameter

def main():
    n_flaws = int(input())
    flaws = get_flaw_locations(n_flaws)
    diameter = get_diameter(flaws)
    print(diameter)

if __name__ == '__main__':
    main()

