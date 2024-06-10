
def get_white_area(rectangle, points):
    white_area = rectangle[0] * rectangle[1]
    for point, a in points:
        if a == 1:
            white_area -= (point[0] * rectangle[1])
        elif a == 2:
            white_area -= (rectangle[0] - point[0]) * rectangle[1]
        elif a == 3:
            white_area -= (point[1] * rectangle[0])
        else:
            white_area -= (rectangle[1] - point[1]) * rectangle[0]
    return white_area

def main():
    rectangle = list(map(int, input().split()))
    points = []
    for _ in range(int(input())):
        points.append(list(map(int, input().split())))
    print(get_white_area(rectangle, points))

if __name__ == '__main__':
    main()

