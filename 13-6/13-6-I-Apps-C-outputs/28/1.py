
def get_common_point(rectangles):
    x_coords = set()
    y_coords = set()
    for rect in rectangles:
        x1, y1, x2, y2 = rect
        x_coords.update([x1, x2])
        y_coords.update([y1, y2])
    for x in x_coords:
        for y in y_coords:
            count = 0
            for rect in rectangles:
                x1, y1, x2, y2 = rect
                if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                    count += 1
            if count >= len(rectangles) - 1:
                return x, y
    return None

def main():
    n = int(input())
    rectangles = []
    for i in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        rectangles.append((x1, y1, x2, y2))
    common_point = get_common_point(rectangles)
    if common_point:
        print(*common_point)
    else:
        print("No common point found.")

if __name__ == '__main__':
    main()

