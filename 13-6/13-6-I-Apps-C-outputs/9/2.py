
def get_delete_rectangle(icons, n_rows, n_cols):
    
    icons_to_delete = icons[:n]
    rows = [icon[0] for icon in icons_to_delete]
    cols = [icon[1] for icon in icons_to_delete]
    top = min(rows)
    bottom = max(rows)
    left = min(cols)
    right = max(cols)
    return [top, left, bottom, right]

def get_moves_required(icons, n_rows, n_cols):
    
    delete_rectangle = get_delete_rectangle(icons, n_rows, n_cols)
    top, left, bottom, right = delete_rectangle
    moves = 0
    for icon in icons[n:]:
        r, c = icon
        if r < top or r > bottom or c < left or c > right:
            moves += 1
    return moves

def main():
    n_rows, n_cols, n, m = map(int, input().split())
    icons = []
    for _ in range(n+m):
        r, c = map(int, input().split())
        icons.append([r, c])
    print(get_moves_required(icons, n_rows, n_cols))

if __name__ == '__main__':
    main()

