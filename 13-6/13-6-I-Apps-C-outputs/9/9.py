
def get_rectangle(icons):
    
    rows = [icon[0] for icon in icons]
    cols = [icon[1] for icon in icons]
    top = min(rows)
    left = min(cols)
    bottom = max(rows)
    right = max(cols)
    return [top, left, bottom, right]

def get_delete_rectangle(icons, delete_icons):
    
    delete_rectangle = get_rectangle(delete_icons)
    for icon in icons:
        if icon not in delete_icons:
            rectangle = get_rectangle([icon, delete_icons[0]])
            delete_rectangle = [min(delete_rectangle[0], rectangle[0]), min(delete_rectangle[1], rectangle[1]), max(delete_rectangle[2], rectangle[2]), max(delete_rectangle[3], rectangle[3])]
    return delete_rectangle

def get_moves(icons, delete_icons):
    
    delete_rectangle = get_delete_rectangle(icons, delete_icons)
    top, left, bottom, right = delete_rectangle
    return (bottom - top) * (right - left)

def main():
    n_r, n_c, n, m = map(int, input().split())
    icons = []
    for _ in range(n+m):
        r, c = map(int, input().split())
        icons.append((r, c))
    delete_icons = icons[:n]
    moves = get_moves(icons, delete_icons)
    print(moves)

if __name__ == '__main__':
    main()

