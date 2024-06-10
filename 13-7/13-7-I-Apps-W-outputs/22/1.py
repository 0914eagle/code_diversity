
def rotate_map(map):
    return [list(row) for row in zip(*map[::-1])]

def flip_map(map):
    return [row[::-1] for row in map]

def are_maps_identical(map1, map2):
    return map1 == map2

def are_maps_rotated(map1, map2):
    return any(map1 == rotate_map(map2) for _ in range(4))

def are_maps_flipped(map1, map2):
    return any(map1 == flip_map(map2) for _ in range(2))

def are_maps_matched(map1, map2):
    return are_maps_identical(map1, map2) or are_maps_rotated(map1, map2) or are_maps_flipped(map1, map2)

def main():
    n = int(input())
    map1 = [input() for _ in range(n)]
    map2 = [input() for _ in range(n)]
    print("Yes") if are_maps_matched(map1, map2) else print("No")

if __name__ == '__main__':
    main()

