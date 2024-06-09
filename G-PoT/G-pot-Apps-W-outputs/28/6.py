
h, w = map(int, input().split())
picture = [input() for _ in range(h)]

def check_plus_shape(picture, center_row, center_col):
    for i in range(center_row-1, -1, -1):  # Check upwards
        if picture[i][center_col] != '*':
            return False
    for i in range(center_row+1, h):  # Check downwards
        if picture[i][center_col] != '*':
            return False
    for j in range(center_col-1, -1, -1):  # Check leftwards
        if picture[center_row][j] != '*':
            return False
    for j in range(center_col+1, w):  # Check rightwards
        if picture[center_row][j] != '*':
            return False
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
