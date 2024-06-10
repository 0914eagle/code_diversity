
import sys

def get_input():
    W, H, N = map(int, input().split())
    points = []
    for _ in range(N):
        x, y, a = map(int, input().split())
        points.append((x, y, a))
    return W, H, N, points

def paint_rectangle(W, H, N, points):
    white_area = W * H
    for x, y, a in points:
        if a == 1:
            white_area -= x * H
        elif a == 2:
            white_area -= (W - x) * H
        elif a == 3:
            white_area -= y * W
        else:
            white_area -= (H - y) * W
    return white_area

def main():
    W, H, N, points = get_input()
    print(paint_rectangle(W, H, N, points))

if __name__ == '__main__':
    main()

