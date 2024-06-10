
def check_maps(map1, map2):
    # Flip map1 along the vertical axis
    map1_flipped = [list(reversed(row)) for row in map1]
    
    # Rotate map1 90 degrees clockwise
    map1_rotated = [list(row) for row in zip(*map1[::-1])]
    
    # Check if map1_flipped and map2 are identical
    if map1_flipped == map2:
        return "Yes"
    
    # Check if map1_rotated and map2 are identical
    if map1_rotated == map2:
        return "Yes"
    
    # Check if map1 and map2 are identical
    if map1 == map2:
        return "Yes"
    
    # If none of the above conditions are met, return "No"
    return "No"

def main():
    # Read the input maps
    map1 = [input() for _ in range(int(input()))]
    map2 = [input() for _ in range(int(input()))]
    
    # Check if the maps are identical
    result = check_maps(map1, map2)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

