
def find_distance(garden, years):
    distances = []
    for year in years:
        row, col = year
        tree_row, tree_col = next((i, j) for i in range(len(garden)) for j in range(len(garden[0])) if garden[i][j] == 'x')
        distances.append((row - tree_row) ** 2 + (col - tree_col) ** 2)
    return distances

