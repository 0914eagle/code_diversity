
def sum_abc(a, b, c):
    return (a * b * c) % 998244353

def solve(a, b, c):
    result = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                result += sum_abc(i, j, k)
    return result % 998244353

