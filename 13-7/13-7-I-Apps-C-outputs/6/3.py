
import math

def get_elevation_contour_lines(n):
    
    contour_lines = []
    for _ in range(n):
        outer_height, inner_height, num_vertices = map(int, input().split())
        contour_line = []
        for _ in range(num_vertices):
            x, y = map(int, input().split())
            contour_line.append((x, y))
        contour_lines.append(contour_line)
    return contour_lines

def get_closest_distance(contour_lines, target_point):
    
    min_distance = math.inf
    for contour_line in contour_lines:
        for i in range(len(contour_line) - 1):
            point1 = contour_line[i]
            point2 = contour_line[i + 1]
            distance = get_distance(point1, point2, target_point)
            if distance < min_distance:
                min_distance = distance
    return min_distance

def get_distance(point1, point2, target_point):
    
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = target_point
    if x1 == x2:
        return abs(y3 - y1)
    if y1 == y2:
        return abs(x3 - x1)
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1
    x = (y3 - c) / m
    y = m * x + c
    return math.sqrt((x - x3) ** 2 + (y - y3) ** 2)

def main():
    n = int(input())
    contour_lines = get_elevation_contour_lines(n)
    target_point = (0, 0)
    closest_distance = get_closest_distance(contour_lines, target_point)
    print(closest_distance)

if __name__ == '__main__':
    main()

