
import math

def get_tunnel_cost(point1, point2):
    return math.fabs(point1[0] - point2[0]) + math.fabs(point1[1] - point2[1]) + math.fabs(point1[2] - point2[2])

def get_min_cost_tunnels(points):
    min_cost = 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            min_cost += get_tunnel_cost(points[i], points[j])
    return min_cost

def main():
    points = []
    for i in range(int(input())):
        points.append(list(map(int, input().split())))
    print(get_min_cost_tunnels(points))

if __name__ == '__main__':
    main()

