
def is_rectangle_possible(piece):
    n, m = piece.shape
    x_coords, y_coords = np.where(piece == 'X')
    x_min, x_max = x_coords.min(), x_coords.max()
    y_min, y_max = y_coords.min(), y_coords.max()
    if x_max - x_min != m - 1 or y_max - y_min != n - 1:
        return "NO"
    for i in range(n):
        for j in range(m):
            if piece[i, j] == 'X' and (i, j) not in zip(x_coords, y_coords):
                return "NO"
    return "YES"

