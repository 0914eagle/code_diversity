
import math

def get_tide_height(t, a):
    return 0.5 * a * (math.cos(t * 2 * math.pi / 12) + 1)

def get_dry_area(heights, tide_height):
    dry_area = []
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            if abs(heights[i][j] - tide_height) <= 1:
                dry_area.append((i, j))
    return dry_area

def get_max_distance(home, dry_area, speed, time):
    max_distance = 0
    for i in range(len(dry_area)):
        for j in range(i+1, len(dry_area)):
            distance = math.sqrt((dry_area[i][0] - dry_area[j][0]) ** 2 + (dry_area[i][1] - dry_area[j][1]) ** 2)
            if distance > max_distance:
                max_distance = distance
    return max_distance * speed * time

def main():
    a, m = map(float, input().split())
    w, h, x, y = map(int, input().split())
    heights = []
    for i in range(h):
        heights.append(list(map(int, input().split())))
    
    tide_height = get_tide_height(1, a)
    dry_area = get_dry_area(heights, tide_height)
    max_distance = get_max_distance((x, y), dry_area, m, 1)
    print(max_distance)

if __name__ == '__main__':
    main()

