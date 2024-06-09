
def f1(n, m, k, a):
    # Initialize variables
    changed_cells = 0
    rows, cols = n, m
    table = [[0] * cols for _ in range(rows)]

    # Fill the table with the given values
    for i in range(rows):
        for j in range(cols):
            table[i][j] = a[i][j]

    # Check if the table meets the requirement
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 1:
                # Check if the cell is part of a connected component
                if table[i][j] != table[i][j-1] or table[i][j] != table[i-1][j]:
                    # Check if the cell can be changed
                    if k > 0:
                        # Change the cell value and decrement the number of available changes
                        table[i][j] = 0
                        changed_cells += 1
                        k -= 1
                    else:
                        # If the number of available changes is zero, return -1
                        return -1

    # If the table meets the requirement, return the number of changed cells
    return changed_cells

def f2(...):
    ...

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    result = f1(n, m, k, a)
    print(result)

