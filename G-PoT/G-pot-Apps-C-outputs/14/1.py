
n = int(input())
swimmers = []
for _ in range(n):
    x, y = map(int, input().split())
    swimmers.append((x, y))

swimmers.sort()

x = (swimmers[n//2-1][0] + swimmers[n//2][0]) // 2
y = (swimmers[n//2-1][1] + swimmers[n//2][1]) // 2

print(x, y)
print(x, y)
