
def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

def is_non_degenerate_triangle(a, b, c):
    return is_triangle(a, b, c) and a != b and b != c and a != c

def solve(n, lengths):
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if is_non_degenerate_triangle(lengths[i], lengths[j], lengths[k]):
                    return "YES"
    return "NO"

