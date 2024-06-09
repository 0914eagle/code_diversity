
def get_good_table(table):
    n, m = len(table), len(table[0])
    for i in range(m):
        for j in range(n-1):
            if table[j][i] > table[j+1][i]:
                return False
    return True

def remove_column(table, col):
    return [row[:col] + row[col+1:] for row in table]

def get_min_operations(table):
    n, m = len(table), len(table[0])
    min_operations = 0
    for i in range(m):
        if not get_good_table(remove_column(table, i)):
            min_operations += 1
    return min_operations

if __name__ == '__main__':
    n, m = map(int, input().split())
    table = [input() for _ in range(n)]
    print(get_min_operations(table))

