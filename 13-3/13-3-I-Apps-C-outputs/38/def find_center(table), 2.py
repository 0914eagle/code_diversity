
def find_center(table):
    # Initialize variables
    n, m = len(table), len(table[0])
    row_sum, col_sum = [0] * n, [0] * m
    for i in range(n):
        for j in range(m):
            if table[i][j] == "B":
                row_sum[i] += 1
                col_sum[j] += 1
    
    # Find the row and column with the maximum sum
    max_row, max_col = 0, 0
    for i in range(n):
        if row_sum[i] > row_sum[max_row]:
            max_row = i
    for j in range(m):
        if col_sum[j] > col_sum[max_col]:
            max_col = j
    
    # Return the center of the square
    return max_row + 1, max_col + 1

