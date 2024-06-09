
def generate_pascals_triangle(num_rows):
    if num_rows == 0:
        return []
    elif num_rows == 1:
        return [[1]]
    else:
        previous_row = generate_pascals_triangle(num_rows - 1)
        current_row = [1]
        for i in range(1, num_rows):
            current_row.append(previous_row[i - 1][0] + previous_row[i - 1][1])
        current_row.append(1)
        return previous_row + [current_row]

