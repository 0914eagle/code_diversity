
t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    ans = ""
    for i in range(n):
        ans += chr(ord('a') + (i % b))
    print(ans)
