
def is_good_table(table):
    for i in range(len(table) - 1):
        if table[i] > table[i + 1]:
            return False
    return True

def remove_column(table, column):
    return [row[:column] + row[column + 1:] for row in table]

def make_table_good(table):
    if is_good_table(table):
        return table
    
    for column in range(len(table[0])):
        new_table = remove_column(table, column)
        if is_good_table(new_table):
            return new_table
    
    return table

def main():
    n, m = map(int, input().split())
    table = [input() for _ in range(n)]
    print(len(make_table_good(table)) - 1)

if __name__ == '__main__':
    main()

