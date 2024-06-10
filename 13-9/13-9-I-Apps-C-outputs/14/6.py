
def get_diameter(flaws):
    # Find the minimum and maximum x, y, and z coordinates of the flaws
    min_x = min(flaw[0] for flaw in flaws)
    max_x = max(flaw[0] for flaw in flaws)
    min_y = min(flaw[1] for flaw in flaws)
    max_y = max(flaw[1] for flaw in flaws)
    min_z = min(flaw[2] for flaw in flaws)
    max_z = max(flaw[2] for flaw in flaws)

    # Calculate the diameter of the cube
    diameter = max(max_x - min_x, max_y - min_y, max_z - min_z)

    return diameter

def main():
    num_flaws = int(input())
    flaws = []
    for i in range(num_flaws):
        x, y, z = input().split()
        flaws.append((float(x), float(y), float(z)))

    print(get_diameter(flaws))

if __name__ == '__main__':
    main()

