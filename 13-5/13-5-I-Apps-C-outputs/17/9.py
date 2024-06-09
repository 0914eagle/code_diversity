
def get_smallest_number_of_columns_to_delete(table):
    # Initialize variables
    num_columns = len(table[0])
    num_rows = len(table)
    rows_are_identical = False
    columns_to_delete = []

    # Loop through each column and check if the rows are identical
    for column_index in range(num_columns):
        column = [row[column_index] for row in table]
        if len(set(column)) == 1:
            columns_to_delete.append(column_index)
        else:
            break

    # If all columns are identical, return the number of columns
    if len(columns_to_delete) == num_columns:
        return num_columns

    # If not all columns are identical, delete the columns and sort the rows
    for column_index in columns_to_delete:
        for row in table:
            row.pop(column_index)
        table = sorted(table)

    # Check if the rows are still identical after deleting the columns
    for row_index in range(num_rows - 1):
        if table[row_index] != table[row_index + 1]:
            rows_are_identical = False
            break
        else:
            rows_are_identical = True

    # If the rows are still identical, return the number of columns deleted
    if rows_are_identical:
        return len(columns_to_delete)

    # If the rows are not identical, delete one more column and try again
    columns_to_delete.append(column_index)
    for column_index in columns_to_delete:
        for row in table:
            row.pop(column_index)
        table = sorted(table)

    # Recursively call the function with the updated table
    return get_smallest_number_of_columns_to_delete(table)

def main():
    table = [[5, 4, 3, 2, 1, 6, 7], [5, 5, 1, 1, 3, 4, 7], [3, 7, 1, 4, 5, 6, 2]]
    print(get_smallest_number_of_columns_to_delete(table))

if __name__ == '__main__':
    main()

