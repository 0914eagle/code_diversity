
def f1(n, m, k, a):
    # Initialize variables
    rows, cols = n, m
    table = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            table[i][j] = a[i][j]
    
    # Check if the table meets the requirement
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 1:
                # Check if the cell is part of a connected component
                if table[i][j] != table[i-1][j] or table[i][j] != table[i][j-1]:
                    return -1
    
    # Check if the table can be changed with at most k cells
    count = 0
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 1 and count < k:
                table[i][j] = 0
                count += 1
    
    # Check if the table meets the requirement after changing k cells
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 1:
                # Check if the cell is part of a connected component
                if table[i][j] != table[i-1][j] or table[i][j] != table[i][j-1]:
                    return -1
    
    return count

def f2(n, m, k, a):
    # Initialize variables
    rows, cols = n, m
    table = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            table[i][j] = a[i][j]
    
    # Check if the table meets the requirement
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 1:
                # Check if the cell is part of a connected component
                if table[i][j] != table[i-1][j] or table[i][j] != table[i][j-1]:
                    return -1
    
    # Check if the table can be changed with at most k cells
    count = 0
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 1 and count < k:
                table[i][j] = 0
                count += 1
    
    # Check if the table meets the requirement after changing k cells
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 1:
                # Check if the cell is part of a connected component
                if table[i][j] != table[i-1][j] or table[i][j] != table[i][j-1]:
                    return -1
    
    return count

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    print(f1(n, m, k, a))
    print(f2(n, m, k, a))

