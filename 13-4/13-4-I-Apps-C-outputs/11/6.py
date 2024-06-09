
import math

def get_input():
    n = int(input())
    fruits = []
    for i in range(n):
        x, y = map(float, input().split())
        fruits.append((x, y))
    return n, fruits

def get_slope(x1, y1, x2, y2):
    if x1 == x2:
        return None
    return (y2 - y1) / (x2 - x1)

def get_y_intercept(x1, y1, slope):
    if slope is None:
        return y1
    return y1 - slope * x1

def get_line_equation(x1, y1, x2, y2):
    slope = get_slope(x1, y1, x2, y2)
    y_intercept = get_y_intercept(x1, y1, slope)
    return slope, y_intercept

def get_line_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    slope1, y_intercept1 = get_line_equation(x1, y1, x2, y2)
    slope2, y_intercept2 = get_line_equation(x3, y3, x4, y4)
    if slope1 == slope2:
        return None
    x = (y_intercept2 - y_intercept1) / (slope1 - slope2)
    y = slope1 * x + y_intercept1
    return x, y

def get_circle_intersection(x, y, r):
    x1 = x - r
    y1 = y - r
    x2 = x + r
    y2 = y + r
    return x1, y1, x2, y2

def get_circle_center(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

def get_circle_radius(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) / 2

def get_circle_area(r):
    return math.pi * r ** 2

def get_circle_perimeter(r):
    return 2 * math.pi * r

def get_circle_intersection_area(x1, y1, x2, y2, x3, y3, x4, y4):
    x, y = get_line_intersection(x1, y1, x2, y2, x3, y3, x4, y4)
    if x is None:
        return 0
    r = get_circle_radius(x1, y1, x2, y2)
    area = get_circle_area(r)
    return area

def get_max_fruits(fruits):
    max_fruits = 0
    for i in range(len(fruits)):
        for j in range(i + 1, len(fruits)):
            x1, y1 = fruits[i]
            x2, y2 = fruits[j]
            area = get_circle_intersection_area(x1, y1, x2, y2, 0, 0, 0, 0)
            max_fruits = max(max_fruits, area)
    return max_fruits

def main():
    n, fruits = get_input()
    max_fruits = get_max_fruits(fruits)
    print(max_fruits)

if __name__ == '__main__':
    main()

