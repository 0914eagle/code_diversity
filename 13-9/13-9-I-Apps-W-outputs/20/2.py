
def is_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (c + a > b)

def solve(n, line_segments):
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if is_triangle(line_segments[i], line_segments[j], line_segments[k]):
                    return "YES"
    return "NO"

