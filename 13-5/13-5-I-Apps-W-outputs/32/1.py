
def get_good_table(table):
    # Sort the table rows lexicographically
    table.sort()
    # Check if the table is already good
    if is_good_table(table):
        return 0
    # Remove columns until the table is good
    removed_columns = 0
    while not is_good_table(table):
        removed_columns += 1
        table = remove_column(table)
    return removed_columns

def is_good_table(table):
    # Check if all rows are lexicographically larger than the previous one
    for i in range(len(table) - 1):
        if table[i] >= table[i + 1]:
            return False
    return True

def remove_column(table):
    # Remove the last column of the table
    return [row[:-1] for row in table]

if __name__ == '__main__':
    n, m = map(int, input().split())
    table = [input() for _ in range(n)]
    print(get_good_table(table))

