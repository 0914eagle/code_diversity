
import math

def get_tide_height(t, a):
    return 0.5 * a * (math.cos(t * 2 * math.pi / 12) + 1)

def is_safe_to_enter_square(square_height, tide_height):
    return abs(square_height - tide_height) <= 1

def get_safe_distance_from_home(map, home_coordinates, walking_speed):
    tide_height = get_tide_height(0, a)
    safe_distance_from_home = 0
    for row in range(home_coordinates[1], len(map)):
        for col in range(home_coordinates[0], len(map[0])):
            square_height = map[row][col]
            if is_safe_to_enter_square(square_height, tide_height):
                safe_distance_from_home = max(safe_distance_from_home, get_distance_between_squares(home_coordinates, (col, row)))
    return safe_distance_from_home

def get_distance_between_squares(square1_coordinates, square2_coordinates):
    return math.sqrt((square1_coordinates[0] - square2_coordinates[0]) ** 2 + (square1_coordinates[1] - square2_coordinates[1]) ** 2)

def main():
    a, m = map(float, input().split())
    w, h, x, y = map(int, input().split())
    map = []
    for _ in range(h):
        map.append(list(map(int, input().split())))
    safe_distance_from_home = get_safe_distance_from_home(map, (x, y), m)
    print(safe_distance_from_home)

if __name__ == '__main__':
    main()

