
import math

def get_angle(a, b, c, d):
    ab = [b[0] - a[0], b[1] - a[1], b[2] - a[2]]
    bc = [c[0] - b[0], c[1] - b[1], c[2] - b[2]]
    cd = [d[0] - c[0], d[1] - c[1], d[2] - c[2]]
    x = [0, 0, 0]
    y = [0, 0, 0]
    for i in range(3):
        x[i] = ab[i] * bc[i]
        y[i] = bc[i] * cd[i]
    x_dot_y = x[0] * y[0] + x[1] * y[1] + x[2] * y[2]
    x_magnitude = math.sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2)
    y_magnitude = math.sqrt(y[0] ** 2 + y[1] ** 2 + y[2] ** 2)
    cos_phi = x_dot_y / (x_magnitude * y_magnitude)
    phi = math.acos(cos_phi)
    return math.degrees(phi)

def main():
    a = list(map(float, input().split()))
    b = list(map(float, input().split()))
    c = list(map(float, input().split()))
    d = list(map(float, input().split()))
    angle = get_angle(a, b, c, d)
    print(angle)

if __name__ == '__main__':
    main()

