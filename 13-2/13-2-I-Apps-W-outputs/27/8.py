
def f1(n, m):
    matrix = []
    for i in range(n):
        matrix.append(["W"] * m)
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                matrix[i][j] = "B"
            else:
                matrix[i][j] = "W"
    return matrix

def f2(n, m):
    matrix = []
    for i in range(n):
        matrix.append(["W"] * m)
    for i in range(n):
        for j in range(m):
            if j % 2 == 0:
                matrix[i][j] = "B"
            else:
                matrix[i][j] = "W"
    return matrix

if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = f1(n, m)
    for row in matrix:
        print("".join(row))

