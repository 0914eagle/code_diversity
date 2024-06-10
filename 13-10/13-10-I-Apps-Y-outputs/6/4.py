
def read_input():
    W, H, N = map(int, input().split())
    points = []
    for _ in range(N):
        x, y, a = map(int, input().split())
        points.append((x, y, a))
    return W, H, N, points

def paint_rectangle(W, H, N, points):
    area = W * H
    for point in points:
        x, y, a = point
        if a == 1:
            area -= (x * H)
        elif a == 2:
            area -= ((W - x) * H)
        elif a == 3:
            area -= (y * W)
        elif a == 4:
            area -= ((H - y) * W)
    return area

def main():
    W, H, N, points = read_input()
    print(paint_rectangle(W, H, N, points))

if __name__ == '__main__':
    main()

