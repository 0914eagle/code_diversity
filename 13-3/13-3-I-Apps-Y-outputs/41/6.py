
t = int(input())

for i in range(t):
    a, b, c, n = map(int, input().split())
    if n % 3 == 0 and a + b + c == n:
        print("YES")
    else:
        print("NO")

