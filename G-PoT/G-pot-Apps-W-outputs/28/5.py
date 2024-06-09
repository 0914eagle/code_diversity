
h, w = map(int, input().split())
picture = [input() for _ in range(h)]

def check_plus_shape(picture, center_row, center_col):
    for i in range(center_row-1, -1, -1):  # Check upward ray
        if picture[i][center_col] == '.':
            return False
        if picture[i][center_col] == '*':
            break
    for i in range(center_row+1, h):  # Check downward ray
        if picture[i][center_col] == '.':
            return False
        if picture[i][center_col] == '*':
            break
    for j in range(center_col-1, -1, -1):  # Check leftward ray
        if picture[center_row][j] == '.':
            return False
        if picture[center_row][j] == '*':
            break
    for j in range(center_col+1, w):  # Check rightward ray
        if picture[center_row][j] == '.':
            return False
        if picture[center_row][j] == '*':
            break
    return True

plus_found = False
for i in range(h):
    for j in range(w):
        if picture[i][j] == '*':
            if check_plus_shape(picture, i, j):
                plus_found = True
                break

if plus_found:
    print("YES")
else:
    print("NO")
