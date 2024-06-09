
def is_triangle(a, b, c):
    return a + b > c and b + c > a and a + c > b

def solve(n, lengths):
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if is_triangle(lengths[i], lengths[j], lengths[k]):
                    return "YES"
    return "NO"

