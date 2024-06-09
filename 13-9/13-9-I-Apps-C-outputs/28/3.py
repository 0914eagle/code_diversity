
def find_largest_square_killer(matrix):
    rows, cols = len(matrix), len(matrix[0])
    largest_killer = -1
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1":
                killer_size = 1
                for x in range(i, rows):
                    for y in range(j, cols):
                        if matrix[x][y] == "0":
                            break
                        killer_size += 1
                    if killer_size > largest_killer:
                        largest_killer = killer_size
    return largest_killer

