
def is_signature_forgable(signature):
    n, m = len(signature), len(signature[0])
    for i in range(n):
        for j in range(m):
            if signature[i][j] == '#':
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if k < n and l < m and signature[k][l] == '#':
                            return "YES"
    return "NO"

