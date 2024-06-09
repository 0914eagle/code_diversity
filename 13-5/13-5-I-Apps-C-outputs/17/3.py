
def read_input():
    N = int(input())
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))
    row3 = list(map(int, input().split()))
    return N, row1, row2, row3

def delete_columns(N, row1, row2, row3):
    # Initialize the number of columns to delete
    num_columns_to_delete = 0
    
    # Loop through each column
    for i in range(N):
        # Check if the columns are identical
        if row1[i] == row2[i] == row3[i]:
            # If they are, increment the number of columns to delete
            num_columns_to_delete += 1
    
    return num_columns_to_delete

def main():
    N, row1, row2, row3 = read_input()
    print(delete_columns(N, row1, row2, row3))

if __name__ == '__main__':
    main()

