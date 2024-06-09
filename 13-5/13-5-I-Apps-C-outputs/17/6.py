
def get_smallest_number_of_columns_to_delete(table):
    # Initialize variables
    num_columns = len(table[0])
    num_rows = len(table)
    columns_to_delete = []

    # Iterate through each column
    for column in range(num_columns):
        # Check if the column is identical in all rows
        identical = True
        for row in range(num_rows):
            if table[row][column] != table[0][column]:
                identical = False
                break

        # If the column is not identical in all rows, add it to the list of columns to delete
        if not identical:
            columns_to_delete.append(column)

    # Return the smallest number of columns to delete
    return len(columns_to_delete)

def main():
    # Read input from stdin
    num_columns = int(input())
    table = []
    for _ in range(3):
        table.append(list(map(int, input().split())))

    # Call the function to get the smallest number of columns to delete
    result = get_smallest_number_of_columns_to_delete(table)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()

