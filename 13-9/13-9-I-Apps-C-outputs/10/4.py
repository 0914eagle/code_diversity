
def get_squared_distances(fruit_garden, years_data):
    distances = []
    for year_data in years_data:
        row, col = year_data
        distances.append(get_squared_distance(fruit_garden, row, col))
    return distances

def get_squared_distance(fruit_garden, row, col):
    tree_row, tree_col = find_tree(fruit_garden, row, col)
    return (row - tree_row) ** 2 + (col - tree_col) ** 2

def find_tree(fruit_garden, row, col):
    for r in range(row):
        for c in range(col):
            if fruit_garden[r][c] == 'x':
                return r, c
    return row, col

