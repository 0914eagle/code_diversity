
def print_beautiful_table(n, k):
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            table[i][j] = (i + j) % k + 1
    return table

