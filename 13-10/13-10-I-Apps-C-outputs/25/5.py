
import math

def get_polygon_area(polygon):
    
    area = 0
    for i in range(len(polygon)):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i+1) % len(polygon)]
        area += x1*y2 - x2*y1
    return abs(area)/2

def get_line_intersection(line1, line2):
    
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]
    denom = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    x = (x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4 - y3*x4)
    y = (x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4 - y3*x4)
    return x/denom, y/denom

def get_cut_cost(polygon, line):
    
    area = get_polygon_area(polygon)
    intersect_point = get_line_intersection(line, polygon[0])
    return math.fabs(area - get_polygon_area([intersect_point] + polygon))

def solve(polygon1, polygon2):
    
    min_cost = float('inf')
    for i in range(len(polygon1)):
        line = [polygon1[i], polygon1[(i+1) % len(polygon1)]]
        intersect_point = get_line_intersection(line, polygon2[0])
        if intersect_point:
            cost = get_cut_cost(polygon1, line)
            if cost < min_cost:
                min_cost = cost
    return min_cost

if __name__ == '__main__':
    polygon1 = []
    polygon2 = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        polygon1.append((x, y))
    for _ in range(int(input())):
        x, y = map(int, input().split())
        polygon2.append((x, y))
    print(solve(polygon1, polygon2))

