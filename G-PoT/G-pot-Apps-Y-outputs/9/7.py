
a, b, c = map(int, input().split())

if b - a == c - b:
    print(c + (c - b))
elif b - a > c - b:
    print(a + (c - b))
else:
    print(b + (b - a))
