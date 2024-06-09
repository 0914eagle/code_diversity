
def count_grey_cells(R, C, K):
    def is_grey(row, col):
        return bin(row)[2:] == bin(col)[2:]
    
    def count_grey_cells_in_row(row):
        if row == 0:
            return C
        return min(row+1, C)
    
    def count_grey_cells_in_col(col):
        if col == 0:
            return R
        return min(col+1, R)
    
    def count_grey_cells_in_diagonal(diagonal):
        if diagonal < min(R, C):
            return diagonal + 1
        return min(R, C) - (diagonal - min(R, C)) + 1
    
    total_grey_cells = 0
    for i in range(K):
        row = i // C
        col = i % C
        if is_grey(row, col):
            total_grey_cells += 1
        else:
            total_grey_cells += count_grey_cells_in_row(row) + count_grey_cells_in_col(col) - 1
            total_grey_cells -= count_grey_cells_in_diagonal(row + col)
    
    return total_grey_cells

# Input
R, C = map(int, input().split())
K = int(input())

# Output
print(count_grey_cells(R, C, K))
