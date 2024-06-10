
def is_same_solar_system(map1, map2):
    # Check if maps are of the same size
    if len(map1) != len(map2):
        return False
    
    # Check if maps are identical
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            if map1[i][j] != map2[i][j]:
                return False
    
    # Check if maps can be rotated to match
    for i in range(4):
        map2_rotated = rotate_map(map2, i)
        if map1 == map2_rotated:
            return True
    
    # Check if maps can be flipped to match
    map2_flipped = flip_map(map2)
    if map1 == map2_flipped:
        return True
    
    # If none of the above conditions are met, the maps are not of the same solar system
    return False

def rotate_map(map, num_rotations):
    # Rotate map by 90 degrees clockwise num_rotations times
    return [list(reversed(row)) for row in zip(*map)]

def flip_map(map):
    # Flip map along the vertical axis
    return [row[::-1] for row in map]

if __name__ == '__main__':
    map1 = [list(input()) for _ in range(int(input()))]
    map2 = [list(input()) for _ in range(int(input()))]
    print("Yes") if is_same_solar_system(map1, map2) else print("No")

