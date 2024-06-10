
import math

def get_tide_height(t, a):
    return 0.5 * a * (math.cos(t * 2 * math.pi / 12) + 1)

def get_max_distance(map, speed, home, tide_heights):
    max_distance = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] != 0 and map[i][j] != home:
                distance = math.sqrt((i - home[0]) ** 2 + (j - home[1]) ** 2)
                if distance > max_distance:
                    max_distance = distance
    return max_distance

def main():
    a, speed = map(float, input().split())
    W, H, X, Y = map(int, input().split())
    map = []
    for i in range(H):
        map.append(list(map(int, input().split())))
    home = [X, Y]
    tide_heights = [get_tide_height(t, a) for t in range(13)]
    max_distance = get_max_distance(map, speed, home, tide_heights)
    print(max_distance)

if __name__ == '__main__':
    main()

