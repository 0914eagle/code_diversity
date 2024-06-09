
import math

def get_triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def get_rod_length(triangle_list):
    min_length = 0
    for triangle in triangle_list:
        a, b, c = triangle
        area = get_triangle_area(a, b, c)
        perimeter = a + b + c
        min_length += 2 * area / perimeter
    return min_length

def main():
    triangle_list = []
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        triangle_list.append((a, b, c))
    print(get_rod_length(triangle_list))

if __name__ == '__main__':
    main()

