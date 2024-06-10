
def check_maps(map1, map2):
    # Check if the maps are the same
    if map1 == map2:
        return "Yes"
    
    # Check if the maps can be rotated 90 degrees clockwise
    map1_rotated = ["".join(reversed(row)) for row in zip(*map1)]
    if map1_rotated == map2:
        return "Yes"
    
    # Check if the maps can be rotated 180 degrees
    map1_rotated = [row[::-1] for row in map1]
    if map1_rotated == map2:
        return "Yes"
    
    # Check if the maps can be rotated 270 degrees clockwise
    map1_rotated = ["".join(reversed(row)) for row in zip(*map1[::-1])]
    if map1_rotated == map2:
        return "Yes"
    
    # Check if the maps can be flipped along the vertical axis
    map1_flipped = [row[::-1] for row in map1]
    if map1_flipped == map2:
        return "Yes"
    
    # Check if the maps can be flipped along the horizontal axis
    map1_flipped = [row[::-1] for row in map1[::-1]]
    if map1_flipped == map2:
        return "Yes"
    
    # If none of the above conditions are met, return "No"
    return "No"

def main():
    n = int(input())
    map1 = [input() for _ in range(n)]
    map2 = [input() for _ in range(n)]
    print(check_maps(map1, map2))

if __name__ == '__main__':
    main()

