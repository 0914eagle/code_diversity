
def count_grey_cells(R, C, K):
    def is_grey(row, col):
        return bin(row)[2:].zfill(len(bin(R)[2:])) == bin(col)[2:].zfill(len(bin(C)[2:])

    def count_grey_cells_in_row(row):
        return sum(1 for col in range(C) if is_grey(row, col))

    total_grey_cells = 0
    for row in range(R):
        grey_cells_in_row = count_grey_cells_in_row(row)
        if K >= grey_cells_in_row:
            K -= grey_cells_in_row
            total_grey_cells += grey_cells_in_row
        else:
            total_grey_cells += K
            break

    return total_grey_cells

# Input
R, C = map(int, input().split())
K = int(input())

# Output
print(count_grey_cells(R, C, K))
