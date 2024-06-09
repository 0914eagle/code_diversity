
def get_squared_distances(fruit_garden, apple_falls):
    distances = []
    for fall in apple_falls:
        row, col = fall
        tree_row, tree_col = next((r, c) for r, c in enumerate(fruit_garden[row]) if c == "x")
        distance = (row - tree_row) ** 2 + (col - tree_col) ** 2
        distances.append(distance)
    return distances

