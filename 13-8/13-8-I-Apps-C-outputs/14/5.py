
def read_points():
    points = []
    for i in range(4):
        x, y, z = map(float, input().split())
        points.append((x, y, z))
    return points

def find_center(points):
    point_a, point_b, point_c, point_d = points
    v1 = [point_b[i] - point_a[i] for i in range(3)]
    v2 = [point_c[i] - point_a[i] for i in range(3)]
    v3 = [point_d[i] - point_a[i] for i in range(3)]
    n1 = [v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0]]
    n2 = [v2[1] * v3[2] - v2[2] * v3[1], v2[2] * v3[0] - v2[0] * v3[2], v2[0] * v3[1] - v2[1] * v3[0]]
    n3 = [v3[1] * n1[2] - v3[2] * n1[1], v3[2] * n1[0] - v3[0] * n1[2], v3[0] * n1[1] - v3[1] * n1[0]]
    denom = n1[0] * n2[1] * n3[2] + n1[1] * n2[2] * n3[0] + n1[2] * n2[0] * n3[1] - n1[2] * n2[1] * n3[0] - n1[1] * n2[0] * n3[2] - n1[0] * n2[2] * n3[1]
    center = [(-n1[1] * n2[2] * point_a[0] + n1[1] * n2[0] * point_a[2] + n1[2] * n2[1] * point_a[0] - n1[2] * n2[0] * point_a[1] - n1[0] * n2[1] * point_a[2] + n1[0] * n2[2] * point_a[1]) / denom,
              (-n1[2] * n2[0] * point_a[1] + n1[2] * n2[1] * point_a[0] + n1[0] * n2[2] * point_a[1] - n1[0] * n2[1] * point_a[2] - n1[1] * n2[2] * point_a[0] + n1[1] * n2[0] * point_a[2]) / denom,
              (-n1[0] * n2[1] * point_a[2] + n1[0] * n2[2] * point_a[1] + n1[1] * n2[0] * point_a[2] - n1[1] * n2[2] * point_a[0] - n1[2] * n2[0] * point_a[1] + n1[2] * n2[1] * point_a[0]) / denom]
    return center

def main():
    points = read_points()
    center = find_center(points)
    print(center[0], center[1], center[2])

if __name__ == '__main__':
    main()

