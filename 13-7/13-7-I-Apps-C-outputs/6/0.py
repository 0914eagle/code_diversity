
import math

def read_input():
    N = int(input())
    contours = []
    for _ in range(N):
        H0, H1, M = map(int, input().split())
        contour = []
        for _ in range(M):
            x, y = map(int, input().split())
            contour.append((x, y))
        contours.append((H0, H1, contour))
    return contours

def find_closest_distance(contours, target):
    min_distance = math.inf
    for H0, H1, contour in contours:
        for i in range(len(contour)):
            x1, y1 = contour[i]
            x2, y2 = contour[(i+1) % len(contour)]
            distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            slant_distance = distance * (H0-H1) / (x1-x2)
            min_distance = min(min_distance, slant_distance)
    return min_distance

def main():
    contours = read_input()
    target = (0, 0)
    print(find_closest_distance(contours, target))

if __name__ == '__main__':
    main()

