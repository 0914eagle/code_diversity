
def solve(a, b, c, d, e, f):
    # Initialize variables
    sugar_water = 0
    sugar_dissolved = 0

    # Operation 1: Pour 100A grams of water into the beaker
    water_added = 100 * a
    sugar_water += water_added
    sugar_dissolved += e * water_added // 100

    # Operation 2: Pour 100B grams of water into the beaker
    water_added = 100 * b
    sugar_water += water_added
    sugar_dissolved += e * water_added // 100

    # Operation 3: Put C grams of sugar into the beaker
    sugar_added = c
    sugar_water += sugar_added
    sugar_dissolved += min(sugar_added, f - sugar_water)

    # Operation 4: Put D grams of sugar into the beaker
    sugar_added = d
    sugar_water += sugar_added
    sugar_dissolved += min(sugar_added, f - sugar_water)

    return sugar_water, sugar_dissolved

