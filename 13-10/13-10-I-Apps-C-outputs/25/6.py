
import math

def get_points(n):
    points = []
    for i in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    return points

def get_polygon_area(points):
    area = 0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def get_cut_line(A, B):
    x1, y1 = A[0]
    x2, y2 = A[1]
    x3, y3 = B[0]
    x4, y4 = B[1]
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None
    x = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
    x = x / denom
    y = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    y = y / denom
    return x, y

def get_cut_cost(A, B, line):
    area_A = get_polygon_area(A)
    area_B = get_polygon_area(B)
    x, y = line
    cost = 0
    for i in range(len(A)):
        x1, y1 = A[i]
        x2, y2 = A[(i + 1) % len(A)]
        if x1 == x2:
            continue
        if (x1 <= x <= x2 and y1 <= y <= y2) or (x1 >= x >= x2 and y1 >= y >= y2):
            cost += abs(x1 - x) + abs(y1 - y)
    return area_A - area_B + cost

def solve(A, B):
    min_cost = float('inf')
    for i in range(len(A)):
        line = get_cut_line(A[i:i+2], B)
        if line:
            cost = get_cut_cost(A, B, line)
            if cost < min_cost:
                min_cost = cost
    return min_cost

def main():
    A = get_points(int(input()))
    B = get_points(int(input()))
    print(solve(A, B))

if __name__ == '__main__':
    main()

