
t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    s = "abcdefghijklmnopqrstuvwxyz"[:b] * (n // a)
    s += "abcdefghijklmnopqrstuvwxyz"[:n % a]
    print(s)
