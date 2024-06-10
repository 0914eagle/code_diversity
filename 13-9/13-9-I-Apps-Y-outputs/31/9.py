
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def escape_hole(gopher_x, gopher_y, dog_x, dog_y, hole_x, hole_y):
    gopher_to_hole = distance(gopher_x, gopher_y, hole_x, hole_y)
    dog_to_hole = distance(dog_x, dog_y, hole_x, hole_y)
    if gopher_to_hole < dog_to_hole * 2:
        return "The gopher can escape through the hole at ({}, {}).".format(hole_x, hole_y)
    else:
        return "The gopher cannot escape."

def main():
    gopher_x, gopher_y, dog_x, dog_y = map(float, input().split())
    num_holes = int(input())
    for _ in range(num_holes):
        hole_x, hole_y = map(float, input().split())
        print(escape_hole(gopher_x, gopher_y, dog_x, dog_y, hole_x, hole_y))

if __name__ == '__main__':
    main()

