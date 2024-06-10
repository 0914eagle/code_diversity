
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def find_escape_hole(gopher_x, gopher_y, dog_x, dog_y, holes):
    min_distance = math.inf
    escape_hole = None
    for hole in holes:
        hole_distance = distance(gopher_x, gopher_y, hole[0], hole[1])
        if hole_distance < min_distance:
            min_distance = hole_distance
            escape_hole = hole
    if escape_hole:
        return "The gopher can escape through the hole at ({}, {})".format(escape_hole[0], escape_hole[1])
    else:
        return "The gopher cannot escape."

def main():
    gopher_x, gopher_y, dog_x, dog_y = map(float, input().split())
    holes = []
    for _ in range(int(input())):
        x, y = map(float, input().split())
        holes.append((x, y))
    print(find_escape_hole(gopher_x, gopher_y, dog_x, dog_y, holes))

if __name__ == '__main__':
    main()

