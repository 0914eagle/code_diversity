
def is_rectangle_possible(puzzle_piece):
    n, m = len(puzzle_piece), len(puzzle_piece[0])
    x_coords, y_coords = [], []
    for i in range(n):
        for j in range(m):
            if puzzle_piece[i][j] == "X":
                x_coords.append(i)
                y_coords.append(j)
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)
    width, height = max_x - min_x + 1, max_y - min_y + 1
    return width == height and width * height == n * m

