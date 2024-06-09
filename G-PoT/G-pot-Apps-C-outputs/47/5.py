
def is_valid_rectangle(table):
    n = len(table)
    m = len(table[0])
    
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                # Check if there is a rectangle with sides parallel to the table
                row_end = i
                while row_end < n and table[row_end][j] == 1:
                    row_end += 1
                col_end = j
                while col_end < m and table[i][col_end] == 1:
                    col_end += 1
                
                for row in range(i, row_end):
                    for col in range(j, col_end):
                        if table[row][col] != 1:
                            return False
                        table[row][col] = -1  # Mark as visited
    return True

def min_cells_to_change(n, m, k, table):
    if k < 0:
        return -1
    
    table_copy = [row[:] for row in table]
    min_changes = float('inf')
    
    for i in range(1 << n*m):
        changes = 0
        for j in range(n):
            for l in range(m):
                if i & (1 << (j*m + l)):
                    table_copy[j][l] = 1 - table_copy[j][l]
                    changes += 1
        
        if is_valid_rectangle(table_copy):
            min_changes = min(min_changes, changes)
        
        table_copy = [row[:] for row in table]
    
    return min_changes if min_changes <= k else -1

n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

result = min_cells_to_change(n, m, k, table)
print(result)
