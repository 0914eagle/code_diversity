
def get_shared_area(pine_trees, aspen_trees):
    pine_x = [tree[0] for tree in pine_trees]
    pine_y = [tree[1] for tree in pine_trees]
    aspen_x = [tree[0] for tree in aspen_trees]
    aspen_y = [tree[1] for tree in aspen_trees]

    pine_area = 0
    aspen_area = 0

    for i in range(len(pine_x)):
        for j in range(i+1, len(pine_x)):
            pine_area += get_triangle_area(pine_x[i], pine_y[i], pine_x[j], pine_y[j], pine_x[0], pine_y[0])

    for i in range(len(aspen_x)):
        for j in range(i+1, len(aspen_x)):
            aspen_area += get_triangle_area(aspen_x[i], aspen_y[i], aspen_x[j], aspen_y[j], aspen_x[0], aspen_y[0])

    shared_area = pine_area + aspen_area - get_triangle_area(0, 0, 0, 0, 0, 0)

    return shared_area

def get_triangle_area(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2)
    return area

