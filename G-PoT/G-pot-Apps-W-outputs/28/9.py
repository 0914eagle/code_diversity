
h, w = map(int, input().split())
picture = [input() for _ in range(h)]

def check_plus_shape(picture, center_row, center_col):
    # Check left
    for col in range(center_col-1, -1, -1):
        if picture[center_row][col] == '.':
            return False
    # Check right
    for col in range(center_col+1, w):
        if picture[center_row][col] == '.':
            return False
    # Check up
    for row in range(center_row-1, -1, -1):
        if picture[row][center_col] == '.':
            return False
    # Check down
    for row in range(center_row+1, h):
        if picture[row][center_col] == '.':
            return False
    return True

plus_found = False
for row in range(h):
    for col in range(w):
        if picture[row][col] == '*':
            if check_plus_shape(picture, row, col):
                plus_found = True
                break
    if plus_found:
        break

if plus_found:
    print("YES")
else:
    print("NO")
