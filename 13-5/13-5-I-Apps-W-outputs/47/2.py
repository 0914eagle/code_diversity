
def get_beautiful_table(n, k):
    # Initialize a table with n rows and n columns
    table = [[0] * n for _ in range(n)]
    
    # Fill the table with numbers from 1 to n^2
    nums = list(range(1, n**2 + 1))
    for i in range(n):
        for j in range(n):
            table[i][j] = nums[i * n + j]
    
    # Check if the table is beautiful
    if is_beautiful(table, k):
        return table
    else:
        return []

def is_beautiful(table, k):
    # Check if the sum of elements in each row equals k
    for i in range(len(table)):
        if sum(table[i]) != k:
            return False
    
    # Check if the sum of elements in each column equals k
    for j in range(len(table[0])):
        col_sum = 0
        for i in range(len(table)):
            col_sum += table[i][j]
        if col_sum != k:
            return False
    
    return True

if __name__ == '__main__':
    n, k = map(int, input().split())
    table = get_beautiful_table(n, k)
    if table:
        for row in table:
            print(*row)
    else:
        print(-1)

