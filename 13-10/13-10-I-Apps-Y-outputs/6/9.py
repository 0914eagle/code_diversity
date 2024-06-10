
import sys

def get_white_area(W, H, points):
    
    x_coords, y_coords, a_seq = zip(*points)
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)
    
    white_area = W * H
    
    for i in range(len(a_seq)):
        if a_seq[i] == 1:
            white_area -= (x_max - x_coords[i]) * H
        elif a_seq[i] == 2:
            white_area -= (x_coords[i] - x_min) * H
        elif a_seq[i] == 3:
            white_area -= (y_max - y_coords[i]) * W
        else:
            white_area -= (y_coords[i] - y_min) * W
    
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

