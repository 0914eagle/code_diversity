
a, b, c = map(int, input().split())

if b - a == c - b:
    print(c + (b - a))
elif b - a > c - b:
    print(a + (c - b))
else:
    print(b + (b - a))
