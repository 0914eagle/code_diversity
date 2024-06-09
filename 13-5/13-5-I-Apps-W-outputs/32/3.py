
def is_good_table(table):
    for i in range(len(table) - 1):
        if table[i] > table[i + 1]:
            return False
    return True

def remove_column(table, column):
    return [row[column] for row in table]

def get_min_columns_to_remove(table):
    min_columns_to_remove = 0
    for column in range(len(table[0])):
        column_values = remove_column(table, column)
        if not is_good_table(column_values):
            min_columns_to_remove += 1
    return min_columns_to_remove

if __name__ == '__main__':
    n, m = map(int, input().split())
    table = [input() for _ in range(n)]
    print(get_min_columns_to_remove(table))

