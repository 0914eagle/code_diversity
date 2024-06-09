
def get_rectangle(icons):
    
    rows = [icon[0] for icon in icons]
    cols = [icon[1] for icon in icons]
    top = min(rows)
    bottom = max(rows)
    left = min(cols)
    right = max(cols)
    return [top, left, bottom, right]

def get_moves(icons, rectangle):
    
    top, left, bottom, right = rectangle
    moves = 0
    for icon in icons:
        row, col = icon
        if row < top:
            moves += top - row
        elif row > bottom:
            moves += row - bottom
        if col < left:
            moves += left - col
        elif col > right:
            moves += col - right
    return moves

def solve(n_r, n_c, n, m, icons):
    
    rectangle = get_rectangle(icons[:n])
    return get_moves(icons, rectangle)

if __name__ == '__main__':
    n_r, n_c, n, m = map(int, input().split())
    icons = []
    for _ in range(n+m):
        r, c = map(int, input().split())
        icons.append([r, c])
    print(solve(n_r, n_c, n, m, icons))

