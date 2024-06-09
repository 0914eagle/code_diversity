
def is_sorted_in_column(table, l, r):
    for j in range(len(table[0])):
        for i in range(l, r):
            if table[i][j] > table[i+1][j]:
                return False
    return True

def solve(table, tasks):
    result = []
    for l, r in tasks:
        result.append("Yes" if is_sorted_in_column(table, l, r) else "No")
    return result

