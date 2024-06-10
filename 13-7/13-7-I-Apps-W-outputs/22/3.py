
def is_identical_map(map1, map2):
    # Check if the maps have the same dimensions
    if len(map1) != len(map2):
        return False
    
    # Check if all the characters in the maps are the same
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            if map1[i][j] != map2[i][j]:
                return False
    
    # If all the characters are the same, the maps are identical
    return True

def rotate_map(map, num_rotations):
    # Rotate the map num_rotations times clockwise
    for _ in range(num_rotations):
        map = list(map[i] for i in range(len(map)-1, -1, -1))
    
    return map

def flip_map(map, axis):
    # Flip the map along the specified axis (0 for horizontal, 1 for vertical)
    if axis == 0:
        return [row[::-1] for row in map]
    else:
        return map[::-1]

def match_maps(map1, map2):
    # Check if map1 and map2 are identical
    if is_identical_map(map1, map2):
        return True
    
    # Check if map1 and map2 can be matched by rotating map1
    for i in range(4):
        if is_identical_map(map1, rotate_map(map2, i)):
            return True
    
    # Check if map1 and map2 can be matched by flipping map1 along the horizontal axis
    if is_identical_map(map1, flip_map(map2, 0)):
        return True
    
    # Check if map1 and map2 can be matched by flipping map1 along the vertical axis
    if is_identical_map(map1, flip_map(map2, 1)):
        return True
    
    # If none of the above conditions are met, map1 and map2 cannot be matched
    return False

def main():
    # Read the input maps from stdin
    map1 = [input() for _ in range(int(input()))]
    map2 = [input() for _ in range(int(input()))]
    
    # Check if map1 and map2 can be matched
    if match_maps(map1, map2):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

