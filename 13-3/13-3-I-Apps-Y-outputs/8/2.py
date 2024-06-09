
def generate_pascal_triangle(num_rows):
    if num_rows == 0:
        return []
    elif num_rows == 1:
        return [[1]]
    else:
        previous_row = generate_pascal_triangle(num_rows - 1)
        current_row = [1]
        for i in range(1, num_rows):
            current_row.append(previous_row[i - 1] + previous_row[i])
        current_row.append(1)
        return [current_row] + previous_row

if __name__ == '__main__':
    num_rows = int(input("Enter the number of rows: "))
    print(generate_pascal_triangle(num_rows))

