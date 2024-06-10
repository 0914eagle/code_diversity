
import math

def calculate_area_of_right_triangle(ab, bc):
    return 0.5 * ab * bc

if __name__ == "__main__":
    ab, bc, ca = map(int, input().split())
    area = calculate_area_of_right_triangle(ab, bc)
    print(area)
