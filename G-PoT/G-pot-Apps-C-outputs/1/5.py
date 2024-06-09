
def count_grey_cells(R, C, K):
    def is_grey(row, col):
        return bin(row)[2:] == bin(col)[2:]

    def count_grey_cells_in_row(row):
        count = 0
        for col in range(C):
            if is_grey(row, col):
                count += 1
        return count

    total_grey_cells = 0
    for row in range(R):
        total_grey_cells += count_grey_cells_in_row(row)
    
    return total_grey_cells

# Input
R, C = map(int, input().split())
K = int(input())

# Output
print(count_grey_cells(R, C, K))
