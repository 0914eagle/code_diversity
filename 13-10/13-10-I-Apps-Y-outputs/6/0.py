
import sys

def get_input():
    W, H, N = map(int, input().split())
    points = []
    for i in range(N):
        x, y, a = map(int, input().split())
        points.append((x, y, a))
    return W, H, N, points

def get_white_region(W, H, points):
    white_region = set([(x, y) for x in range(W) for y in range(H)])
    for x, y, a in points:
        if a == 1:
            white_region -= set([(x_, y_) for x_ in range(x) for y_ in range(H)])
        elif a == 2:
            white_region -= set([(x_, y_) for x_ in range(x, W) for y_ in range(H)])
        elif a == 3:
            white_region -= set([(x_, y_) for x_ in range(W) for y_ in range(y)])
        else:
            white_region -= set([(x_, y_) for x_ in range(W) for y_ in range(y, H)])
    return white_region

def get_area(white_region):
    return len(white_region)

def main():
    W, H, N, points = get_input()
    white_region = get_white_region(W, H, points)
    print(get_area(white_region))

if __name__ == '__main__':
    main()

