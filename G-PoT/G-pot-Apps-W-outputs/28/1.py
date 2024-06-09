
h, w = map(int, input().split())
picture = [input() for _ in range(h)]

def check_plus_shape(picture, h, w, center_row, center_col):
    # Check left direction
    for col in range(center_col-1, -1, -1):
        if picture[center_row][col] == '.':
            return False
    # Check right direction
    for col in range(center_col+1, w):
        if picture[center_row][col] == '.':
            return False
    # Check up direction
    for row in range(center_row-1, -1, -1):
        if picture[row][center_col] == '.':
            return False
    # Check down direction
    for row in range(center_row+1, h):
        if picture[row][center_col] == '.':
            return False
    return True

found_center = False
for row in range(h):
    for col in range(w):
        if picture[row][col] == '*':
            if found_center:
                print("NO")
                exit()
            found_center = True
            if not check_plus_shape(picture, h, w, row, col):
                print("NO")
                exit()

if found_center:
    print("YES")
else:
    print("NO")
