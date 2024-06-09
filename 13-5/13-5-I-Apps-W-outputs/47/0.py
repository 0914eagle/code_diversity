
def is_beautiful_table(table, k):
    # Check if the sum of elements in each row is equal to k
    for row in table:
        if sum(row) != k:
            return False
    
    # Check if the sum of elements in each column is equal to k
    for i in range(len(table[0])):
        column_sum = 0
        for row in table:
            column_sum += row[i]
        if column_sum != k:
            return False
    
    return True

def find_beautiful_table(n, k):
    # Initialize a table with n rows and n columns
    table = [[0 for _ in range(n)] for _ in range(n)]
    
    # Fill the table with numbers from 1 to n^2
    nums = list(range(1, n*n+1))
    for i in range(n):
        for j in range(n):
            table[i][j] = nums[i*n+j]
    
    # Check if the table is beautiful
    if is_beautiful_table(table, k):
        return table
    
    # If the table is not beautiful, return an empty table
    return []

if __name__ == '__main__':
    n, k = map(int, input().split())
    table = find_beautiful_table(n, k)
    if table:
        for row in table:
            print(*row)
    else:
        print(-1)

