
import math

def read_input():
    points = []
    for i in range(4):
        x, y, z = map(float, input().split())
        points.append((x, y, z))
    return points

def get_center(points):
    p1, p2, p3, p4 = points
    a1, a2, a3 = p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]
    b1, b2, b3 = p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]
    c1, c2, c3 = p4[0] - p1[0], p4[1] - p1[1], p4[2] - p1[2]
    d1 = a2*b3 - a3*b2
    d2 = a3*b1 - a1*b3
    d3 = a1*b2 - a2*b1
    x = (d1*(b2*c3 - b3*c2) + d2*(b3*c1 - b1*c3) + d3*(b1*c2 - b2*c1))/(2*(a1*d1 + a2*d2 + a3*d3))
    y = (d1*(c2*a3 - c3*a2) + d2*(c3*a1 - c1*a3) + d3*(c1*a2 - c2*a1))/(2*(b1*d1 + b2*d2 + b3*d3))
    z = (d1*(a2*b3 - a3*b2) + d2*(a3*b1 - a1*b3) + d3*(a1*b2 - a2*b1))/(2*(c1*d1 + c2*d2 + c3*d3))
    return x, y, z

def get_distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 + (point1[2]-point2[2])**2)

def compare_distance(point1, point2, point3):
    return get_distance(point1, point2) < get_distance(point1, point3)

def main():
    points = read_input()
    center = get_center(points)
    distances = [get_distance(center, point) for point in points]
    sorted_distances = sorted(distances)
    print(center)
    print(sorted_distances)

if __name__ == '__main__':
    main()

