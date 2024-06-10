
def rotate_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def rotate_180(matrix):
    return rotate_90(rotate_90(matrix))

def rotate_270(matrix):
    return rotate_90(rotate_180(matrix))

def flip_horizontally(matrix):
    return [list(reversed(row)) for row in matrix]

def flip_vertically(matrix):
    return [list(reversed(row)) for row in matrix[::-1]]

def are_identical(map1, map2):
    return map1 == map2

def are_rotated(map1, map2):
    return are_identical(map1, rotate_90(map2)) or \
           are_identical(map1, rotate_180(map2)) or \
           are_identical(map1, rotate_270(map2))

def are_flipped(map1, map2):
    return are_identical(map1, flip_horizontally(map2)) or \
           are_identical(map1, flip_vertically(map2))

def are_matched(map1, map2):
    return are_identical(map1, map2) or \
           are_rotated(map1, map2) or \
           are_flipped(map1, map2)

def main():
    map1 = []
    map2 = []
    for _ in range(int(input())):
        map1.append(input())
        map2.append(input())
    if are_matched(map1, map2):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

