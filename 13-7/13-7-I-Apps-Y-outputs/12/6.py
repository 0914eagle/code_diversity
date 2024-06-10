
def get_white_area(rectangle):
    
    x1, y1, x2, y2 = rectangle
    return (x2 - x1) * (y2 - y1)

def main():
    W, H, N = map(int, input().split())
    points = []
    for _ in range(N):
        x, y, a = map(int, input().split())
        points.append((x, y, a))

    # Initialize the rectangle with the given dimensions
    rectangle = (0, 0, W, H)

    # Iterate through the points and paint the corresponding regions
    for x, y, a in points:
        if a == 1:
            rectangle = (rectangle[0], rectangle[1], x, rectangle[3])
        elif a == 2:
            rectangle = (rectangle[0], rectangle[1], rectangle[2], y)
        elif a == 3:
            rectangle = (rectangle[0], y, rectangle[2], rectangle[3])
        elif a == 4:
            rectangle = (x, rectangle[1], rectangle[2], rectangle[3])

    # Calculate the area of the white region
    white_area = get_white_area(rectangle)
    print(white_area)

if __name__ == '__main__':
    main()

