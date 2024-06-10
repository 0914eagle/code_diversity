
def get_sugar_water(A, B, C, D, E, F):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Operation 1: Pour 100A grams of water into the beaker
    water_100A = 100 * A
    if water_100A <= F:
        sugar_water += water_100A
        F -= water_100A

    # Operation 2: Pour 100B grams of water into the beaker
    water_100B = 100 * B
    if water_100B <= F:
        sugar_water += water_100B
        F -= water_100B

    # Operation 3: Put C grams of sugar into the beaker
    sugar_C = C
    if sugar_C <= F:
        sugar_water += sugar_C
        F -= sugar_C
        sugar_dissolved += min(E, sugar_C)

    # Operation 4: Put D grams of sugar into the beaker
    sugar_D = D
    if sugar_D <= F:
        sugar_water += sugar_D
        F -= sugar_D
        sugar_dissolved += min(E, sugar_D)

    return sugar_water, sugar_dissolved

def main():
    A, B, C, D, E, F = map(int, input().split())
    sugar_water, sugar_dissolved = get_sugar_water(A, B, C, D, E, F)
    print(sugar_water, sugar_dissolved)

if __name__ == '__main__':
    main()

