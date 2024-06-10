
import math

def get_points():
    points = []
    for i in range(4):
        x, y, z = map(float, input().split())
        points.append((x, y, z))
    return points

def get_center(points):
    x1, y1, z1 = points[0]
    x2, y2, z2 = points[1]
    x3, y3, z3 = points[2]
    x4, y4, z4 = points[3]

    a1 = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
    b1 = 2 * ((x2 - x1) * (x3 - x1) + (y2 - y1) * (y3 - y1) + (z2 - z1) * (z3 - z1))
    c1 = (x3 - x1)**2 + (y3 - y1)**2 + (z3 - z1)**2

    a2 = (x3 - x1)**2 + (y3 - y1)**2 + (z3 - z1)**2
    b2 = 2 * ((x3 - x1) * (x4 - x1) + (y3 - y1) * (y4 - y1) + (z3 - z1) * (z4 - z1))
    c2 = (x4 - x1)**2 + (y4 - y1)**2 + (z4 - z1)**2

    a3 = (x4 - x1)**2 + (y4 - y1)**2 + (z4 - z1)**2
    b3 = 2 * ((x4 - x1) * (x2 - x1) + (y4 - y1) * (y2 - y1) + (z4 - z1) * (z2 - z1))
    c3 = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2

    delta1 = b1**2 - 4 * a1 * c1
    delta2 = b2**2 - 4 * a2 * c2
    delta3 = b3**2 - 4 * a3 * c3

    if delta1 < 0 or delta2 < 0 or delta3 < 0:
        return None

    xc = (b1 * c2 - b2 * c1) / (a1 * c2 - a2 * c1)
    yc = (a1 * b2 - a2 * b1) / (a1 * c2 - a2 * c1)
    zc = (c1 * b2 - c2 * b1) / (a1 * c2 - a2 * c1)

    return (xc, yc, zc)

def main():
    points = get_points()
    center = get_center(points)
    if center is not None:
        print(center[0], center[1], center[2])
    else:
        print("No center found")

if __name__ == '__main__':
    main()

