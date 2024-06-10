
def is_match(map1, map2):
    # Convert the maps to sets to check for identical stars
    set1 = set(map1)
    set2 = set(map2)
    if set1 == set2:
        return True
    
    # Check if the maps can be rotated 90 degrees clockwise
    map1_rotated = [list(row) for row in zip(*map1[::-1])]
    set1 = set(map1_rotated)
    if set1 == set2:
        return True
    
    # Check if the maps can be rotated 180 degrees
    map1_rotated = [list(row) for row in map1[::-1]]
    set1 = set(map1_rotated)
    if set1 == set2:
        return True
    
    # Check if the maps can be rotated 270 degrees clockwise
    map1_rotated = [list(row) for row in zip(*map1)]
    set1 = set(map1_rotated)
    if set1 == set2:
        return True
    
    # Check if the maps can be flipped along the vertical axis
    map1_flipped = [row[::-1] for row in map1]
    set1 = set(map1_flipped)
    if set1 == set2:
        return True
    
    # Check if the maps can be flipped along the horizontal axis
    map1_flipped = [row[::-1] for row in map1[::-1]]
    set1 = set(map1_flipped)
    if set1 == set2:
        return True
    
    return False

def main():
    n = int(input())
    map1 = [input() for _ in range(n)]
    map2 = [input() for _ in range(n)]
    if is_match(map1, map2):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

