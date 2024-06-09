
n = int(input())
swimmers = []
for _ in range(n):
    x, y = map(int, input().split())
    swimmers.append((x, y))

swimmers.sort()

x = swimmers[n//2][0]
y = swimmers[n//2][1]

print(f"{x-1} {y}")
print(f"{x+1} {y}")
