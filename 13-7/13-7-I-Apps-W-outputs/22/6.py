
def is_same_map(map1, map2):
    # Check if the maps have the same dimensions
    if len(map1) != len(map2):
        return False

    # Check if the maps are identical
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            if map1[i][j] != map2[i][j]:
                return False

    return True

def rotate_map(map, n):
    # Rotate the map n times
    for _ in range(n):
        map = list(map[i] for i in range(len(map)-1, -1, -1))
    return map

def flip_map(map, axis):
    # Flip the map along the specified axis
    if axis == "horizontal":
        return ["".join(reversed(row)) for row in map]
    elif axis == "vertical":
        return list(reversed(map))
    else:
        raise ValueError("Invalid axis")

def find_matching_map(map1, map2):
    # Check if the maps are identical
    if is_same_map(map1, map2):
        return True

    # Check if the maps can be rotated to match
    for i in range(4):
        if is_same_map(map1, rotate_map(map2, i)):
            return True

    # Check if the maps can be flipped to match
    for axis in ["horizontal", "vertical"]:
        if is_same_map(map1, flip_map(map2, axis)):
            return True

    # If no match is found, return False
    return False

if __name__ == '__main__':
    map1 = [input() for _ in range(int(input()))]
    map2 = [input() for _ in range(int(input()))]
    print("Yes") if find_matching_map(map1, map2) else print("No")

