
def find_hole(gopher_pos, dog_pos, holes):
    # Find the distance between the gopher and the dog
    dist = abs(gopher_pos[0] - dog_pos[0]) + abs(gopher_pos[1] - dog_pos[1])
    
    # Find the hole that is closest to the gopher
    min_dist = float('inf')
    min_hole = None
    for hole in holes:
        hole_dist = abs(gopher_pos[0] - hole[0]) + abs(gopher_pos[1] - hole[1])
        if hole_dist < min_dist:
            min_dist = hole_dist
            min_hole = hole
    
    # Check if the dog can reach the hole before the gopher
    if min_dist < dist:
        return "The gopher cannot escape."
    
    # Check if the dog can reach the hole at the same time as the gopher
    if min_dist == dist:
        return "The gopher can escape through the hole at ({}, {}).".format(min_hole[0], min_hole[1])
    
    # Check if the dog can reach the hole after the gopher
    if min_dist > dist:
        return "The gopher can escape through the hole at ({}, {}).".format(min_hole[0], min_hole[1])

def main():
    gopher_pos = list(map(float, input().split()))
    dog_pos = list(map(float, input().split()))
    holes = []
    for _ in range(int(input())):
        holes.append(list(map(float, input().split())))
    print(find_hole(gopher_pos, dog_pos, holes))

if __name__ == '__main__':
    main()

