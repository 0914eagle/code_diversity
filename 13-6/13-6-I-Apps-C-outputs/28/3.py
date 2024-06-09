
def find_common_point(rectangles):
    x_coords = set()
    y_coords = set()
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        x_coords.update([x1, x2])
        y_coords.update([y1, y2])
    for x in x_coords:
        for y in y_coords:
            if all([rectangle_contains(rect, x, y) for rect in rectangles]):
                return x, y
    return None

def rectangle_contains(rect, x, y):
    x1, y1, x2, y2 = rect
    return x1 <= x <= x2 and y1 <= y <= y2

def main():
    n = int(input())
    rectangles = []
    for i in range(n):
        rectangles.append(tuple(map(int, input().split())))
    point = find_common_point(rectangles)
    if point:
        print(*point)
    else:
        print("No common point found.")

if __name__ == '__main__':
    main()

