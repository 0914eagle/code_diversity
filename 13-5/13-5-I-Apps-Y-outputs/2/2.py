
import math

def get_points():
    return [tuple(map(float, input().split())) for _ in range(4)]

def get_angle(points):
    ab, bc, cd = [points[i] - points[i-1] for i in range(1, 4)]
    x = get_cross_product(ab, bc)
    y = get_cross_product(bc, cd)
    return math.degrees(math.acos(get_dot_product(x, y) / (get_magnitude(x) * get_magnitude(y))))

def get_dot_product(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

def get_cross_product(v1, v2):
    return (v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0])

def get_magnitude(v):
    return math.sqrt(sum(a * a for a in v))

if __name__ == '__main__':
    points = get_points()
    print(get_angle(points))

