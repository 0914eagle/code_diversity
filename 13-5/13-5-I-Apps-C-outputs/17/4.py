
def read_input():
    N = int(input())
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))
    row3 = list(map(int, input().split()))
    return N, row1, row2, row3

def delete_columns(N, row1, row2, row3):
    # Initialize the number of columns to delete
    num_cols_to_delete = 0
    
    # Iterate through each column
    for col in range(N):
        # Check if the column is identical in all three rows
        if row1[col] == row2[col] == row3[col]:
            # If the column is identical, increment the number of columns to delete
            num_cols_to_delete += 1
    
    return num_cols_to_delete

def main():
    N, row1, row2, row3 = read_input()
    print(delete_columns(N, row1, row2, row3))

if __name__ == '__main__':
    main()

