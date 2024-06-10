
import math

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def get_closest_hole(gopher_x, gopher_y, dog_x, dog_y, holes):
    closest_hole = None
    closest_distance = float('inf')
    for hole_x, hole_y in holes:
        distance = get_distance(gopher_x, gopher_y, hole_x, hole_y)
        if distance < closest_distance:
            closest_hole = (hole_x, hole_y)
            closest_distance = distance
    return closest_hole

def main():
    gopher_x, gopher_y, dog_x, dog_y = map(float, input().split())
    num_holes = int(input())
    holes = []
    for _ in range(num_holes):
        x, y = map(float, input().split())
        holes.append((x, y))
    closest_hole = get_closest_hole(gopher_x, gopher_y, dog_x, dog_y, holes)
    if closest_hole:
        print(f"The gopher can escape through the hole at ({closest_hole[0]}, {closest_hole[1]}).")
    else:
        print("The gopher cannot escape.")

if __name__ == '__main__':
    main()

