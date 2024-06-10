
import math

def get_angle_between_planes(points):
    AB = points[1] - points[0]
    BC = points[2] - points[1]
    CD = points[3] - points[2]
    X = AB.cross(BC)
    Y = BC.cross(CD)
    return math.degrees(math.acos(X.dot(Y)/(X.norm()*Y.norm())))

def main():
    points = []
    for i in range(4):
        x, y, z = map(float, input().split())
        points.append([x, y, z])
    print(get_angle_between_planes(points))

if __name__ == '__main__':
    main()

