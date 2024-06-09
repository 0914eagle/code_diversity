
def get_largest_square_killer(matrix):
    rows, cols = len(matrix), len(matrix[0])
    largest_killer = 0

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "1":
                current_killer = 1
                for i in range(row, rows):
                    for j in range(col, cols):
                        if matrix[i][j] == "0":
                            break
                        current_killer += 1
                    else:
                        continue
                    break
                largest_killer = max(largest_killer, current_killer)

    return largest_killer

