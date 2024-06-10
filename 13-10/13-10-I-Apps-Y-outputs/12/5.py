
def read_points():
    return [tuple(map(float, input().split())) for _ in range(4)]

def get_vectors(points):
    return [points[i] - points[i-1] for i in range(1, len(points))]

def get_dot_product(v1, v2):
    return sum(a*b for a, b in zip(v1, v2))

def get_cross_product(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0], v1[0]*v2[2] - v1[2]*v2[0], v1[1]*v2[2] - v1[2]*v2[1]

def get_angle(v1, v2):
    x = get_cross_product(v1, v2)
    y = get_dot_product(v1, v2)
    return math.degrees(math.acos(y/math.sqrt(get_dot_product(x, x))))

def main():
    points = read_points()
    vectors = get_vectors(points)
    print(get_angle(vectors[1], vectors[2]))

if __name__ == '__main__':
    main()

