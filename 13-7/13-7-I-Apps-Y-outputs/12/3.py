
def get_white_area(rectangle, points):
    x1, y1, x2, y2 = rectangle
    white_area = (x2 - x1) * (y2 - y1)
    for point, a in points:
        if a == 1:
            white_area -= (point - x1) * (y2 - y1)
        elif a == 2:
            white_area -= (x2 - point) * (y2 - y1)
        elif a == 3:
            white_area -= (x2 - x1) * (point - y1)
        else:
            white_area -= (x2 - x1) * (y2 - point)
    return white_area

def main():
    rectangle = list(map(int, input().split()))
    points = []
    for i in range(int(input())):
        x, y, a = map(int, input().split())
        points.append((x, y, a))
    print(get_white_area(rectangle, points))

if __name__ == '__main__':
    main()

