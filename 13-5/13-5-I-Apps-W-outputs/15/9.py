
def is_regular_polygon(n, ang):
    import math
    return n >= 3 and all(math.isclose(ang, math.radians(180 / n)) for i in range(n))

def find_regular_polygon(ang):
    for n in range(3, 998244354):
        if is_regular_polygon(n, ang):
            return n
    return -1

if __name__ == '__main__':
    ang = int(input())
    print(find_regular_polygon(ang))

