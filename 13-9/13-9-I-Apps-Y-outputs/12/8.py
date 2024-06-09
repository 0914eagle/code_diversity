
def generate_pascal_triangle(num_rows):
    pascal_triangle = []
    for row in range(num_rows):
        current_row = [1] * (row + 1)
        if row > 0:
            for col in range(1, row):
                current_row[col] = pascal_triangle[row - 1][col - 1] + pascal_triangle[row - 1][col]
        pascal_triangle.append(current_row)
    return pascal_triangle

