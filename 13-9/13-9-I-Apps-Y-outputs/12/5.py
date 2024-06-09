
def generate_pascal_triangle(num_rows):
    pascal_triangle = []
    for row in range(num_rows):
        current_row = []
        for col in range(row+1):
            if col == 0 or col == row:
                current_value = 1
            else:
                previous_row = pascal_triangle[row-1]
                current_value = previous_row[col-1] + previous_row[col]
            current_row.append(current_value)
        pascal_triangle.append(current_row)
    return pascal_triangle

