
import math

def calculate_semiperimeter(sides):
    return sum(sides) / 2

def calculate_max_area(sides):
    s = calculate_semiperimeter(sides)
    area = math.sqrt((s - sides[0]) * (s - sides[1]) * (s - sides[2]) * (s - sides[3]))
    return round(area, 6)

if __name__ == '__main__':
    sides = list(map(int, input().split()))
    max_area = calculate_max_area(sides)
    print(max_area)
