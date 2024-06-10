
def get_white_area(rectangle):
    
    x1, y1, x2, y2 = rectangle
    return (x2 - x1) * (y2 - y1)

def main():
    w, h, n = map(int, input().split())
    points = []
    for _ in range(n):
        x, y, a = map(int, input().split())
        points.append((x, y, a))
    
    rectangle = (0, 0, w, h)
    for point in points:
        if point[2] == 1:
            rectangle = (rectangle[0], point[1], point[0], rectangle[3])
        elif point[2] == 2:
            rectangle = (point[0], rectangle[1], rectangle[2], rectangle[3])
        elif point[2] == 3:
            rectangle = (rectangle[0], rectangle[1], rectangle[2], point[1])
        else:
            rectangle = (rectangle[0], point[1], rectangle[2], rectangle[3])
    
    print(get_white_area(rectangle))

if __name__ == '__main__':
    main()

