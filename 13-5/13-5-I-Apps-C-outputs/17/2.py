
def read_input():
    N = int(input())
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))
    row3 = list(map(int, input().split()))
    return N, row1, row2, row3

def delete_columns(N, row1, row2, row3):
    # find the columns that need to be deleted
    columns_to_delete = set()
    for i in range(N):
        if row1[i] != row2[i] or row1[i] != row3[i]:
            columns_to_delete.add(i)
    
    # delete the columns
    for i in sorted(columns_to_delete, reverse=True):
        row1.pop(i)
        row2.pop(i)
        row3.pop(i)
    
    return row1, row2, row3

def sort_rows(row1, row2, row3):
    return sorted(row1), sorted(row2), sorted(row3)

def find_min_columns_to_delete(N, row1, row2, row3):
    # find the minimum number of columns that need to be deleted
    min_columns_to_delete = N
    for i in range(N):
        row1_sorted, row2_sorted, row3_sorted = delete_columns(N, row1, row2, row3)
        if row1_sorted == row2_sorted == row3_sorted:
            min_columns_to_delete = min(min_columns_to_delete, i)
    
    return min_columns_to_delete

def main():
    N, row1, row2, row3 = read_input()
    min_columns_to_delete = find_min_columns_to_delete(N, row1, row2, row3)
    print(min_columns_to_delete)

if __name__ == '__main__':
    main()

