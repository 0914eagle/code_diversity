
h, w = map(int, input().split())
picture = [input() for _ in range(h)]

def check_plus_shape(picture, center_row, center_col):
    # Check left
    left = center_col - 1
    while left >= 0 and picture[center_row][left] == '*':
        left -= 1
    if left < 0 or picture[center_row][left] != '*':
        return False
    
    # Check right
    right = center_col + 1
    while right < w and picture[center_row][right] == '*':
        right += 1
    if right >= w or picture[center_row][right] != '*':
        return False
    
    # Check up
    up = center_row - 1
    while up >= 0 and picture[up][center_col] == '*':
        up -= 1
    if up < 0 or picture[up][center_col] != '*':
        return False
    
    # Check down
    down = center_row + 1
    while down < h and picture[down][center_col] == '*':
        down += 1
    if down >= h or picture[down][center_col] != '*':
        return False
    
    return True

found_plus = False
for i in range(h):
    for j in range(w):
        if picture[i][j] == '*':
            if check_plus_shape(picture, i, j):
                found_plus = True
                break

if found_plus:
    print("YES")
else:
    print("NO")
