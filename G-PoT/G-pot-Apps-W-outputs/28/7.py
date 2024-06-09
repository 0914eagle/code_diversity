
h, w = map(int, input().split())
picture = [input() for _ in range(h)]

def check_plus_shape(picture, center_row, center_col):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in directions:
        row, col = center_row + dr, center_col + dc
        while 0 <= row < h and 0 <= col < w and picture[row][col] == '*':
            row += dr
            col += dc
        if not (0 <= row < h and 0 <= col < w and picture[row][col] == '.'):
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
