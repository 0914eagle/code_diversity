
import math

def get_tide_level(t, a):
    return 0.5 * a * (math.cos(t * 2 * math.pi / 12) + 1)

def get_distance_from_home(home_x, home_y, x, y):
    return math.sqrt((home_x - x) ** 2 + (home_y - y) ** 2)

def is_safe_to_enter_square(square_height, current_tide_level, max_tide_level):
    return abs(square_height - current_tide_level) <= 1

def get_max_distance_from_home(map, home_x, home_y, walking_speed):
    max_distance = 0
    current_tide_level = get_tide_level(0, a)
    for y in range(len(map)):
        for x in range(len(map[y])):
            if is_safe_to_enter_square(map[y][x], current_tide_level, get_tide_level(1, a)):
                distance = get_distance_from_home(home_x, home_y, x, y)
                if distance > max_distance:
                    max_distance = distance
            current_tide_level += walking_speed / 1000
    return max_distance

def main():
    a, walking_speed = map(float, input().split())
    home_x, home_y = map(int, input().split())
    map = []
    for _ in range(H):
        map.append(list(map(int, input().split())))
    print(get_max_distance_from_home(map, home_x, home_y, walking_speed))

if __name__ == '__main__':
    main()

