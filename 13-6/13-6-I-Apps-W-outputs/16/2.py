
def find_beautiful_table(n, k):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i + j == k:
                return [i, j]
    return []

