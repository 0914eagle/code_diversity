
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

def can_change_k_cells(table, k):
    # Check if it is possible to change at most k cells
    # so that the table meets the requirement
    rows = len(table)
    cols = len(table[0])
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 0:
                # Try changing the current cell to 1
                table[i][j] = 1
                if is_rectangle(table, 1):
                    # If the table forms a rectangle, check if we can change at most k cells
                    cells_changed = count_cells(table, 1)
                    if cells_changed <= k:
                        return True
                table[i][j] = 0
    return False

def min_cells_to_change(table, k):
    # Find the minimum number of cells that need to be changed
    # so that the table meets the requirement
    rows = len(table)
    cols = len(table[0])
    min_cells = float('inf')
    for i in range(rows):
        for j in range(cols):
            if table[i][j] == 0:
                # Try changing the current cell to 1
                table[i][j] = 1
                if is_rectangle(table, 1):
                    # If the table forms a rectangle, check if we can change at most k cells
                    cells_changed = count_cells(table, 1)
                    if cells_changed <= k and cells_changed < min_cells:
                        min_cells = cells_changed
                table[i][j] = 0
    return min_cells

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
    if can_change_k_cells(table, k):
        print(min_cells_to_change(table, k))
    else:
        print(-1)

