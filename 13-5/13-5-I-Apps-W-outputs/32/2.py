
def is_good_table(table):
    for i in range(len(table) - 1):
        if table[i] > table[i + 1]:
            return False
    return True

def remove_column(table, column):
    return [row[:column] + row[column + 1:] for row in table]

def get_min_columns_to_remove(table):
    min_columns = 0
    for column in range(len(table[0])):
        if is_good_table(remove_column(table, column)):
            min_columns += 1
    return min_columns

def main():
    n, m = map(int, input().split())
    table = [input() for _ in range(n)]
    print(get_min_columns_to_remove(table))

if __name__ == '__main__':
    main()

