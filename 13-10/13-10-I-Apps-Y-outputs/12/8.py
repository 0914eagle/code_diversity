
def get_input():
    return list(map(float, input().split()))

def get_dot_product(x, y):
    return sum(x_i * y_i for x_i, y_i in zip(x, y))

def get_cross_product(x, y):
    return [x[1] * y[2] - x[2] * y[1],
            x[2] * y[0] - x[0] * y[2],
            x[0] * y[1] - x[1] * y[0]]

def get_magnitude(v):
    return (sum(x_i ** 2 for x_i in v)) ** 0.5

def get_angle(a, b, c):
    x = get_cross_product(b - a, c - b)
    y = get_cross_product(b - a, c - b)
    dot = get_dot_product(x, y)
    mag_x = get_magnitude(x)
    mag_y = get_magnitude(y)
    return math.degrees(math.acos(dot / (mag_x * mag_y)))

def main():
    a = get_input()
    b = get_input()
    c = get_input()
    d = get_input()
    print(get_angle(a, b, c))
    print(get_angle(b, c, d))

if __name__ == '__main__':
    main()

