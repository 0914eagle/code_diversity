
def rotate_map(map, num_rotations):
    return map[::-1]

def flip_map(map, axis):
    if axis == "vertical":
        return ["".join(reversed(row)) for row in map]
    elif axis == "horizontal":
        return list(map)[::-1]
    else:
        raise ValueError("Invalid axis")

def are_maps_identical(map1, map2):
    return map1 == map2

def main():
    n = int(input())
    map1 = [input() for _ in range(n)]
    map2 = [input() for _ in range(n)]
    for i in range(4):
        rotated_map1 = rotate_map(map1, i)
        for j in range(4):
            flipped_map1 = flip_map(rotated_map1, "vertical" if j % 2 == 0 else "horizontal")
            if are_maps_identical(flipped_map1, map2):
                return "Yes"
    return "No"

if __name__ == '__main__':
    print(main())

