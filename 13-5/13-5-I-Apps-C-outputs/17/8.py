
def get_smallest_number_of_columns_to_delete(table):
    # Initialize variables
    num_columns = len(table[0])
    num_rows = len(table)
    rows_are_identical = False
    columns_to_delete = []

    # Iterate through each column
    for column_index in range(num_columns):
        # Check if the column values are identical in all rows
        for row_index in range(num_rows):
            if table[row_index][column_index] != table[0][column_index]:
                break
        else:
            # If the column values are identical in all rows, add the column index to the list of columns to delete
            columns_to_delete.append(column_index)

    # Return the smallest number of columns to delete
    return len(columns_to_delete)

def main():
    # Read the input table
    num_rows = int(input())
    table = []
    for _ in range(num_rows):
        table.append(list(map(int, input().split())))

    # Call the function to get the smallest number of columns to delete
    smallest_number_of_columns_to_delete = get_smallest_number_of_columns_to_delete(table)

    # Print the result
    print(smallest_number_of_columns_to_delete)

if __name__ == '__main__':
    main()

