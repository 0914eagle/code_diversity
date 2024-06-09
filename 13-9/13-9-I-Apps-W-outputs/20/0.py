
def is_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (c + a > b)

def solve(n, a):
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if is_triangle(a[i], a[j], a[k]):
                    return "YES"
    return "NO"

