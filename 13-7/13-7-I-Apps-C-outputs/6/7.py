
import math

def get_distance(x, y):
    return math.sqrt(x**2 + y**2)

def get_angle(x1, y1, x2, y2):
    return math.atan2(y2 - y1, x2 - x1)

def get_closest_distance(x, y, contour):
    min_distance = float('inf')
    for i in range(len(contour) - 1):
        x1, y1 = contour[i]
        x2, y2 = contour[i + 1]
        angle = get_angle(x1, y1, x2, y2)
        distance = get_distance(x - x1, y - y1)
        projection = distance * math.cos(angle)
        if projection < min_distance:
            min_distance = projection
    return min_distance

def get_closest_point(x, y, contour):
    min_distance = float('inf')
    closest_point = None
    for i in range(len(contour) - 1):
        x1, y1 = contour[i]
        x2, y2 = contour[i + 1]
        angle = get_angle(x1, y1, x2, y2)
        distance = get_distance(x - x1, y - y1)
        projection = distance * math.cos(angle)
        if projection < min_distance:
            min_distance = projection
            closest_point = (x1, y1)
    return closest_point

def get_closest_distance_to_target(contours):
    x, y = 0, 0
    min_distance = float('inf')
    for contour in contours:
        distance = get_closest_distance(x, y, contour)
        if distance < min_distance:
            min_distance = distance
    return min_distance

def get_closest_point_to_target(contours):
    x, y = 0, 0
    min_distance = float('inf')
    closest_point = None
    for contour in contours:
        point = get_closest_point(x, y, contour)
        distance = get_distance(x - point[0], y - point[1])
        if distance < min_distance:
            min_distance = distance
            closest_point = point
    return closest_point

def main():
    n = int(input())
    contours = []
    for i in range(n):
        height_out, height_in, num_vertices = map(int, input().split())
        contour = []
        for j in range(num_vertices):
            x, y = map(int, input().split())
            contour.append((x, y))
        contours.append(contour)
    print(get_closest_distance_to_target(contours))
    print(get_closest_point_to_target(contours))

if __name__ == '__main__':
    main()

