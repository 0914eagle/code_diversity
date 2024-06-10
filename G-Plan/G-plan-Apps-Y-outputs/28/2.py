
import math

def calculate_area(AB, BC):
    return 0.5 * AB * BC

if __name__ == "__main__":
    AB, BC, CA = map(int, input().split())
    area = calculate_area(AB, BC)
    print(int(area))
