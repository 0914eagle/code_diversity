
def get_white_area(W, H, points):
    # Initialize the white area as the entire rectangle
    white_area = W * H
    
    # Iterate over the points and update the white area accordingly
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
    for i in range(N):
        x, y, a = map(int, input().split())
        points.append((x, y, a))
    print(get_white_area(W, H, points))

if __name__ == '__main__':
    main()

