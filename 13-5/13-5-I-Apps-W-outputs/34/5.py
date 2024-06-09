
def is_sorted_in_non_decreasing_order(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] > table[i+1][j]:
                return False
    return True

def solve(table, l, r):
    return "Yes" if is_sorted_in_non_decreasing_order([row for row in table[l-1:r]]) else "No"

