
def f1(n, rectangles):
    # Function to find any point with integer coordinates that belongs to at least (n-1) given rectangles
    x_coords = set()
    y_coords = set()
    for rectangle in rectangles:
        x1, y1, x2, y2 = rectangle
        x_coords.update([x1, x2])
        y_coords.update([y1, y2])
    x_coords = list(x_coords)
    y_coords = list(y_coords)
    for x in x_coords:
        for y in y_coords:
            count = 0
            for rectangle in rectangles:
                x1, y1, x2, y2 = rectangle
                if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                    count += 1
            if count >= n-1:
                return x, y
    return -1, -1

def f2(n, rectangles):
    # Function to find any point with integer coordinates that belongs to at least (n-1) given rectangles
    x_coords = set()
    y_coords = set()
    for rectangle in rectangles:
        x1, y1, x2, y2 = rectangle
        x_coords.update([x1, x2])
        y_coords.update([y1, y2])
    x_coords = list(x_coords)
    y_coords = list(y_coords)
    for y in y_coords:
        for x in x_coords:
            count = 0
            for rectangle in rectangles:
                x1, y1, x2, y2 = rectangle
                if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                    count += 1
            if count >= n-1:
                return x, y
    return -1, -1

if __name__ == '__main__':
    n = int(input())
    rectangles = []
    for i in range(n):
        rectangles.append(list(map(int, input().split())))
    x, y = f1(n, rectangles)
    if x == -1 and y == -1:
        x, y = f2(n, rectangles)
    print(x, y)

