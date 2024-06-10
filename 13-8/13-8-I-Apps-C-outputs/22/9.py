
def get_tide_height(t, a):
    return 0.5 * a * (cos(t * 2 * pi / 12) + 1)

def get_distance_between_squares(square1, square2, speed):
    return (square2[0] - square1[0]) ** 2 + (square2[1] - square1[1]) ** 2

def is_safe_to_enter_square(square, tide_height, dry_threshold):
    return abs(square[2] - tide_height) <= dry_threshold

def get_max_distance_from_home(home, map, speed, tide_a, dry_threshold):
    max_distance = 0
    current_square = home
    tide_height = get_tide_height(0, tide_a)
    while True:
        # Get the four neighbouring squares
        north_square = map[current_square[1] - 1][current_square[0]] if current_square[1] > 0 else None
        south_square = map[current_square[1] + 1][current_square[0]] if current_square[1] < len(map) - 1 else None
        east_square = map[current_square[1]][current_square[0] + 1] if current_square[0] < len(map[0]) - 1 else None
        west_square = map[current_square[1]][current_square[0] - 1] if current_square[0] > 0 else None

        # Check if any of the neighbouring squares are safe to enter
        safe_squares = [square for square in [north_square, south_square, east_square, west_square] if is_safe_to_enter_square(square, tide_height, dry_threshold)]

        # If there are no safe squares, we can't move any further
        if not safe_squares:
            break

        # Choose the closest safe square to move to
        closest_safe_square = min(safe_squares, key=lambda square: get_distance_between_squares(current_square, square, speed))

        # Update the current square and tide height
        current_square = closest_safe_square
        tide_height = get_tide_height(current_square[3], tide_a)

        # Update the max distance
        max_distance = max(max_distance, get_distance_between_squares(home, current_square, speed))

    return max_distance

def main():
    tide_a, speed = map(float, input().split())
    _, _, home_x, home_y = map(int, input().split())
    map = []
    for _ in range(int(input())):
        map.append([int(i) for i in input().split()])
    dry_threshold = 1
    max_distance = get_max_distance_from_home((home_x, home_y, 0, 0), map, speed, tide_a, dry_threshold)
    print(max_distance)

if __name__ == '__main__':
    main()

