
def get_beautiful_table(n, k):
    table = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            table[i][j] = (i + j) % k + 1
    return table

