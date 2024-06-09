
def solve(n, m, k, a):
    # Initialize variables
    rows, cols = {}, {}
    for i in range(n):
        for j in range(m):
            val = a[i][j]
            if val not in rows:
                rows[val] = 1
            else:
                rows[val] += 1
            if val not in cols:
                cols[val] = 1
            else:
                cols[val] += 1
    
    # Check if it is possible to meet the requirement with at most k changes
    count = 0
    for val in rows:
        if rows[val] % val != 0:
            count += rows[val] // val + 1
        else:
            count += rows[val] // val
    for val in cols:
        if cols[val] % val != 0:
            count += cols[val] // val + 1
        else:
            count += cols[val] // val
    if count > k:
        return -1
    
    # Return the minimum number of cells that need to be changed
    return count

