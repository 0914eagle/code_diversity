
import sys

n, m = map(int, input().split())
prefectures = [[] for _ in range(n + 1)]

for i in range(m):
    p, y = map(int, input().split())
    prefectures[p].append((y, i))

for prefecture in prefectures:
    prefecture.sort()

for prefecture in prefectures:
    for city in prefecture:
        print(f"{str(prefecture[0][0]).zfill(6)}{str(city[1]).zfill(6)}")

