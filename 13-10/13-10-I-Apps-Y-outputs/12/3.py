
import math

def get_points():
    return [tuple(map(float, input().split())) for _ in range(4)]

def get_vectors(points):
    return [points[i + 1] - points[i] for i in range(len(points) - 1)]

def get_cross_product(v1, v2):
    return (v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0])

def get_dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

def get_magnitude(v):
    return math.sqrt(get_dot_product(v, v))

def get_angle(v1, v2):
    return math.degrees(math.acos(get_dot_product(v1, v2) / (get_magnitude(v1) * get_magnitude(v2))))

def main():
    points = get_points()
    vectors = get_vectors(points)
    phi = get_angle(get_cross_product(vectors[0], vectors[1]), get_cross_product(vectors[1], vectors[2]))
    print(f"{phi:.2f}")

if __name__ == '__main__':
    main()

