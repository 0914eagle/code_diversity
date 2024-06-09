
def generate_pascals_triangle(num_rows):
    triangle = []
    for row in range(num_rows):
        triangle.append([])
        for col in range(row+1):
            if col == 0 or col == row:
                triangle[row].append(1)
            else:
                triangle[row].append(triangle[row-1][col-1] + triangle[row-1][col])
    return triangle

