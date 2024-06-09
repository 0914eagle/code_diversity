
def get_min_operations(table):
    # Initialize variables
    n, m = len(table), len(table[0])
    good_cells = []
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                good_cells.append((i, j))
    operations = 0

    # Loop through all good cells
    for i in range(len(good_cells)):
        for j in range(i+1, len(good_cells)):
            # Get the coordinates of the two good cells
            x1, y1 = good_cells[i]
            x2, y2 = good_cells[j]

            # Check if the two good cells are in the same row or column
            if x1 == x2 or y1 == y2:
                continue

            # Get the minimum and maximum values of the two good cells
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)

            # Loop through all cells in the table
            for i in range(n):
                for j in range(m):
                    # Check if the current cell is in the rectangle defined by the two good cells
                    if min_x <= i <= max_x and min_y <= j <= max_y:
                        # Increment the number of operations
                        operations += 1

    return operations

def main():
    n, m = map(int, input().split())
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
    print(get_min_operations(table))

if __name__ == '__main__':
    main()

