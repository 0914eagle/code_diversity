
import math

def get_triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def get_rod_length(triangle_list):
    area_list = []
    for a, b, c in triangle_list:
        area_list.append(get_triangle_area(a, b, c))
    return 2 * max(area_list)

def main():
    triangle_list = []
    for _ in range(int(input())):
        triangle_list.append(list(map(int, input().split())))
    print(get_rod_length(triangle_list))

if __name__ == '__main__':
    main()

