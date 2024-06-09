
def count_rectangles(a, s):
    n = len(s)
    b = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i, n):
            b[i][j + 1] = b[i][j] + int(s[j])
    rectangles = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    if b[i][k + 1] - b[i][j] == b[l + 1][k + 1] - b[l + 1][j]:
                        rectangles += 1
    return rectangles

if __name__ == '__main__':
    a = int(input())
    s = input()
    print(count_rectangles(a, s))

