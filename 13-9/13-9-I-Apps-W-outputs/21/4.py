
import math

def get_min_radius(points):
    x_coords, y_coords = zip(*points)
    x_avg, y_avg = sum(x_coords) / len(x_coords), sum(y_coords) / len(y_coords)
    distances = [math.sqrt((x - x_avg) ** 2 + (y - y_avg) ** 2) for x, y in points]
    return max(distances)

def main():
    points = []
    for _ in range(int(input())):
        points.append(tuple(map(int, input().split())))
    print(get_min_radius(points))

if __name__ == '__main__':
    main()

