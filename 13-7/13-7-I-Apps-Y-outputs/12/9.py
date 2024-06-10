
def get_white_area(width, height, points):
    white_area = width * height
    for point, a in points:
        if a == 1:
            white_area -= point * height
        elif a == 2:
            white_area -= (width - point) * height
        elif a == 3:
            white_area -= width * (height - point)
        else:
            white_area -= width * point
    return white_area

def main():
    width, height, num_points = map(int, input().split())
    points = []
    for _ in range(num_points):
        x, y, a = map(int, input().split())
        points.append((x, y, a))
    print(get_white_area(width, height, points))

if __name__ == '__main__':
    main()

