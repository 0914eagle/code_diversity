
def generate_pascal_triangle(num_rows):
    pascal_triangle = []
    for row in range(num_rows):
        current_row = []
        for col in range(row+1):
            if col == 0 or col == row:
                current_element = 1
            else:
                current_element = pascal_triangle[row-1][col-1] + pascal_triangle[row-1][col]
            current_row.append(current_element)
        pascal_triangle.append(current_row)
    return pascal_triangle

