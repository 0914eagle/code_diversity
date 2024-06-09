
import math

def get_triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def get_rod_length(triangles):
    areas = []
    for triangle in triangles:
        areas.append(get_triangle_area(*triangle))
    return 2 * max(areas)

def main():
    n = int(input())
    triangles = []
    for i in range(n):
        triangle = [int(x) for x in input().split()]
        triangles.append(triangle)
    print(get_rod_length(triangles))

if __name__ == '__main__':
    main()

