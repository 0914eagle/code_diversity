
a, b, c = map(int, input().split())

if b - a == c - b:
    print(c + (c - b))
elif b - a > c - b:
    print(a + (b - a))
else:
    print(b + (c - b))
