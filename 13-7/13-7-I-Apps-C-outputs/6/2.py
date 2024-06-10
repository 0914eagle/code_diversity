
import math

def get_input():
    N = int(input())
    contours = []
    for i in range(N):
        H_0, H_1, M = map(int, input().split())
        contours.append([H_0, H_1, M])
        points = []
        for j in range(M):
            x, y = map(int, input().split())
            points.append([x, y])
        contours[-1].append(points)
    return contours

def get_closest_distance(contours):
    # Find the contour with the highest inner height
    highest_contour = contours[0]
    for contour in contours:
        if contour[1] > highest_contour[1]:
            highest_contour = contour
    
    # Find the point on the highest contour with the minimum distance to the target point (0, 0)
    min_distance = math.inf
    min_point = None
    for point in highest_contour[2]:
        distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
        if distance < min_distance:
            min_distance = distance
            min_point = point
    
    # Find the angle between the line from the target point to the minimum point and the x-axis
    angle = math.atan2(min_point[1], min_point[0])
    
    # Find the distance from the target point to the minimum point along the line with the minimum angle
    distance = math.sqrt((min_point[0] - 0) ** 2 + (min_point[1] - 0) ** 2) * math.cos(angle)
    
    return distance

def main():
    contours = get_input()
    print(get_closest_distance(contours))

if __name__ == '__main__':
    main()

