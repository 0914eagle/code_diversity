
import sys

n, m = map(int, input().split())
prefectures = {}

for i in range(m):
    prefecture, year = map(int, input().split())
    if prefecture not in prefectures:
        prefectures[prefecture] = []
    prefectures[prefecture].append(year)

for prefecture, years in prefectures.items():
    for i, year in enumerate(sorted(years), start=1):
        print(f"{prefecture:06d}{i:06d}")

