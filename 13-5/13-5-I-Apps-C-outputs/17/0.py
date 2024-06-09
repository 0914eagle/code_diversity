
def read_input():
    N = int(input())
    rows = []
    for i in range(3):
        row = list(map(int, input().split()))
        rows.append(row)
    return N, rows

def delete_columns(N, rows):
    # Initialize the number of columns to delete
    num_cols_to_delete = 0
    
    # Loop through each column
    for col in range(N):
        # Check if the column is unique in all rows
        is_unique = True
        for row in rows:
            if row[col] != row[0]:
                is_unique = False
                break
        
        # If the column is unique in all rows, increment the number of columns to delete
        if is_unique:
            num_cols_to_delete += 1
    
    return num_cols_to_delete

def sort_rows(rows):
    return [sorted(row) for row in rows]

def main():
    N, rows = read_input()
    num_cols_to_delete = delete_columns(N, rows)
    sorted_rows = sort_rows(rows)
    print(num_cols_to_delete)

if __name__ == '__main__':
    main()

