
def count_grey_cells(R, C, K):
    def is_grey(row, col):
        return bin(row)[2:] == '0' or bin(col)[2:] == '0'
    
    def calculate_grey_cells(row, col):
        if is_grey(row, col):
            return 1
        return 0
    
    total_grey_cells = 0
    current_row, current_col = 0, 0
    step = 1
    while K > 0:
        total_grey_cells += calculate_grey_cells(current_row, current_col)
        K -= 1
        if current_col == 0 and step == -1:
            current_row += 1
            step = 1
        elif current_col == C - 1 and step == 1:
            current_row += 1
            step = -1
        else:
            current_col += step
    
    return total_grey_cells

R, C = map(int, input().split())
K = int(input())
print(count_grey_cells(R, C, K))
