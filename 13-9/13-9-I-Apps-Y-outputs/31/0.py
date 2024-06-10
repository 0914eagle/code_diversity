
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_hole_location(gopher_x, gopher_y, dog_x, dog_y, hole_x, hole_y):
    distance_to_hole = get_distance(gopher_x, gopher_y, hole_x, hole_y)
    dog_reaches_hole_before_gopher = distance_to_hole / (get_distance(gopher_x, gopher_y, dog_x, dog_y) * 2)
    if dog_reaches_hole_before_gopher >= 1:
        return True
    else:
        return False

def main():
    gopher_x, gopher_y, dog_x, dog_y = map(float, input().split())
    num_holes = int(input())
    for i in range(num_holes):
        hole_x, hole_y = map(float, input().split())
        if get_hole_location(gopher_x, gopher_y, dog_x, dog_y, hole_x, hole_y):
            print(f"The gopher can escape through the hole at ({hole_x}, {hole_y}).")
            break
    else:
        print("The gopher cannot escape.")

if __name__ == '__main__':
    main()

