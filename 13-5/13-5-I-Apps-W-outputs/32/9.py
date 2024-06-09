
def is_good_table(table):
    for i in range(len(table) - 1):
        if table[i] > table[i + 1]:
            return False
    return True

def remove_column(table, col):
    return [row[:col] + row[col + 1:] for row in table]

def min_columns_to_make_good(table):
    if is_good_table(table):
        return 0
    min_columns = len(table[0])
    for col in range(len(table[0])):
        new_table = remove_column(table, col)
        min_columns = min(min_columns, 1 + min_columns_to_make_good(new_table))
    return min_columns

if __name__ == '__main__':
    n, m = map(int, input().split())
    table = [input() for _ in range(n)]
    print(min_columns_to_make_good(table))

