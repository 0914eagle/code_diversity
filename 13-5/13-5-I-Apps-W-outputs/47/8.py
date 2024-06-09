
def generate_beautiful_table(n, k):
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            table[i][j] = (i + j) % k + 1
    return table

def print_beautiful_table(table):
    for row in table:
        print(*row)

if __name__ == '__main__':
    n, k = map(int, input().split())
    table = generate_beautiful_table(n, k)
    print_beautiful_table(table)

