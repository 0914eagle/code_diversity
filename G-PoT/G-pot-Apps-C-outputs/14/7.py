
n = int(input())
swimmers = []
for _ in range(n):
    x, y = map(int, input().split())
    swimmers.append((x, y))

swimmers.sort()

mid = n // 2
you = swimmers[mid]
coworker = swimmers[mid - 1]

print(you[0] + coworker[0], you[1] + coworker[1])
print(you[0] - coworker[0], you[1] - coworker[1])
