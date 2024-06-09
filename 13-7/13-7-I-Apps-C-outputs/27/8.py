
def solve(n, m, k, a):
    # Initialize variables
    rows, cols = {}, {}
    for i in range(n):
        for j in range(m):
            val = a[i][j]
            if val == 0:
                continue
            if i not in rows:
                rows[i] = {}
            if j not in rows[i]:
                rows[i][j] = 1
            if j not in cols:
                cols[j] = {}
            if i not in cols[j]:
                cols[j][i] = 1
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if 0 <= x < n and 0 <= y < m and a[x][y] == val:
                        if x not in rows[i]:
                            rows[i][x] = 1
                        if y not in cols[j]:
                            cols[j][y] = 1

    # Check if it is possible to form a rectangle with the given cells
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                if i not in rows or j not in cols or len(rows[i]) != len(cols[j]):
                    return -1

    # Calculate the minimum number of cells that need to be changed
    count = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1 and len(rows[i]) * len(cols[j]) > k:
                count += 1

    return count

