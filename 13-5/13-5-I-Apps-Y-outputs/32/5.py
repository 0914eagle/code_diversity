
import math

def get_triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def get_rod_length(triangles):
    areas = [get_triangle_area(a, b, c) for a, b, c in triangles]
    return max(areas) ** 2 / sum(areas)

def main():
    n = int(input())
    triangles = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        triangles.append((a, b, c))
    print(get_rod_length(triangles))

if __name__ == '__main__':
    main()

