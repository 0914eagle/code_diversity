
def get_smallest_number_of_columns_to_delete(table):
    # Initialize variables
    num_columns = len(table[0])
    num_rows = len(table)
    rows_same = False
    columns_to_delete = []

    # Loop through each column
    for col in range(num_columns):
        # Check if all rows are the same
        rows_same = True
        for row in range(num_rows):
            if table[row][col] != table[0][col]:
                rows_same = False
                break

        # If all rows are the same, add the column to the list of columns to delete
        if rows_same:
            columns_to_delete.append(col)

    # Return the smallest number of columns to delete
    return len(columns_to_delete)

def main():
    # Read input
    num_columns = int(input())
    table = []
    for _ in range(3):
        table.append(list(map(int, input().split())))

    # Call the function to get the smallest number of columns to delete
    smallest_number_of_columns_to_delete = get_smallest_number_of_columns_to_delete(table)

    # Print the output
    print(smallest_number_of_columns_to_delete)

if __name__ == '__main__':
    main()

