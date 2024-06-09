
def solve(pine_trees, aspen_trees):
    pine_x = [tree[0] for tree in pine_trees]
    pine_y = [tree[1] for tree in pine_trees]
    aspen_x = [tree[0] for tree in aspen_trees]
    aspen_y = [tree[1] for tree in aspen_trees]

    pine_area = 0
    aspen_area = 0

    for i in range(len(pine_x)):
        for j in range(i+1, len(pine_x)):
            pine_area += triangle_area(pine_x[i], pine_y[i], pine_x[j], pine_y[j], 0, 0)

    for i in range(len(aspen_x)):
        for j in range(i+1, len(aspen_x)):
            aspen_area += triangle_area(aspen_x[i], aspen_y[i], aspen_x[j], aspen_y[j], 0, 0)

    common_area = pine_area + aspen_area - pine_area * aspen_area

    return common_area

def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)

