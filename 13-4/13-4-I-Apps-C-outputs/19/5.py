
def f1(n, x, y, x_a, y_a, x_b, y_b):
    # find the area of the polygon
    area = 0
    for i in range(n):
        area += x[i] * y[i+1] - x[i+1] * y[i]
    area = abs(area) / 2

    # find the area of the triangle formed by the two points and the midpoint of the canal
    x_mid = (x_a + x_b) / 2
    y_mid = (y_a + y_b) / 2
    triangle_area = abs(x_mid * y_a - x_a * y_mid + x_mid * y_b - x_b * y_mid + x_a * y_b - x_b * y_a) / 2

    # return the maximum area
    return max(area - triangle_area, 0)

def f2(...):
    # find the area of the polygon
    area = 0
    for i in range(n):
        area += x[i] * y[i+1] - x[i+1] * y[i]
    area = abs(area) / 2

    # find the area of the triangle formed by the two points and the midpoint of the canal
    x_mid = (x_a + x_b) / 2
    y_mid = (y_a + y_b) / 2
    triangle_area = abs(x_mid * y_a - x_a * y_mid + x_mid * y_b - x_b * y_mid + x_a * y_b - x_b * y_a) / 2

    # return the maximum area
    return max(area - triangle_area, 0)

if __name__ == '__main__':
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    x_a, y_a, x_b, y_b = map(int, input().split())
    print(f1(n, x, y, x_a, y_a, x_b, y_b))
    print(f2(n, x, y, x_a, y_a, x_b, y_b))

