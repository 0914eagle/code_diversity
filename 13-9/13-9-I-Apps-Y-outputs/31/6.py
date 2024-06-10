
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_closest_hole(dog_x, dog_y, gopher_x, gopher_y, holes):
    closest_hole = None
    min_distance = float('inf')
    for hole in holes:
        distance = get_distance(gopher_x, gopher_y, hole[0], hole[1])
        if distance < min_distance:
            min_distance = distance
            closest_hole = hole
    return closest_hole

def get_gopher_escape_hole(dog_x, dog_y, gopher_x, gopher_y, holes):
    closest_hole = get_closest_hole(dog_x, dog_y, gopher_x, gopher_y, holes)
    if closest_hole:
        return 'The gopher can escape through the hole at ({}, {}).'.format(closest_hole[0], closest_hole[1])
    else:
        return 'The gopher cannot escape.'

def main():
    dog_x, dog_y, gopher_x, gopher_y = map(float, input().split())
    num_holes = int(input())
    holes = []
    for i in range(num_holes):
        x, y = map(float, input().split())
        holes.append((x, y))
    print(get_gopher_escape_hole(dog_x, dog_y, gopher_x, gopher_y, holes))

if __name__ == '__main__':
    main()

