
def is_rectangle(table, value):
    # Check if the connected component forms a rectangle
    # with sides parallel to the sides of the table
    rows = len(table)
    cols = len(table[0])
    for i in range(rows):
        for j in range(cols):
            if table[i][j] != value:
                return False
    return True

def count_cells(table, value):
    # Count the number of cells in the connected component
    rows = len(table)
    cols = len(table[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == value:
                count += 1
    return count

def can_form_rectangle(table, k):
    # Check if it is possible to form a rectangle with the given k cells
    rows = len(table)
    cols = len(table[0])
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 1:
                # Check if the connected component forms a rectangle
                if is_rectangle(table, 1):
                    # Check if the number of cells in the connected component is correct
                    count = count_cells(table, 1)
                    if count == k:
                        return True
    return False

def solve(n, m, k, table):
    # Check if it is possible to form a rectangle with the given k cells
    if can_form_rectangle(table, k):
        return 0
    # If it is not possible to form a rectangle with the given k cells, try changing one cell at a time
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                table[i][j] = 1
                if can_form_rectangle(table, k):
                    return 1
                table[i][j] = 0
    return -1

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
    print(solve(n, m, k, table))

