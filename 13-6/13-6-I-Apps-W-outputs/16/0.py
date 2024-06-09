
def find_beautiful_table(n, k):
    for i in range(1, 1001):
        table = [[0] * n for _ in range(n)]
        table[0][0] = i
        if is_beautiful_table(table, n, k):
            return table
    return None

def is_beautiful_table(table, n, k):
    for i in range(n):
        row_sum = sum(table[i])
        if row_sum != k:
            return False
    for j in range(n):
        col_sum = sum(table[i][j] for i in range(n))
        if col_sum != k:
            return False
    return True

