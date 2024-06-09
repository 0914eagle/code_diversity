
a, b, c = map(int, input().split())

if a + c == 2 * b:
    print(c + (b - a))
elif b - a == c - b:
    print(c + (c - b))
elif c - b == b - a:
    print(a - (b - a))
