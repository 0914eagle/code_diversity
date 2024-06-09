
def count_grey_cells(R, C, K):
    def count_ones(n):
        count = 0
        while n:
            count += 1
            n &= (n - 1)
        return count

    def is_grey(row, col):
        return count_ones(row) % 2 == 0 or count_ones(col) % 2 == 0

    total_grey = 0
    for i in range(K):
        row = i // C
        col = i % C
        if is_grey(row, col):
            total_grey += 1

    return total_grey

# Read input
R, C = map(int, input().split())
K = int(input())

result = count_grey_cells(R, C, K)
print(result)
