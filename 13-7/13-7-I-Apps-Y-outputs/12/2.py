
def get_white_area(W, H, points):
    white_area = W * H
    for point, a in points:
        if a == 1:
            white_area -= point * H
        elif a == 2:
            white_area -= (W - point) * H
        elif a == 3:
            white_area -= W * (H - point)
        else:
            white_area -= W * point
    return white_area

def main():
    W, H, N = map(int, input().split())
    points = []
    for _ in range(N):
        x, y, a = map(int, input().split())
        points.append((x, y, a))
    print(get_white_area(W, H, points))

if __name__ == '__main__':
    main()

