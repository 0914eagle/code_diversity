
def is_valid_rectangle(table, start_row, start_col, end_row, end_col):
    value = table[start_row][start_col]
    for i in range(start_row, end_row + 1):
        for j in range(start_col, end_col + 1):
            if table[i][j] != value:
                return False
    return True

def min_cells_to_change(n, m, k, table):
    min_changes = float('inf')
    
    for start_row in range(n):
        for end_row in range(start_row, n):
            for start_col in range(m):
                for end_col in range(start_col, m):
                    if is_valid_rectangle(table, start_row, start_col, end_row, end_col):
                        count_changes = 0
                        for i in range(n):
                            for j in range(m):
                                if not (start_row <= i <= end_row and start_col <= j <= end_col):
                                    count_changes += 1
                        if count_changes <= k:
                            min_changes = min(min_changes, count_changes)
    
    return min_changes if min_changes != float('inf') else -1

n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

result = min_cells_to_change(n, m, k, table)
print(result)
