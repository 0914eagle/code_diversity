
t = int(input())

for i in range(t):
    a, b, c, n = map(int, input().split())
    
    if n % 3 == 0 and n // 3 >= max(a, b, c):
        print("YES")
    else:
        print("NO")

