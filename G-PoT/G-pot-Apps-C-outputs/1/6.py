
def count_grey_cells(R, C, K):
    def is_grey(row, col):
        return bin(row)[2:].zfill(len(bin(R)[2:])) == bin(col)[2:].zfill(len(bin(C)[2:])


    def count_grey_cells_in_row(row):
        if row % 2 == 0:
            return C // 2 + C % 2
        else:
            return C // 2

    total_grey_cells = 0
    current_row = 0
    current_col = 0

    while K > 0:
        if is_grey(current_row, current_col):
            total_grey_cells += 1
            K -= 1

        if current_row % 2 == 0:
            if current_col < C - 1:
                current_col += 1
            else:
                current_row += 1
        else:
            if current_col > 0:
                current_col -= 1
            else:
                current_row += 1

    return total_grey_cells

# Input
R, C = map(int, input().split())
K = int(input())

# Output
print(count_grey_cells(R, C, K))
