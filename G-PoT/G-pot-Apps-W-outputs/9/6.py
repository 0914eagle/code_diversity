
n, m, h = map(int, input().split())
front_view = list(map(int, input().split()))
left_view = list(map(int, input().split()))

top_view = []
for _ in range(n):
    row = list(map(int, input().split()))
    top_view.append(row)

result = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        result[i][j] = min(front_view[j], left_view[i], h)

for i in range(n):
    for j in range(m):
        if top_view[i][j] == 0:
            result[i][j] = 0

for row in result:
    print(*row)
