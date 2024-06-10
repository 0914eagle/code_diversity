
import math

def calculate_area_of_right_triangle(AB, BC):
    return 0.5 * AB * BC

if __name__ == "__main__":
    AB, BC, CA = map(int, input().split())
    area = calculate_area_of_right_triangle(AB, BC)
    print(int(area))
