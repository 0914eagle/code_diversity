
import math

def get_vector_dot_product(vector1, vector2):
    return sum(a * b for a, b in zip(vector1, vector2))

def get_vector_magnitude(vector):
    return math.sqrt(sum(a * a for a in vector))

def get_plane_angle(point1, point2, point3):
    vector1 = [point2[0] - point1[0], point2[1] - point1[1], point2[2] - point1[2]]
    vector2 = [point3[0] - point2[0], point3[1] - point2[1], point3[2] - point2[2]]
    dot_product = get_vector_dot_product(vector1, vector2)
    magnitude1 = get_vector_magnitude(vector1)
    magnitude2 = get_vector_magnitude(vector2)
    cosine_angle = dot_product / (magnitude1 * magnitude2)
    return math.degrees(math.acos(cosine_angle))

def main():
    point1 = list(map(float, input().split()))
    point2 = list(map(float, input().split()))
    point3 = list(map(float, input().split()))
    print(get_plane_angle(point1, point2, point3))

if __name__ == '__main__':
    main()

