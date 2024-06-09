
def max_rectangle_area(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    max_area = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1":
                area = 0
                for k in range(i, rows):
                    if matrix[k][j] == "0":
                        break
                    area += 1
                max_area = max(max_area, area)
    return max_area

