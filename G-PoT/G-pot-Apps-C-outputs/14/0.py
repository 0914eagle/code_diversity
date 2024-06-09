
n = int(input())
swimmers = []
for _ in range(n):
    x, y = map(int, input().split())
    swimmers.append((x, y))

swimmers.sort()

mid = n // 2
x1, y1 = swimmers[mid-1]
x2, y2 = swimmers[mid]

print(x1 + x2, y1 + y2)
print(x1 - x2, y1 - y2)
