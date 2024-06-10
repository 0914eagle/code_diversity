
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_hole_distance(gopher_x, gopher_y, hole_x, hole_y):
    return get_distance(gopher_x, gopher_y, hole_x, hole_y)

def get_dog_distance(gopher_x, gopher_y, dog_x, dog_y):
    return get_distance(gopher_x, gopher_y, dog_x, dog_y)

def can_gopher_escape(gopher_x, gopher_y, dog_x, dog_y, hole_x, hole_y):
    gopher_hole_distance = get_hole_distance(gopher_x, gopher_y, hole_x, hole_y)
    dog_gopher_distance = get_dog_distance(gopher_x, gopher_y, dog_x, dog_y)
    if gopher_hole_distance < dog_gopher_distance * 2:
        return True
    else:
        return False

def find_hole(gopher_x, gopher_y, dog_x, dog_y, hole_coordinates):
    for hole_x, hole_y in hole_coordinates:
        if can_gopher_escape(gopher_x, gopher_y, dog_x, dog_y, hole_x, hole_y):
            return hole_x, hole_y
    return None

def main():
    gopher_x, gopher_y, dog_x, dog_y = map(float, input().split())
    hole_coordinates = []
    for _ in range(int(input())):
        hole_x, hole_y = map(float, input().split())
        hole_coordinates.append((hole_x, hole_y))
    hole_x, hole_y = find_hole(gopher_x, gopher_y, dog_x, dog_y, hole_coordinates)
    if hole_x is not None:
        print(f"The gopher can escape through the hole at ({hole_x:.3f}, {hole_y:.3f}).")
    else:
        print("The gopher cannot escape.")

if __name__ == '__main__':
    main()

