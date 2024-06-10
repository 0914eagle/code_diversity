
import math

def get_tide_height(t, a):
    return 0.5 * a * (math.cos(t * 2 * math.pi / 12) + 1)

def get_walkable_squares(square_heights, low_tide_height):
    walkable_squares = []
    for i in range(len(square_heights)):
        if abs(square_heights[i] - low_tide_height) <= 1:
            walkable_squares.append(i)
    return walkable_squares

def get_max_distance(walkable_squares, home_square, walk_speed):
    max_distance = 0
    for square in walkable_squares:
        distance = math.sqrt((square[0] - home_square[0]) ** 2 + (square[1] - home_square[1]) ** 2)
        time = distance / walk_speed
        low_tide_height = get_tide_height(time, a)
        if abs(square_heights[square] - low_tide_height) <= 1:
            max_distance = max(max_distance, distance)
    return max_distance

def main():
    a, m = map(float, input().split())
    W, H, X, Y = map(int, input().split())
    square_heights = []
    for i in range(H):
        row = list(map(int, input().split()))
        square_heights.append(row)
    home_square = (X, Y)
    walk_speed = m / 3600
    low_tide_height = get_tide_height(0, a)
    walkable_squares = get_walkable_squares(square_heights, low_tide_height)
    max_distance = get_max_distance(walkable_squares, home_square, walk_speed)
    print(max_distance)

if __name__ == '__main__':
    main()

