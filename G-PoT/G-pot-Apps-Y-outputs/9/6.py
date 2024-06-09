
a, b, c = map(int, input().split())

if b - a == c - b:
    print(c + (b - a))
elif a - b == b - c:
    print(a + (b - c))
else:
    print(b + (c - a))
