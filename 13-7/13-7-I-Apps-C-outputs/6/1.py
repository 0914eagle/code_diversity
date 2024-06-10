
import math

def get_distance(x, y):
    return math.sqrt(x**2 + y**2)

def get_slanted_distance(x, y):
    return math.sqrt(x**2 + y**2) / math.fabs(y)

def get_closest_slanted_distance(contour_lines):
    closest_distance = float('inf')
    for line in contour_lines:
        for i in range(len(line) - 1):
            x1, y1 = line[i]
            x2, y2 = line[i + 1]
            distance = get_slanted_distance(x2 - x1, y2 - y1)
            if distance < closest_distance:
                closest_distance = distance
    return closest_distance

def main():
    n = int(input())
    contour_lines = []
    for i in range(n):
        outer_height, inner_height, num_vertices = map(int, input().split())
        contour_line = []
        for j in range(num_vertices):
            x, y = map(int, input().split())
            contour_line.append((x, y))
        contour_lines.append(contour_line)
    print(get_closest_slanted_distance(contour_lines))

if __name__ == '__main__':
    main()

