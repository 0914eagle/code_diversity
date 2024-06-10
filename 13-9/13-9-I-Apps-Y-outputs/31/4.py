
import math

def find_closest_hole(gopher_location, dog_location, hole_locations):
    
    closest_hole = None
    min_distance = math.inf
    for hole in hole_locations:
        distance = math.sqrt((hole[0] - gopher_location[0]) ** 2 + (hole[1] - gopher_location[1]) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_hole = hole
    return closest_hole

def can_escape(gopher_location, dog_location, hole_locations):
    
    closest_hole = find_closest_hole(gopher_location, dog_location, hole_locations)
    if closest_hole:
        distance_to_hole = math.sqrt((closest_hole[0] - gopher_location[0]) ** 2 + (closest_hole[1] - gopher_location[1]) ** 2)
        distance_to_dog = math.sqrt((dog_location[0] - gopher_location[0]) ** 2 + (dog_location[1] - gopher_location[1]) ** 2)
        if distance_to_hole < distance_to_dog * 2:
            return True
    return False

def main():
    gopher_location = tuple(map(float, input().split()))
    dog_location = tuple(map(float, input().split()))
    hole_locations = []
    for _ in range(int(input())):
        hole_locations.append(tuple(map(float, input().split())))
    if can_escape(gopher_location, dog_location, hole_locations):
        print("The gopher can escape through the hole at", hole_locations[0])
    else:
        print("The gopher cannot escape.")

if __name__ == '__main__':
    main()

