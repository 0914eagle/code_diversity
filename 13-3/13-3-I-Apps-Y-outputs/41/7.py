
def is_possible(a, b, c, n):
    if a + b + c != n:
        return "NO"
    if a == b == c:
        return "YES"
    if a == b or b == c or c == a:
        return "YES"
    return "NO"

t = int(input())
for i in range(t):
    a, b, c, n = map(int, input().split())
    print(is_possible(a, b, c, n))

