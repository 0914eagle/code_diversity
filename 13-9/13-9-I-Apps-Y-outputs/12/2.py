
def generate_pascals_triangle(num_rows):
    pascals_triangle = []
    for row in range(num_rows):
        row_values = [1] * (row + 1)
        if row > 0:
            for col in range(1, row):
                row_values[col] = pascals_triangle[row - 1][col - 1] + pascals_triangle[row - 1][col]
        pascals_triangle.append(row_values)
    return pascals_triangle

