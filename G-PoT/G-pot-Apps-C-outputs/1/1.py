
def count_grey_cells(R, C, K):
    def is_grey(row, col):
        return bin(row)[2:] == '0' or bin(col)[2:] == '0'
    
    def count_grey_cells_in_row(row):
        return C - bin(row).count('1')
    
    def count_grey_cells_in_col(col):
        return R - bin(col).count('1')
    
    total_grey_cells = 0
    for i in range(K):
        row = i // C
        col = i % C
        if is_grey(row, col):
            total_grey_cells += 1
    
    remaining_grey_cells = total_grey_cells
    for i in range(K, R * C):
        row = i // C
        col = i % C
        if is_grey(row, col):
            remaining_grey_cells += 1
        if remaining_grey_cells == K:
            break
    
    return remaining_grey_cells

# Read input
R, C = map(int, input().split())
K = int(input())

# Output the result
print(count_grey_cells(R, C, K))
