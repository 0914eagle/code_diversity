
import math

def calculate_dot_product(vec1, vec2):
    return vec1[0]*vec2[0] + vec1[1]*vec2[1] + vec1[2]*vec2[2]

def calculate_cross_product(vec1, vec2):
    return [vec1[1]*vec2[2] - vec1[2]*vec2[1], vec1[2]*vec2[0] - vec1[0]*vec2[2], vec1[0]*vec2[1] - vec1[1]*vec2[0]]

def calculate_angle(vec1, vec2):
    dot_product = calculate_dot_product(vec1, vec2)
    magnitude_product = math.sqrt(calculate_dot_product(vec1, vec1)) * math.sqrt(calculate_dot_product(vec2, vec2))
    return math.degrees(math.acos(dot_product / magnitude_product))

def main():
    point_a = [float(x) for x in input().split()]
    point_b = [float(x) for x in input().split()]
    point_c = [float(x) for x in input().split()]
    point_d = [float(x) for x in input().split()]

    vec_ab = [point_b[i] - point_a[i] for i in range(3)]
    vec_bc = [point_c[i] - point_b[i] for i in range(3)]
    vec_cd = [point_d[i] - point_c[i] for i in range(3)]

    vec_ac = calculate_cross_product(vec_ab, vec_bc)
    vec_bd = calculate_cross_product(vec_bc, vec_cd)

    angle_abc = calculate_angle(vec_ac, vec_ab)
    angle_bcd = calculate_angle(vec_bd, vec_bc)

    print(f"The angle between the plane made by the points A, B, C and B, C, D is {angle_abc + angle_bcd:.2f} degrees.")

if __name__ == '__main__':
    main()

