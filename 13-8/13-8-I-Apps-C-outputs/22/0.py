
import math

def get_tide_level(t):
    return 0.5 * a * (math.cos(t * 2 * math.pi / 12) + 1)

def get_distance_from_home(x, y, tide_level):
    return math.sqrt((x - W / 2) ** 2 + (y - H / 2) ** 2)

def get_safe_distance(tide_level):
    safe_distance = 0
    for x in range(W):
        for y in range(H):
            if heights[x][y] <= tide_level:
                safe_distance = max(safe_distance, get_distance_from_home(x, y, tide_level))
    return safe_distance

def main():
    a, m = map(float, input().split())
    W, H, X, Y = map(int, input().split())
    heights = []
    for _ in range(H):
        heights.append(list(map(int, input().split())))

    tide_levels = [get_tide_level(t) for t in range(13)]
    safe_distances = [get_safe_distance(tide_level) for tide_level in tide_levels]

    print(max(safe_distances))

if __name__ == '__main__':
    main()

