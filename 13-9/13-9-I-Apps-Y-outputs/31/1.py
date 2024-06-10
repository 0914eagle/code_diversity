
import math

def get_closest_hole(gopher_position, holes):
    closest_hole = None
    min_distance = math.inf
    for hole in holes:
        distance = math.sqrt((gopher_position[0]-hole[0])**2 + (gopher_position[1]-hole[1])**2)
        if distance < min_distance:
            min_distance = distance
            closest_hole = hole
    return closest_hole

def can_gopher_escape(gopher_position, dog_position, holes):
    closest_hole = get_closest_hole(gopher_position, holes)
    if closest_hole:
        distance_to_hole = math.sqrt((gopher_position[0]-closest_hole[0])**2 + (gopher_position[1]-closest_hole[1])**2)
        dog_distance_to_hole = math.sqrt((dog_position[0]-closest_hole[0])**2 + (dog_position[1]-closest_hole[1])**2)
        if distance_to_hole < dog_distance_to_hole:
            return True
    return False

def main():
    gopher_position = list(map(float, input().split()))
    dog_position = list(map(float, input().split()))
    holes = []
    for _ in range(int(input())):
        hole = list(map(float, input().split()))
        holes.append(hole)
    if can_gopher_escape(gopher_position, dog_position, holes):
        print("The gopher can escape through the hole at", get_closest_hole(gopher_position, holes))
    else:
        print("The gopher cannot escape.")

if __name__ == '__main__':
    main()

