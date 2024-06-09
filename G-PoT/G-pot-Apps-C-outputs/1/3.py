
def count_grey_cells(R, C, K):
    def is_grey(row, col):
        return bin(row)[2:] == bin(col)[2:]
    
    count = 0
    for i in range(R):
        for j in range(C):
            if is_grey(i, j):
                count += 1
            if count == K:
                return count
    
    return count

# Input
R, C = map(int, input().split())
K = int(input())

# Output
print(count_grey_cells(R, C, K))
