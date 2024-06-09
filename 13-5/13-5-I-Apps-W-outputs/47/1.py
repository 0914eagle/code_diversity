
def generate_table(n, k):
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            table[i][j] = (i + j) % k + 1
    return table

def is_beautiful_table(table):
    n = len(table)
    for i in range(n):
        row_sum = sum(table[i])
        if row_sum != k:
            return False
    for j in range(n):
        col_sum = sum(row[j] for row in table)
        if col_sum != k:
            return False
    return True

def main():
    n, k = map(int, input().split())
    table = generate_table(n, k)
    if is_beautiful_table(table):
        for row in table:
            print(*row)
    else:
        print(-1)

if __name__ == '__main__':
    main()

