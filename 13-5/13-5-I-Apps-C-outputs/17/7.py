
def get_smallest_number_of_columns_to_delete(table):
    # Initialize variables
    num_columns = len(table[0])
    num_rows = len(table)
    rows_equal = False
    columns_to_delete = 0

    # Loop through each column and check if all rows are equal
    while not rows_equal:
        for i in range(num_columns):
            column = [row[i] for row in table]
            if len(set(column)) != 1:
                break
        else:
            rows_equal = True
            break

        # If all rows are not equal, delete the current column and sort the rows
        columns_to_delete += 1
        for row in table:
            row.pop(i)
        table = [sorted(row) for row in table]

    return columns_to_delete

def main():
    num_columns = int(input())
    table = []
    for i in range(3):
        table.append(list(map(int, input().split())))
    print(get_smallest_number_of_columns_to_delete(table))

if __name__ == '__main__':
    main()

