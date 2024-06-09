
# Read input
a, b, c = map(int, input().split())

# Find the missing number
if b - a == c - b:
    print(c + (c - b))
elif b - a > c - b:
    print(a + (c - b))
else:
    print(b + (b - a))
