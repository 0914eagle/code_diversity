
import math

def get_hole_coordinates():
    hole_coordinates = []
    for _ in range(int(input())):
        hole_coordinates.append(tuple(map(float, input().split())))
    return hole_coordinates

def find_closest_hole(gopher_coordinates, dog_coordinates, hole_coordinates):
    min_distance = float('inf')
    closest_hole = None
    for hole in hole_coordinates:
        distance = math.sqrt((gopher_coordinates[0] - hole[0]) ** 2 + (gopher_coordinates[1] - hole[1]) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_hole = hole
    return closest_hole

def escape_through_hole(gopher_coordinates, dog_coordinates, hole_coordinates):
    closest_hole = find_closest_hole(gopher_coordinates, dog_coordinates, hole_coordinates)
    if closest_hole:
        return f"The gopher can escape through the hole at ({closest_hole[0]}, {closest_hole[1]})."
    else:
        return "The gopher cannot escape."

def main():
    gopher_coordinates = tuple(map(float, input().split()))
    dog_coordinates = tuple(map(float, input().split()))
    hole_coordinates = get_hole_coordinates()
    print(escape_through_hole(gopher_coordinates, dog_coordinates, hole_coordinates))

if __name__ == '__main__':
    main()

