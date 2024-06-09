
def count_grey_cells(R, C, K):
    def is_grey(row, col):
        return bin(row)[2:] == '0' or bin(col)[2:] == '0'

    def count_grey_cells_in_row(row):
        if row == 0:
            return C
        elif row == 1:
            return C - 1
        else:
            return min(C, K // row)

    total_grey_cells = 0
    for row in range(R):
        grey_cells_in_row = count_grey_cells_in_row(row)
        if K >= grey_cells_in_row:
            total_grey_cells += grey_cells_in_row
            K -= grey_cells_in_row
        else:
            total_grey_cells += K
            break

    return total_grey_cells

# Input
R, C = map(int, input().split())
K = int(input())

# Output
print(count_grey_cells(R, C, K))
