
import math

def get_center(p1, p2, p3, p4):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x3, y3, z3 = p3
    x4, y4, z4 = p4

    d1 = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    d2 = math.sqrt((x3-x1)**2 + (y3-y1)**2 + (z3-z1)**2)
    d3 = math.sqrt((x4-x1)**2 + (y4-y1)**2 + (z4-z1)**2)

    a = (d1**2 - d2**2 + d3**2)/(2*d1*d2)
    h = 2*math.sqrt(d1**2 - a**2)

    xc = (x1 + a*(x2-x1))/(d1 + h)
    yc = (y1 + a*(y2-y1))/(d1 + h)
    zc = (z1 + a*(z2-z1))/(d1 + h)

    return xc, yc, zc

def main():
    p1 = tuple(map(float, input().split()))
    p2 = tuple(map(float, input().split()))
    p3 = tuple(map(float, input().split()))
    p4 = tuple(map(float, input().split()))

    xc, yc, zc = get_center(p1, p2, p3, p4)
    print(xc, yc, zc)

if __name__ == '__main__':
    main()

