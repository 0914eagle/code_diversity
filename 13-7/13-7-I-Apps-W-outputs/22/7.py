
def is_same_solar_system(map1, map2):
    # Flip map1 along the vertical axis
    flipped_map1 = [list(reversed(row)) for row in map1]
    
    # Check if map2 is identical to flipped_map1 after rotation
    for i in range(4):
        if map2 == rotate_map(flipped_map1, i):
            return True
    
    # Check if map2 is identical to flipped_map1 after flipping along the horizontal axis
    flipped_map1 = [list(reversed(row)) for row in flipped_map1]
    if map2 == flipped_map1:
        return True
    
    # If none of the above conditions are met, the maps are not identical
    return False

def rotate_map(map, n):
    # Rotate map n times clockwise
    return [row[n:] + row[:n] for row in map]

if __name__ == '__main__':
    map1 = [input() for _ in range(int(input()))]
    map2 = [input() for _ in range(int(input()))]
    print("Yes") if is_same_solar_system(map1, map2) else print("No")

