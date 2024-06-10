
def get_white_area(W, H, N, points):
    # Initialize the white area as the entire rectangle
    white_area = W * H
    
    # Loop through each point and its corresponding a value
    for point, a in points:
        # If a = 1, paint the region to the left of the point
        if a == 1:
            white_area -= (point * H)
        # If a = 2, paint the region to the right of the point
        elif a == 2:
            white_area -= ((W - point) * H)
        # If a = 3, paint the region above the point
        elif a == 3:
            white_area -= (point * W)
        # If a = 4, paint the region below the point
        elif a == 4:
            white_area -= ((H - point) * W)
    
    return white_area

def main():
    W, H, N = map(int, input().split())
    points = []
    for _ in range(N):
        x, y, a = map(int, input().split())
        points.append((x, y, a))
    print(get_white_area(W, H, N, points))

if __name__ == '__main__':
    main()

