
def get_sugar_water_density(a, b, e):
    return (100 * b) / (a + b)

def get_max_sugar_water(a, b, c, d, e, f):
    max_sugar_water = 0
    max_sugar_dissolved = 0
    for sugar_water in range(a, b + 1):
        for sugar_dissolved in range(c, d + 1):
            if sugar_water * e >= sugar_dissolved and sugar_water + sugar_dissolved <= f:
                density = get_sugar_water_density(a, sugar_water, e)
                if density > max_sugar_water:
                    max_sugar_water = density
                    max_sugar_dissolved = sugar_dissolved
    return max_sugar_water, max_sugar_dissolved

def main():
    a, b, c, d, e, f = map(int, input().split())
    max_sugar_water, max_sugar_dissolved = get_max_sugar_water(a, b, c, d, e, f)
    print(max_sugar_water, max_sugar_dissolved)

if __name__ == '__main__':
    main()

