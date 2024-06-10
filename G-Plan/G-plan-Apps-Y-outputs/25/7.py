
import math

def semiperimeter(sides):
    return sum(sides) / 2

def max_quadrilateral_area(sides):
    s = semiperimeter(sides)
    area = math.sqrt((s - sides[0]) * (s - sides[1]) * (s - sides[2]) * (s - sides[3]))
    return round(area, 6)

if __name__ == "__main__":
    sides = list(map(int, input().split()))
    print(max_quadrilateral_area(sides))
